# **<u>Pure Django To Do App</u>**

## <u>개발 기능 내용</u>

## _유저_
- [x] 회원가입
- [x] 로그인
- [x] 로그아웃
- [ ] 소셜 가입
- [ ] 소셜 로그인

## _팀_
- [x] 팀 작성
- [ ] 팀 수정(운영자만)
- [ ] 팀 삭제

## _팀 구성원_
- [x] 팀 작성시 구성원 추가
- [ ] 기존 팀에 구성원 추가
- [ ] 기존 팀에서 구성원 삭제

## _TODO_
- [ ] TODO 추가
- [ ] TODO 삭제
- [ ] TODO 관리자 설정
- [ ] TODO 관리자 변경
- [ ] TODO 상태 변경

### Docker Build Command
- docker build .

### Docker Compose Build
- docker-compose build

### Build Project
- docker-compose run app sh -c "django-admin startproject config ."

### Run Server
- docker-compose up