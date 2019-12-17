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
  * pip install 명령어 사용
* [dlib 설치방법](https://sulastri.tistory.com/3)
* 게임 내 랭킹 기능을 사용하고 싶다면
  * 아래의 형식에 맞는 'ranking'테이블을 생성합니다.

이름|영어|정보|수학

---|---|---|---|
나동빈|98점|87점|100점|
홍길동|97점|78점|93점|
이순신|89점|93점|97점|

|Column Name|Datatype|PK|AI|
|:---:|:---:|:---:|:---:|
|num|INT(11)|Y|Y|
|name|VARCHAR(45)|  |  |
|score|INT(11)|  |  |
  * db.py의 line3에 password를 수정합니다.
* 게임 내 랭킹 기능을 사용하기 싶지 않다면
  * 아래를 참고하고 해당 부분을 주석처리 합니다.
     * game.py의 line 20
     * username.py의 line 4
     * username.py의 line 209
     * username.py의 line 232

## 게임설명
* 게임 내의 아이템을 모두 먹고 장애물을 피하여 목표지점에 도달합니다.
* 게임 조작 방법
  * 캐릭터 이동 : 좌우 방향키
  * 캐릭터 방어막 : 아래 방향키
    * 장애물을 피할 수 있도록 도와줍니다
  * **캐릭터 점프 : 사용자의 얼굴 위로 이동**
  * **아이템 먹기 : 사용자의 입 열기**
* 랭킹은 목표지점에 도착한 시간이 **짧은** 순서로 매겨집니다.


## 참고 오픈소스
* [shape_predictor_81_face_landmarks](https://github.com/codeniko/shape_predictor_81_face_landmarks)
* [게임 내 카메라 이동](https://bitbucket.org/plaoo/pygame-side-scrolling/src/default/)