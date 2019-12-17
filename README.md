# face landmark를 활용한 platformer 게임
> platformer game using face landmarks

## 2019-2-OSSP1-DINO-4
##### 2017113504 강영은
##### 2017113508 양진나

## 개발환경
* Python 3.7.0
* MySQL 8.0

## 실행방법
* 게임 실행에 필요한 module을 설치합니다.
* [dlib 설치방법](https://sulastri.tistory.com/3)
* 

## 게임설명
* 게임 내의 아이템을 모두 먹고 장애물을 피하여 목표지점에 도달합니다
* 게임 조작 방법
  * 캐릭터 이동 : 좌우 방향키
  * 캐릭터 방어막 : 아래 방향키
    - 장애물을 피할 수 있도록 도와줍니다
  * **캐릭터 점프 : 사용자의 얼굴 위로 이동**
  * **아이템 먹기 : 사용자의 입 열기**


## 참고 오픈소스
* [shape_predictor_81_face_landmarks](https://github.com/codeniko/shape_predictor_81_face_landmarks)
* [게임 내 카메라 이동](https://bitbucket.org/plaoo/pygame-side-scrolling/src/default/)