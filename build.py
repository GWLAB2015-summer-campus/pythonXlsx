#!/usr/bin/python
import pymysql.cursors
import xlsxwriter
import datetime
import json

def setSqlQuery():
 # Query Input
 global cols
 cols = dict()
 global tables
 tables = dict()

 print "### Query String(SELECT ('column1, cloumn2') + FROM ('talbe1, table2') + OPTION(WHERE ~~ ))\n"

 while True:
  try:
   print "Input Table Count : "
   tableCount = int(raw_input())
  except ValueError:
   print "Table Count must be Integer"
  else:
   break;

 global tableStr
 tableStr= " "
 print "Input Table name"
 for idx in range(0, int(tableCount), 1):
  tables[idx] = raw_input()
  if (idx != (int)(tableCount) - 1):
   tableStr += tables[idx] + ', '
  else:
   tableStr += tables[idx] + ' '
 print tableStr

 while True:
  try:
   print "Input Column Count : "
   global colCount
   colCount = int(raw_input())
  except ValueError:
   print "Column Count must be Integer"
  else:
   break;

 global colStr
 colStr = " "
 print "Input Colunm Name"
 for idx in range(0, int(colCount), 1):
  cols[idx] = raw_input()
  if (idx != (int)(colCount) - 1):
   colStr += cols[idx] + ', '
  else:
   colStr += cols[idx] + ' '
 print colStr

 print "Input Option( ex) where ~~ )"
 global optStr
 optStr = raw_input()


#DB Config Parsing json
file = open("./config.json",'r')
jsonData = json.loads(file.read())

DATABASE_HOST = jsonData['DATABASE_HOST']
DATABASE_USER = jsonData['DATABASE_USER']
DATABASE_NAME = jsonData['DATABASE_NAME']
DATABASE_PASSWD = jsonData['DATABASE_PASSWD']

#DB Connect
connection=pymysql.connect(host=DATABASE_HOST,user=DATABASE_USER,
 password=DATABASE_PASSWD, db=DATABASE_NAME, cursorclass=pymysql.cursors.DictCursor)

print "### DataBase export to xlsx ###\n\n"
setSqlQuery()


while True:
 try:
  with connection.cursor() as cursor:
   sql = "SELECT "+ colStr +"FROM " + tableStr + optStr
   cursor.execute(sql)
   result = cursor.fetchall()

   # Create WorkSheet
   workbook = xlsxwriter.Workbook('data.xlsx')
   worksheet = workbook.add_worksheet()

   row = 1
   date_format = workbook.add_format()
   date_format.set_num_format('dd/mm/yyyy / hh:mm:ss')

   # Sheet Header
   for col in range(0, int(colCount), 1):
     worksheet.write(0, col, cols[col]);
     worksheet.set_column(0,col,20)

   #value = list()
   for rows in result:

    for col in range(0, int(colCount), 1):
     if (type(rows[cols[col]]) == type(datetime.datetime.now())):  ## how to compare datetime type..

      worksheet.write(row, col, rows[cols[col]], date_format)
     else:
      worksheet.write(row, col, rows[cols[col]])
    row += 1
 except pymysql.err.DatabaseError, e:
  print "Check the Query, Table Structure"
  setSqlQuery()
 else:
   workbook.close()
   connection.close()

   print "Export Xlsx Complete!"
   break;

#_check_mysql_exception