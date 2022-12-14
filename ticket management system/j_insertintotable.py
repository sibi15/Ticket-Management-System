# insert into table code:


# connection object creation: 
import mysql.connector
import time

con=mysql.connector.connect(host='localhost', user='root', password='sibikarthik260104', database='test')
time.sleep(2)
if con.is_connected():
      print('\nSuccessful Connection. ')

cur1=con.cursor()
queryquery=("drop table random")
cur1.execute(queryquery)
con.commit()
time.sleep(2)
print('Table dropped.')
      


# table deleted after each ticket_id append check, so create again before inserting values:
cur=con.cursor()
cur.execute("create table random(ticket_id varchar(3) primary key not null, date varchar(10), time varchar(8))")
time.sleep(2)
print('Table created successfully')

# lists for the ID:
import string

letters=[]
for i in range(0,26):
      letters.append(string.ascii_uppercase[i])
print(letters)

numbers=[]
for i in range(1,6):
      numbers.append(i)
print(numbers)



# main (run once (i) so that only once all gets appended):
ticket_id='%s%s'                           # can use f STRINGS
for j in letters:
      for k in numbers:
            ticket_id=ticket_id%(j,k)
            query=("insert into random values('{}','','')".format(ticket_id))    # command done here, as we have to replace the placeholders as it can only be replaced once.
            cur1=con.cursor()                                                      #|
            cur1.execute(query)                                                    #v
            con.commit()                                                           
            ticket_id='%s%s'                                                       # HERE
            #print(ticket_id)




time.sleep(2)
print('\nRows added successfully.')
