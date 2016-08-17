# PythonXlsx

### 1. 구현 환경
* osX 10.11.2

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

  2. column count, name : 가져올 열의 갯수와 이름, * 의 경우 count를 1 name을 * 로 입력 ( 조회하는 table이 1개인 경우만 사용가능 )

  3. option : query에서 where 절 부터 끝까지 입력 ( ex) where TimeStamp <= DATE_FORMAT('2016-04-28 17:30:00))

  4. chart column count, column number : 차트에 이용될 열의 갯수, 열의 번호(1 = A, 2 = B)

### 4. 주의사항
 * 데이터 양이 많을 경우 시간이 다소 걸림 complete message가 출력되야 완료된 것
 
 * column, table 은 갯수와 이름만 입력
 
 * option 입력시 where 부터 입력해야 함
 
 * query 구문이 이상하거나 존재 하지않는 column, table 입력시 예외 처리되어 다시 입력 받지만 가급적 확인 하고 입력
 
 * Test Query : SELECT Startup, TimeStamp from T_PCS_UNIT WHERE TimeStamp <= DATE_FORMAT('2016-04-28 03:30:00','%Y-%m-%d %H:%i:%s')
 
### 5. 입력 예시
 
 ```
Input Number Of Tables
1
Input Table Name
T_PCS_UNIT

Input Column Count
3

Input Column Name
Startup
Reconn_Int
TimeStamp

Startup, Reconn_Int, TimeStamp 

Input Option( ex) where ~~ )
WHERE TimeStamp <= DATE_FORMAT('2016-04-28 03:30:00','%Y-%m-%d %H:%i:%s')
 SELECT Startup, Reconn_Int, TimeStamp FROM T_PCS_UNIT WHERE TimeStamp <= DATE_FORMAT('2016-04-28 03:30:00','%Y-%m-%d %H:%i:%s')
 

Input column Count will be used chart (Max : 3)
2

Startup A : 1
Reconn_Int B : 2
TimeStamp C : 3

Column 1
1
Column 2
2

Export Xlsx Complete!

 ```


Q) ghjf1278@naver.com 



