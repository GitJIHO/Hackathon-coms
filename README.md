# Hackathon-coms

<!--대표 화면 사진 넣겠습니다-->
<a href="https://ibb.co/prCfMvc"><img src="https://i.ibb.co/VpXgzWR/Kakao-Talk-20240602-012026461.png" alt="Kakao-Talk-20240602-012026461" border="0"></a>


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
        <img src="https://i.ibb.co/F81syB1/2024-06-02-021553.png" width="100px;" alt=""/>
        <br /><sub><b>이지호</b></sub>
    </td>
    <td align="center">
        <img src="https://i.ibb.co/cyFbxf6/Kakao-Talk-20240602-020747331.jpg" alt="Kakao-Talk-20240602-020747331" width="100px;" alt=""/>
        <br /><sub><b>김건</b></sub>
    </td>
    <td align="center">
        <img src="https://i.ibb.co/72dFvpV/Kakao-Talk-20240602-020346537.jpg" alt="Kakao-Talk-20240602-020346537" alt="Kakao-Talk-20240602-020346537" width="100px;" alt=""/>
        <br /><sub><b>김서연</b></sub>
    </td>
    <td align="center">
        <img src="https://i.ibb.co/wg2jNb6/Kakao-Talk-20240602-020833222.jpg" alt="Kakao-Talk-20240602-020833222" width="100px;" alt=""/>
        <br /><sub><b>최기영</b></sub>
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
<a href="https://imgbb.com/"><img src="https://i.ibb.co/ccJMVb8/Kakao-Talk-20240601-215513941.png" alt="Kakao-Talk-20240601-215513941" border="0" width = "300px"></a>
<br/>
<br/>
<b> ♦️ 다이아몬드(diamond) + 일상 기록(log) 📖 </b>
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
<br/>
<br/>
<br/>

# 3. 주요 기능 소개
## ✍🏻한줄한컷
<a href="https://ibb.co/YNyJKKL"><img src="https://i.ibb.co/0nF1WWG/2024-06-02-035414.png" alt="2024-06-02-035414" border="0"></a>

<br/>
📌 <strong>Karlog.ai</strong> 이용하여 AI 기반 그림(사진)일기 생성<br/>
🔗 https://blog.kakaobrain.com/news/room/1024
<br/>
<br/>
<br/>

## ✍🏻얼굴 찌푸리지 말아요
<a href="https://ibb.co/myb8hwT"><img src="https://i.ibb.co/94ctyLg/2024-06-02-043400.png" alt="2024-06-02-043400" border="0"></a>

<br/>
📌 <strong>tensorflow</strong>이용하여 업로드한 사진 속 인물의 행복도 측정<br/>
🔗 https://www.kaggle.com/datasets/msambare/fer2013
<br/>
<br/>
<br/>

## ✍🏻쉼터
<a href="https://ibb.co/MDJzHP0"><img src="https://i.ibb.co/FbdQ18T/2024-06-02-043026.png" alt="2024-06-02-043026" border="0"></a>

<br/>
📌 <strong>마크다운 에디터</strong>를 사용하여 다양한 표현을 이용하여 게시글 작성<br/>
<br/>
<br/>
<br/>

# 4. 부가 기능 소개
## 👥 마이페이지
<a href="https://ibb.co/Wn9jd6g"><img src="https://i.ibb.co/BLDF7tq/2024-06-02-040629.png" alt="2024-06-02-040629" border="0"></a>

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
<a href="https://ibb.co/PY1KyMD"><img src="https://i.ibb.co/W3BZX0V/image.png" alt="image" border="0"></a>

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
<span><img src="https://i.ibb.co/3F7LcnF/s-00001.jpg" alt="s-00001" border="0"></span>

<br/>
<br/>
<br/>

# 8. "dialog"만의 차별점

<br/>
📍 하루를 기록하는 작품을 생성할 때, 화풍을 지정하여 그림 혹은 사진으로 저장 가능. <br/>
📍 사진 속 인물의 행복도를 측정하여 사용자로 하여금 웃음을 유발할 수 있도록 함. <br/>
📍 취미 공유 플랫폼 기능을 추가하여 많은 사람들과 소통하는 과정에서 마음의 병을 치유할 수 있도록 함. <br/>
