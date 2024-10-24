# Hackathon-coms
> # 2024 GLOW 해커톤 본선 진출작

![image](https://github.com/user-attachments/assets/ab002571-324a-4381-9cc5-8e8e9406b8a5)


<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap" rel="stylesheet">

<br/>

# 목차
1. 웹 서비스 소개 및 팀 소개
2. 웹 서비스 개발 배경
3. 주요 기능 소개
4. 부가 기능 소개
5. 기술 스택
6. 서버 환경
7. 기술 명세서
8. "dialog"만의 차별점
<br/>

# 1. 웹 서비스 소개 및 팀 소개
### ♦️ 팀명
>**Com's**
    
### ♦️ 팀원
<table>
<tbody>
    <td align="center">
        <a href="https://ifh.cc/g/QkXhsw.jpg"><img src="https://ifh.cc/g/QkXhsw.jpg" alt="이지호" border="0" width="95px;" alt=""/></a>
        <br /><sub><b>이지호 - BE</b></sub>
    </td>
    <td align="center">
        <a href="https://ifh.cc/g/NjmafX.jpg"><img src="https://ifh.cc/g/NjmafX.jpg" alt="김건" border="0" width="100px;" alt=""/></a>
        <br /><sub><b>김건 - BE</b></sub>
    </td>
    <td align="center">
        <a href="https://ibb.co/HrSPjbz"><img src="https://i.ibb.co/Jz1p9G7/Kakao-Talk-20240602-020346537.jpg" alt="김서연" border="0" width="95px;" /></a>
        <br /><sub><b>김서연 - FE</b></sub>
    </td>
    <td align="center">
        <a href="https://ifh.cc/g/KPoovL.jpg"><img src="https://ifh.cc/g/KPoovL.jpg" alt="최기영" border="0" width="110px;" alt=""/></a>
        <br /><sub><b>최기영 - FE</b></sub>
    </td>
</tbody>
</table>

### ♦️ dialog 소개
저희 서비스는 사용자의 하루를 한 줄로 작성하면<br/>
AI 기반으로 그림(또는 사진)으로 하루를 기록해줍니다.<br/><br/>
또한 사용자가 업로드하는 사진 속의 인물의 행복도를 분석하여<br/>
사용자로 하여금 웃음을 유발하도록 합니다.<br/><br/>
마지막으로 외로운 현대인들을 위해<br/>
사용자들의 취미를 공유할 수 있는 게시판을 제작하여<br/>
사용자들 간의 소통을 가능하게 하였습니다.<br/><br/>

### ♦️ dialog의 마스코트 '몬드(Mond)'
![image](https://github.com/user-attachments/assets/aee0c02f-ac78-404b-856b-318cd9266868)

<br/>
<b> 📖 다이아몬드(diamond) + 일상 기록(log) 📖 </b>
<br/>
<br/>
"다이아몬드처럼 반짝이는 당신의 하루를 특별하게 기록 해드릴게요!"
<br/>
<br/>
<br/>

# 2.웹 서비스 개발 배경
<a href="https://ibb.co/2c6JdYR"><img src="https://i.ibb.co/7rzhKNB/2024-05-31-205405.png" alt="2024-05-31-205405" border="0" width="300"></a>
<a href="https://ibb.co/s9JQ1Fw"><img src="https://i.ibb.co/B2Kj6gZ/2024-05-31-205439.png" alt="2024-05-31-205439" border="0" width="300"></a>
<br/>
<br/>
<br/>
현대인들의 우울증, 불안증상은 나날히 커져가고 있습니다. <br/>
이에 저희는 하루를 기록하여 현대인들의 정신건강에 도움이 되고자<br/>
<strong>"dialog"</strong> 웹 서비스를 개발하게 되었습니다. <br/><br/>
하루를 기록하고 본인의 감정을 들여다 보는 것은<br/>
우울증 및 불안증상과 같은 현대인의 마음의 병을 치료하는데에 큰 도움이 됩니다.<br/><br/>
뿐만 아니라 많은 사람들과의 취미 공유를 통해서도<br/>
외로움을 극복하고 마음의 병을 치유 및 예방할 수 있습니다.<br/>

<br/>
<strong>"dialog"를 통해 하루를 기록하고, 마음을 돌보는 건 어떨까요?</strong>
<br/>

<br/>
<br/>
<br/>
<br/>

# 3. 주요 기능 소개
## ✍🏻한줄한컷
![image](https://github.com/user-attachments/assets/280aac27-d4c6-43c1-a207-bd4b79617e26)

<br/>
📌 <strong>Karlog.ai</strong> 이용하여 AI 기반 그림(사진)일기 생성<br/>
<br/>
<a href="https://ibb.co/rw63knP"><img src="https://i.ibb.co/S3ncNqT/2024-05-31-214033.png" alt="2024-05-31-214033" border="0" width = "450px"></a><br/>
🔗 https://blog.kakaobrain.com/news/room/1024

<br/>
<br/>
<br/>

## ✍🏻얼굴 찌푸리지 말아요
![image](https://github.com/user-attachments/assets/0352a049-8c0a-4946-8139-8e11c979b980)

<br/>
﻿
📌 <strong>Kaggle Datasets</strong>의 28709개의 표정들을 TensorFlow를 통해 사전에 학습시켜 AI 감정 분석 기능을 설계함.<br/>
<a href="https://ibb.co/MZhw5qJ"><img src="https://i.ibb.co/S5xY7qZ/2024-05-31-214345.png" alt="2024-05-31-214345" border="0" width="450px"></a> <br/>
🔗 https://www.kaggle.com/datasets/msambare/fer2013
<br/>
<br/>
<br/>

## ✍🏻쉼터
![image](https://github.com/user-attachments/assets/90a155ca-576d-4038-88f9-fb9c5e8e3e96)
![image](https://github.com/user-attachments/assets/3ed4a2cd-8f46-49ed-8021-61dd5e888baf)

<br/>
📌 <strong>마크다운 에디터</strong>를 사용하여 다양한 표현을 이용하여 게시글 작성<br/>

🔗 https://simplemde.com/markdown-guide
<br/>
<br/>
<br/>

# 4. 부가 기능 소개
## 👥 마이페이지
![image](https://github.com/user-attachments/assets/8594298d-793d-4f15-814d-175a91ed6f70)

<br/>
📌 이메일을 이용하여 회원가입 후, 내 정보에서 본인의 이름 수정 가능.

<br/>
<br/>
<br/>

# 5. 기술 스택
### 🖥️ Front-End
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white">
### 🖥️ Back-End
<img src="https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=Spring&logoColor=white"> <img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white">  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white"> <img src="https://img.shields.io/badge/ngrok-1F1E37?style=for-the-badge&logo=ngrok&logoColor=white">

<br/>
<br/>
<br/>

# 6. 서버 환경

📌 <strong>Ngrok</strong>: 로컬 개발 환경에서 인터넷을 통해 웹 애플리케이션에 안전하게 접근할 수 있도록 해줌.<br/>
🔗 https://ngrok.com/

<br/>

<b>🌟Ngrok의 장점</b> <br/>
🔎 편리한 설치와 사용 <br/>
🔎 안전한 연결 <br/>
🔎 개발 및 테스트 용이성 <br/>
🔎 다양한 기능 <br/>

<br/>
<br/>
<br/>

# 7. 기술 명세서
![img](https://github.com/user-attachments/assets/86d82657-8813-4cb7-a3aa-92d8fd1eedd5)


<br/>
<br/>
<br/>

# 8. "dialog"만의 차별점

<br/>
📍 하루를 기록하는 작품을 생성할 때, 화풍을 지정하여 그림 혹은 사진으로 저장 가능. <br/>
📍 사진 속 인물의 행복도를 측정하여 사용자로 하여금 웃음을 유발할 수 있도록 함. <br/>
📍 취미 공유 플랫폼 기능을 추가하여 많은 사람들과 소통하는 과정에서 마음의 병을 치유할 수 있도록 함. <br/>
