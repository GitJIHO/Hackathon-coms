from flask import Flask, request, render_template, redirect
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
from datetime import datetime
import pymysql.cursors  # PyMySQL 연결을 위한 라이브러리

# REST_API_KEY값 분리
import config

# 재귀 깊이 제한 증가 (일시적인 해결책)
sys.setrecursionlimit(10000)

app = Flask(__name__)

# 모델 로드
model = load_model('emotion_model.h5')

# 감정 레이블
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# MySQL 데이터베이스 연결 설정
db_config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'mydatabase'
}

def get_db_connection():
    return pymysql.connect(
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )

def save_image_to_db(image_name, image_data):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO images (name, data) VALUES (%s, %s)"
            cursor.execute(sql, (image_name, image_data))
        conn.commit()
    finally:
        conn.close()

def detect_face(img_path):
    img = cv2.imread(img_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None, 'Face not detected'

    (x, y, w, h) = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)[0]
    face_img = img[y:y+h, x:x+w]
    cv2.imwrite('uploads/face_' + os.path.basename(img_path), face_img)
    return 'uploads/face_' + os.path.basename(img_path), None

def encode_image(image_path):
    if image_path is None:
        return None
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded_string if encoded_string else None

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(48, 48), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

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
            'Authorization': f'KakaoAK {config.REST_API_KEY}',
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
            current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분")
            folder_path = os.path.join('src', 'main', 'resources', 'static', 'images')
            os.makedirs(folder_path, exist_ok=True)
            filename = os.path.join(folder_path, f'{current_time}.png')
            with open(filename, 'wb') as f:
                f.write(image_data)

            # 데이터베이스에 이미지 저장
            save_image_to_db(f'{current_time}.png', image_data)

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

import url8080
url = url8080.url

@app.route("/redirectToMain2")
def redirect_to_main():
    return redirect(url)

@app.route("/redirectToDiary2")
def redirect_to_diary():
    return redirect(url + "/diary")

@app.route("/redirectToAlbum2")
def redirect_to_album():
    return redirect(url + "/album")

@app.route("/redirectToBoard2")
def redirect_to_board():
    return redirect(url + "/question/list")

@app.route("/redirectToMyinfo2")
def redirect_to_myinfo():
    return redirect(url + "/myInfo")

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True, port=5000)