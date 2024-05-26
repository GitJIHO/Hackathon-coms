from flask import Flask, request, render_template
import tensorflow as tf
import requests
from deep_translator import GoogleTranslator
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import sys
import cv2
import base64
from langdetect import detect
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import session




# 재귀 깊이 제한 증가 (일시적인 해결책)
sys.setrecursionlimit(10000)

REST_API_KEY = 'a98c47a7fdcca1ecc24765726681da78'

app = Flask(__name__)

# 모델 로드
model = load_model('emotion_model.h5')

# 감정 레이블
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def detect_face(img_path):
    # 이미지 읽기
    img = cv2.imread(img_path)
    # Haar Cascade 분류기 로드
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # 이미지를 흑백으로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 얼굴 감지
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None, 'Face not detected'  # 얼굴이 검출되지 않은 경우에도 None과 오류 메시지 반환

    # 가장 큰 얼굴 영역 선택
    (x, y, w, h) = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)[0]

    # 얼굴 이미지 추출
    face_img = img[y:y+h, x:x+w]

    # 이미지 저장 (optional)
    cv2.imwrite('uploads/face_' + os.path.basename(img_path), face_img)

    return 'uploads/face_' + os.path.basename(img_path), None  # 오류가 없을 때는 None을 반환하고 오류 메시지는 None으로 처리

# 이미지를 Base64로 인코딩하는 함수
def encode_image(image_path):
    if image_path is None:
        return None
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded_string if encoded_string else None

# 이미지 전처리 함수
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(48, 48), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # 정규화
    return img_array

# 감정 예측 함수
def predict_emotion(img_path):
    preprocessed_img = preprocess_image(img_path)
    predictions = model.predict(preprocessed_img)
    predictions_percentage = {emotion_labels[i]: round(pred * 100, 2) for i, pred in enumerate(predictions[0])}
    max_index = np.argmax(predictions[0])
    emotion = emotion_labels[max_index]
    return emotion, predictions_percentage

def generate_image(prompt, negative_prompt):
    r = requests.post(
        'https://api.kakaobrain.com/v2/inference/karlo/t2i',
        json={
            'prompt': prompt,
            'negative_prompt': negative_prompt
        },
        headers={
            'Authorization': f'KakaoAK {REST_API_KEY}',
            'Content-Type': 'application/json'
        }
    )
    r.raise_for_status()
    return r.json()

@app.route('/')
def index():
    return render_template('text.html')

@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        if 'sentence' in request.form:
            sentence = request.form['sentence']
            translator = GoogleTranslator(source='auto', target='en')
            translated_sentence = translator.translate(sentence)
            response = generate_image(translated_sentence, '')
            image_url = response.get('images')[0].get('image')
            image_data = requests.get(image_url).content
            # 이미지 파일 이름을 현재 날짜와 시간으로 설정하여 저장
            current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분")
            folder_path = os.path.join('src', 'main','resources', 'static', 'images')
            os.makedirs(folder_path, exist_ok=True)
            filename = os.path.join(folder_path, f'{current_time}.png')
            with open(filename, 'wb') as f:
                f.write(image_data)
            base64_image = base64.b64encode(image_data).decode('utf-8')

            return render_template('result_text.html', image=base64_image)
    return render_template('text.html')

@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return render_template('file.html', message='No selected file')
            try:
                filename = os.path.join('uploads', file.filename)
                file.save(filename)
                face_path, error_message = detect_face(filename)
                if error_message:
                    emotion, predictions_percentage = predict_emotion(filename)
                    original_image_encoded = encode_image(filename)
                    return render_template('result_file.html', original_image=original_image_encoded, prediction=emotion, percentages=predictions_percentage)
                else:
                    emotion, predictions_percentage = predict_emotion(face_path)
                    original_image_encoded = encode_image(filename)
                    face_image_encoded = encode_image(face_path)
                    return render_template('result_file.html', original_image=original_image_encoded, face_image=face_image_encoded, prediction=emotion, percentages=predictions_percentage)
            except Exception as e:
                return render_template('file.html', message=str(e))
    return render_template('file.html')
if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True, port=5000)