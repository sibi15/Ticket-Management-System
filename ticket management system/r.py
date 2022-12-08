# giving user a random ticket:

import time
import datetime
import uuid
import string
import sys
import random

letters=[]
for i in range(0,26):
      letters.append(string.ascii_uppercase[i])
print(letters)

numbers=[]
for i in range(1,6):
      numbers.append(i)
print(numbers)




#main:

##count=0
##try: 
##      n=int(input('No. of tickets needed.: '))
##      for i in range(0,5):
##            if n<0:
##                  print('Wrong input, try again.')
##                  n=int(input('No. of tickets needed.: '))
##                  count+=1
##            else:
##                  pass
##            if count==4:
##                  print('exiting.')
##                  sys.exit()
##
##except ValueError:
##      print('Wrong input.')
##      sys.exit()
##      
                  
      
            


##for i in range(1,n+1):
##      #str1=uuid.uuid4()
##      ticket_id='%s%s'
##      for j in letters:
##            #ticket_id=ticket_id%(j)
##            for k in numbers:
##                  ticket_id=ticket_id%(j,k)
##                  #print('Ticket', i, 'is', ticket_id)
##                  print(ticket_id)
##                  #time.sleep(2)
##                  ticket_id='%s%s'
##                  #break
##            #break




ticket_id='%s%s'
l=random.choice(letters)
n=random.choice(numbers)
ticket_id=ticket_id%(l,n)
print('Your ticket ID is:',ticket_id)
print('Please remember it, to stop your timer.')

##import mysql.connector
##con=mysql.connector.connect(host='localhost', user='root', password='', database='test')
##cur=con.cursor()
##date=input('Please enter the date in the format (ddmmyy): ')
##query=("update random set date='{}' where ticket_id='{}'".format(date,ticket_id))
##cur.execute(query)
##con.commit()
##time.sleep(2)
##print('Date provided.')
# error ---> same code  

# timer starts here:

time.sleep(2)
print('The timer has started.')
start=time.perf_counter()
##time.sleep(2)
##end=time.perf_counter()
##time_period=end-start
##time_period=int(time_period//1)
##formats=str(datetime.timedelta(seconds=time_period))
##print('Time passed is', formats)            
