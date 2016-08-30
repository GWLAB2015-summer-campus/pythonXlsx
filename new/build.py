#!/usr/bin/python
import pymysql.cursors
import xlsxwriter
import datetime
import getpass
import hashlib
import json
import os

def dbConnect():
 # DB Config Parsing json
 file = open("./config.json", 'r')
 jsonData = json.loads(file.read())

 DATABASE_HOST = jsonData['DATABASE_HOST']
 DATABASE_USER = jsonData['DATABASE_USER']
 DATABASE_NAME = jsonData['DATABASE_NAME']
 DATABASE_PASSWD = jsonData['DATABASE_PASSWD']

 print "### DataBase Connection\n"
 if DATABASE_HOST == "":
  print "Input DB Config\n"
  os.system("python config.py")

 print "Host is " + DATABASE_HOST

 passwd = getpass.getpass()
 SHA = hashlib.sha512()
 SHA.update(passwd)
 sha512 = SHA.hexdigest()
 if DATABASE_PASSWD == sha512.upper():
  # DB Connect
  global connection  ###

  connection = pymysql.connect(host=DATABASE_HOST, user=DATABASE_USER,
                               password=passwd, db=DATABASE_NAME, cursorclass=pymysql.cursors.DictCursor)
 else:
  print "Connection failed"
  exit()


def describeTable():
 while True:
  print "Input Number Of Tables"
  try:
   tableCount = int(raw_input())
  except ValueError:
   print "Table Count must be Integer"
  else :
   break;

 tables = dict()
 idx = 0

 print "Input Table Name"
 while True:
  tableName=raw_input()
  try:
   with connection.cursor() as cursor:
    sql = "DESCRIBE "+ tableName
    cursor.execute(sql)
    result = cursor.fetchall()

    field = "{0:30}"
    etc = "{0:20}"
    print "-" * 143
    print '| ' + field.format("Field") + '| ' + etc.format("Type") + '| ' + etc.format("Null") + '| ' + etc.format(
     "Key") + '| ' + etc.format("Default") + '| ' + etc.format("Extra") + '| '
    print "-" * 143
    for rows in result:
     print '| ' + field.format(rows['Field']) + '| ' + etc.format(rows['Type']) + '| ' + etc.format(
      rows['Null']) + '| ' + etc.format(rows['Key']) + '| ' + etc.format(rows['Default']) + '| ' + etc.format(
      rows['Extra']) + '| '
    print "-" * 143
    tables[idx] = tableName

    if idx == (tableCount - 1):
     break

    idx += 1
  except pymysql.err.DatabaseError:
   print "Check the tableName"


 return tables


def setSqlQuery(tables):
 # Query Input
 global cols ###
 cols = dict()

 print "### Query String(SELECT ('column1, cloumn2') + FROM ('talbe1, table2') + OPTION(WHERE ~~ ))"


 global tableStr ###
 tableCount = len(tables)
 global tableStr
 tableStr = ""

 for idx in range(0, int(tableCount), 1):
  if (idx != (int)(tableCount) - 1):
   tableStr += tables[idx] + ', '
  else:
   tableStr += tables[idx] + ' '
 print tableStr

 while True:
  try:
   print "Input Column Count"
   global colCount ###
   colCount = int(raw_input())
  except ValueError:
   print "Column Count must be Integer"
  else:
   break;

 global colStr ###
 colStr = ""
 print "Input Column Name"
 for idx in range(0, int(colCount), 1):
  cols[idx] = raw_input()

### dirty
  if (cols[idx] == '*') :
   for i in range(0, int(tableCount), 1):
    try:
     with connection.cursor() as cursor:
      sql = "DESCRIBE " + tables[i]
      cursor.execute(sql)
      result = cursor.fetchall()
      colCount = len(result)
      for j in range(0,int(colCount),1):
       cols[j] = result[j]['Field']
       if (j != int(colCount) -1):
        colStr += cols[j] + ', '
       else:
        colStr += cols[j] + ' '
    except pymysql.err.DatabaseError ,e :
     print e
   break
### dirty

  if (idx != (int)(colCount) - 1):
   colStr += cols[idx] + ', '
  else:
   colStr += cols[idx] + ' '

 print colStr


 print "Input Option( ex) where ~~ )"
 global optStr ###
 optStr = raw_input()



dbConnect()

print "### DataBase export to xlsx ###"

tables = describeTable()
setSqlQuery(tables) ### set Query


workbook = list()
worksheet = list()
res = list()
row = list()

while True:
 cnt = 0
 try:
  with connection.cursor() as cursor:

   sql = "SELECT "+ colStr +"FROM " + tableStr + optStr
   cursor.execute(sql)
   result = cursor.fetchall()

   print "Data Length : " + str(len(result))
   print "Input threshold"
   threshold = int(raw_input())

   length = (len(result) / threshold) + 2

   for idx in range(1, length ,1) :
    if idx != (length - 1) :
     res.append(result[(idx-1) * threshold :idx * threshold])
    else :
     res.append(result[(idx-1) * threshold : ])

    # Create WorkSheet
    sheetName = tableStr + "dump"+str(idx)+".xlsx"

    workbook.append(xlsxwriter.Workbook(sheetName))
    worksheet.append(workbook[idx-1].add_worksheet())

    row.append(1)
    date_format = workbook[idx-1].add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})

    # Sheet Header
    for col in range(0, int(colCount), 1):
      worksheet[idx-1].write(0, col, cols[col]);
      worksheet[idx-1].set_column(0,col,20)

    mergeCol = 2
    currentCol = 2
    pretm = None

    # chart data
    for rows in res[idx-1]:
     for col in range(0, int(colCount), 1):

      if (type(rows[cols[col]]) == type(datetime.datetime.now())):  ## how to compare datetime type..
       # time data

       worksheet[idx-1].write(row[idx-1], col,rows[cols[col]],date_format)

       # merge cell

      else:
       worksheet[idx-1].write(row[idx-1], col,rows[cols[col]])

     row[idx-1] += 1

    #worksheet[idx - 1].merge_range('AA' + str(currentCol) + ':AA' + str(row[idx - 1]), tm, date_format)


   ##Chart Input

   print "Will use chart [y/n]"
   yn = raw_input();
   if yn == 'y' :
    print "Input column Count will be used chart (Max : " + str(colCount) + ")"
    charCount = raw_input()

    for col in range(0, int(colCount), 1):
     if col < 26 :
      print cols[col] + " " + chr(65 + col) + " : " +str(col + 1)
     else:
      print cols[col] + " " + chr(65) + chr(65 + col-26) + " : " +str(col + 1)

    chart = list()
    for j in range(1, length, 1):
     chart.append(workbook[j-1].add_chart({'type': 'line'}))

    for i in range(0,int(charCount),1):
     print "Column " + str(i+1)
     colNum = int(raw_input())
     colName = chr(colNum + 64)


     ## Draw Chart
     for j in range(1, length, 1):
      sheetStr = "=Sheet1!$" + colName + "$2:$" + colName + "$" + str(row[j-1])
      #categoryStr = "=Sheet1!$" + "AA" + "$2:$" + "AA" + "$" + str(row[j-1])
      print row[j-1]

      chart[j-1].add_series({
       #'categories': categoryStr,
       'values': sheetStr,
       'name' : str(cols[colNum - 1]),

      })
      chart[j-1].set_x_axis({
       'interval_unit':9
      })

     for j in range(1, length, 1):
      worksheet[j - 1].insert_chart(0, col, chart[j-1])



 except pymysql.err.DatabaseError, e:
  print sql
  print "Check the Query, Table Structure"
  tables = describeTable()
  setSqlQuery(tables)
 else:
  for j in range(1, length, 1):
   workbook[j-1].close()
  connection.close()

  print "Export Xlsx Complete!"
  break;

#_check_mysql_exception
