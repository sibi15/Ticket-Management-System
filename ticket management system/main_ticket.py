import random
import time
import string
import sys
import datetime

# INTRODUCTION:
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print('\n                                                           TICKET MANAGAMENT SYSTEM\n')
print('---------------------------------------------------------------------------------------------------------------------------------------------')

print('1. Book a ticket.')
print('2. Exit.')
ch=int(input('Please enter choice (1 or 2): '))

if ch==1:
      # function to stop the timer if the correct ticket_id is entered:
      def stop_timer():
            re_en=input('Please enter the Ticket ID to stop the timer after you have RETURNED. ')
            time.sleep(1)
            if re_en==ticket_id:
                  pass
            else:
                  print('Wrong Ticket ID inputed. Please try again.')
                  time.sleep(1)
                  stop_timer()
                  return re_en
      
      # letters and numbers list generation:
      letters=[]
      for i in range(0,26):
          letters.append(string.ascii_uppercase[i])
      numbers=[]
      for i in range(1,6):
          numbers.append(i)
      time.sleep(1)
      # providing user random ticket code:
      ticket_id='%s%s'
      l=random.choice(letters)
      m=random.choice(numbers)
      ticket_id=ticket_id%(l,m)
      print("Your ticket ID is:", ticket_id)
      print("Don't forget your ticket ID\n")
      time.sleep(1)
      
      # making the ticket_id UNIQUE by updating the null date to an actual date:
      import mysql.connector
      con=mysql.connector.connect(host='localhost', user='root', password='', database='test')
      cur=con.cursor()
      date=input('Please enter the date in the format (DD-MM-YY): ')
      query=("update random set date='{}' where ticket_id='{}'".format(date,ticket_id))
      cur.execute(query)
      con.commit()
      time.sleep(1)
      print('Date provided.\n')

      # STARTING of the timer:
      time.sleep(1)
      print("Timer will start now.")
      start=time.perf_counter()
      stop_timer()  # call function to stop timer (with recursion):
      end=time.perf_counter()
      time_period=end-start
      time_period=int(time_period//1)
      
      # to print the TIME and the COST to be payed:
      print('\nYou will be prompted to the payment details soon after the following.')

      # check if connected successfully:
      con=mysql.connector.connect(host='localhost', user='root', password='', database='test')
      if con.is_connected():
          print("\nloading.")
          time.sleep(0.5)
          print("loading..")
          time.sleep(0.5)
          print("loading...")
          time.sleep(0.5)
          
      # UPDATING the time to the SQL table:
      cur2=con.cursor()
      sql_uptime=("update random set time='{}' where ticket_id='{}'".format(time_period, ticket_id))
      cur2.execute(sql_uptime)
      con.commit()
      print('Time updated.')
      time.sleep(1)

      print('Time you have to pay for is:', str(datetime.timedelta(seconds=time_period)))
      cost=time_period*4
      print("(Calculating cost per second for now)")
      time.sleep(1)
      print("\nYour cost will be", cost, ".")

      cur3=con.cursor()
      sql_set=("update random set date='', time=''")
      cur3.execute(sql_set)
      con.commit()
      time.sleep(1)
      print('Reset successful.')
      print('Thank you. ')

# DIRECT EXIT:
elif ch==2:
      time.sleep(1)
      print('Thank you.')
      sys.exit()
