# 200ok_backend
![imges](https://user-images.githubusercontent.com/104487608/185346903-65a8745b-da0f-4fb9-8d4f-a9603735332b.png)
# 녹턴앨리 B-street 지하2층 불법 입학 센터 (200ok)
해리포터 컨셉, 사람 사진을 초상화처럼 스타일을 변경하고 움직임을 추가해서 움직이는 초상화를 만들고 머신러닝을 통해 기숙사를 분류해주는 웹사이트
***
<br><br/>


## 1. 개발 기간, 참여 인원
* 개발기간: 2022.06.28 - 2022.07.05
* **Team** <a href="https://github.com/cmjcum"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
김동근 <a href="https://github.com/yinmsk"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
노을 <a href="https://github.com/minkkky"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이정아 <a href="https://github.com/zeonga1102"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이현경 <a href="https://github.com/LULULALA2"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/108">블로그로 이동(☞ﾟヮﾟ)☞</a>
***
<br><br/>


## 2. 사용 기술(버전 적기)
* python
* Django
* DRF
* deepfake
* style transfer
* S3
 
<br><br/>


## 3. ERD 설계
![200ok](https://user-images.githubusercontent.com/104487608/186652733-dd0af8a2-605f-446f-b993-51fb96388c0a.png)
<br><br/>


## 4. 핵심 기능
이 프로젝트의 핵심 기능은 딥페이크를 이용해 사진을 움직이는 초상화로 만드는 것 입니다.
* JWT를 이용한 사용자 인증
* 이미지를 style transfer와 딥페이크를 이용해서 움직이는 그림처럼 변형
* 방명록 작성 및 삭제
* 시간이 오래 걸리는 작업을 멀티 프로세싱을 이용하여 처리
* S3를 이용한 파일 처리
* 차트를 이용해서 데이터를 시각적으로 표현
* 여러 css 애니메이션 효과
<details>
  <summary>기능 자세히 알아보기</summary>
  <div markdown="1">
 
## 기능 소개
* simplejwt 를 이용한 회원 가입 기능
   * [티스토리 참조](https://ddongkim.tistory.com/73)
* 배포 [코드 확인](https://github.com/yinmsk/WM_back/blob/739a549417f4d2bfa0fa7d6eea1c42a45d89631b/myroom/views.py#L42-L44)
   * 기능 설명
    
  </div>
</details>
<br><br/>


## 5. 트러블 슈팅
<details>
  <summary>cors</summary>
  <div markdown="1">
 
* 프론트의 주소와 백엔드의 주소가 달라 cors 에러가 발생했다
* 공식 문서를 참조해서 해결 할 수 있었는데 문서 설명에 따라 settings.py 의 INSTALLED_APPS, MIDDLEWARE,  CORS_ALLOWED_ORGINS 설정을 통해 해결 할 수 있었다.
   [티스토리 참조](https://ddongkim.tistory.com/85)
  </div>
</details>

<details>
  <summary>트러블 슈팅 2</summary>
  <div markdown="1">
 
* 여기
  </div>
</details>
<br><br/>

## 6. 회고 느낀점
> 프로젝트 개발 회고 (https://github.com/yinmsk/portfolio)
