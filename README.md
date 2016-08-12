# PythonXlsx

### 1. 구현 환경
* os X 10.11.2

* python 2.7.10

* python pymysql, xlsxwriter 모듈 필요(pip install pymysql, xlsxwriter)

### 2. 파일 설명
* config.json : db접속 config를 저장하는 파일

* config.py : config.json을 변경하는 스크립트

* build.py : sql query입력을 통해 나오는 data를 xlsx파일로 export하는 스크립트

* data.xlsx : 변환된 xlsx파일

### 3. 사용법 및 명령어

* python config.py -> db config 입력

* python build.py -> sql query 입력

  1. table count, name : 검색할 테이블의 갯수와 이름 (ex) from 'T_PCS_UNIT')

  2. column count, name : 가져올 열의 갯수와 이름, * 의 경우 count를 1 name을 * 로 입력 ( ex) select 'TimeStamp')

  3. option : query에서 where 절 부터 끝까지 입력 ( ex) where TimeStamp <= DATE_FORMAT('2016-04-27 03:30:00))

### 4. 주의사항
 * 데이터 양이 많을 경우 시간이 다소 걸림 complete message가 출력되야 완료된 것
 
 * column, table 은 갯수와 이름만 입력
 
 * option 입력시 where 부터 입력해야 함
 
 * query 구문이 이상하거나 존재 하지않는 column, table 입력시 예외 처리되어 다시 입력 받지만 가급적 확인 하고 입력
 
 * Test Query : SELECT Startup, TimeStamp from T_PCS_UNIT WHERE TimeStamp <= DATE_FORMAT('2016-04-27 03:30:00','%Y-%m-%d %H:%i:%s')


Q) ghjf1278@naver.com 



