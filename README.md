# 200ok_backend
![imges](https://user-images.githubusercontent.com/104487608/185346903-65a8745b-da0f-4fb9-8d4f-a9603735332b.png)
# 🔮녹턴앨리 B-street 지하2층 불법 입학 센터 (200ok)
사진을 Style Transfer를 이용해 스타일을 변경하고 Deepfake로 움직임을 추가해서 움직이는 초상화를 만들어 호그와트의 학생증을 만들어주는 해리포터 컨셉의 웹사이트, 간단한 커뮤니티 기능 포함

# 🧙‍♀️Intro
* Style Transfer와 Deepfake를 이용해 사진을 움직이는 초상화로 변형
* 기숙사 배정 테스트와 Chart로 기숙사별 학생수 및 방명록 작성수 시각화
* **개발 기간**: 2022.06.27 ~ 2022.07.04
* **개발 인원(4명)**: 김동근, 노을, 이정아, 이현경
* **Team Repository** <a href="https://github.com/cmjcum/200ok_backend"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/108">블로그로 이동(☞ﾟヮﾟ)☞</a>

# 🧙‍♂️Project
### Frontend Repository
<a href="https://github.com/cmjcum/200ok_frontend"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>

### 사용 기술
* Python 3.7
* Django REST Framework 3.13

### 핵심 기능
* Style Transfer와 Deepfake를 이용한 이미지 변형
* JWT를 이용한 사용자 인증
* 라운지 페이지에서 방명록 CRUD
* Chart를 이용한 데이터 시각화

### 맡은 부분
<details>
<summary>사용자가 입력한 사진에 Style Transfer, Deepfake 적용 <a href="https://github.com/zeonga1102/200ok_backend/blob/master/user/views.py#L60">📑코드</a></summary>

사용자가 입력한 사진을 Style Transfer와 Deepfake를 이용해서 그림처럼 바꾸고 움직이게 했습니다. 바뀌는 스타일과 움직임은 랜덤합니다.<br>
시간이 오래 걸리는 작업이므로 멀티 프로세싱을 이용하여 사용자가 이미지 변환을 긴 시간 기다리지 않아도 되도록 했습니다.
</details>
<details>
<summary>기숙사 테스트 문제 조회 <a href="https://github.com/zeonga1102/200ok_backend/blob/master/dormitory/views.py#L21">📑코드</a></summary>

기숙사 배정을 위한 테스트 문제들을 조회합니다.
</details>
<details>
<summary>사용자 정보 저장 <a href="https://github.com/zeonga1102/200ok_backend/blob/master/user/views.py#L71">📑코드</a></summary>

테스트를 통한 기숙사 정보를 비롯해 사용자가 입력한 정보와 변형한 이미지 url을 저장합니다.
</details>

### ERD
![200ok](https://user-images.githubusercontent.com/104487608/186652733-dd0af8a2-605f-446f-b993-51fb96388c0a.png)

# 🛠Troubleshooting
### ImportError: cannot import name 'PILLOW_VERSION' from 'PIL'
pillow의 버전이 높아서 발생하는 에러입니다. pillow의 버전을 6.2.2로 낮춰서 해결했습니다.

# 🖋회고
이번 프로젝트는 다른게 아니라 딥러닝을 프로젝트에 적용하는 것부터가 힘들었다. DRF로 처음 프로젝트를 진행하는건 괜찮았는데 Style Transfer와 Deepfake를 어떤 식으로 써야하나 감이 잘 안 잡혔다. 그래도 무사히 적용해서 다행이었다. 지금은 사진을 변형할 때 Deepfake를 먼저 하고 Style Transfer를 뒤에 적용했는데 생각해보니 반대 순서로 하는게 실행 속도가 빨랐을 것 같다.<br>
사실 사용자들의 기숙사를 분류할 때도 머신러닝을 적용하고 싶었다. 영화 해리포터에 출연한 배우들의 얼굴로 분류 모델을 만들어서 모델을 통한 분류 결과와 테스트 결과를 적절히 섞어 사용자들의 기숙사를 배정하려 했다. 기간도 짧고 프로젝트 초반에 헤매기도 해서 이것까지 하기에는 시간이 부족했다. 이 기능까지 됐으면 더 좋았을 것 같아서 아쉽다.<br>
나 말고 다른 팀원들도 새롭게 해보는 기능이 많고 프로젝트 기간도 짧다보니 다들 고생이 많았다. 그래도 고생한만큼 특색있는 결과물을 만들 수 있었던 것 같다. 배포는 최종적으로는 실패했지만 이번 실패를 밑거름 삼아 다음에는 배포까지 마칠 수 있도록 해야겠다.<br>
[팀 회고 보러가기(☞ﾟヮﾟ)☞](https://cold-charcoal.tistory.com/116)

# ✨Credit
* Style Transfer pre-trained models <a href="https://github.com/ycjing/Neural-Style-Transfer-Papers"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* 딥페이크 코드 <a href="https://github.com/AliaksandrSiarohin/first-order-model"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
