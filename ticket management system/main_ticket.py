  #giving user a random ticket:

# certain days: free tickets or reduced prices
# reduced price for more hours (cost/min)
# regular customer
# more cost on thurs and fris due to more crowd

import random
import time
import string
import sys
import datetime

# INTRODUCTION:
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('\n                                                               TICKET MANAGAMENT SYSTEM\n')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------')

time.sleep(4)

print('1. Book a ticket.')
print('2. Exit.')
time.sleep(2)
ch=int(input('Please enter choice (1 or 2): '))

if ch==1:
      
      # function to stop the timer if the correct ticket_id is entered:
      def stop_timer():
            re_en=input('Please enter the Ticket ID to stop the timer after you have RETURNED. ')
            time.sleep(2)
            if re_en==ticket_id:
                  time.sleep(2)
                  pass
            else:
                  print('Wrong Ticket ID inputed. Please try again.')
                  time.sleep(1)
                  stop_timer()    # recurssion
                  return re_en



      # letters and numbers list generation:
      letters=[]
      for i in range(0,26):
          letters.append(string.ascii_uppercase[i])


      numbers=[]
      for i in range(1,6):
          numbers.append(i)
      time.sleep(2)



      # providing user random ticket code:
      ticket_id='%s%s'
      l=random.choice(letters)
      m=random.choice(numbers)
      ticket_id=ticket_id%(l,m)
      print("Your ticket ID is:", ticket_id)
      print("Don't forget your ticket ID or we will empty your pockets and your bank account!\n")
      time.sleep(2)


      # making the ticket_id UNIQUE by updating the null date to an actual date:
      import mysql.connector
      con=mysql.connector.connect(host='localhost', user='root', password='', database='test')
      cur=con.cursor()
      date=input('Please enter the date in the format (DD-MM-YY): ')
      query=("update random set date='{}' where ticket_id='{}'".format(date,ticket_id))
      cur.execute(query)
      con.commit()
      time.sleep(2)
      print('Date provided.\n')
      # error ---> two people get same code


      # STARTING of the timer:
      time.sleep(2)
      print("Timer will start now.")
      start=time.perf_counter()

      # once user enters any key, the timer STOPS:
      time.sleep(2)
      ##print("Please press any key to stop the timer once you're done.")   
      ##now=input("")
      ##
      ##if now=="":
      ##    print("")
      ##else:
      ##    print("")

      stop_timer()  # call function to stop timer (with recursion):

      end=time.perf_counter()
      time_period=end-start
      time_period=int(time_period//1)






      # to print the TIME and the COST to be payed.

      import mysql
      import mysql.connector
      import time

      print('\nYou will be prompted to the payment details soon after the following.')

      # check if connected successfully:
      con=mysql.connector.connect(host='localhost', user='root', password='sibikarthik260104', database='test')
      if con.is_connected():
          print("\nloading.")
          time.sleep(0.5)
          print("loading..")
          time.sleep(0.5)
          print("loading...")
          time.sleep(0.5)


      #re entering code to 

      ##re_en=input("Enter ticket code:")
      ##try:
      ##    cur1=con.cursor()
      ##    sql_re=("select * from random where ticket_id = '{}'".format(re_en))
      ##    cur1.execute(sql_re)#,{'re':re_en})
      ##    #con.commit()
      ##    row=cur1.fetchall()
      ##    #print(row)
      ##    for i in row:
      ##        tuple1=i
      ##    for j in tuple1:
      ##        print(j)
      ##except Exception as err: 
      ##    print("Exception occured while fetching the records ", err)
      ##else:
      ##    print(" ")


      # UPDATING the time to the SQL table:

      cur2=con.cursor()
      sql_uptime=("update random set time='{}' where ticket_id='{}'".format(time_period, ticket_id))
      cur2.execute(sql_uptime)
      con.commit()
      time.sleep(2)
      print('Time updated.')



      time.sleep(3)
      print('Time you have to pay for is:', str(datetime.timedelta(seconds=time_period)))
      cost=time_period*4
      time.sleep(2)
      print("(Calculating cost per second for now)")
      time.sleep(2)
      print("\nYour cost will be", cost, "AED.")

      time.sleep(4)

      cur3=con.cursor()
      sql_set=("update random set date='', time=''")
      cur3.execute(sql_set)
      con.commit()
      time.sleep(1)
      print('Reset successful.')
      time.sleep(2)

      print('Thank you. ')


# DIRECT EXIT:

elif ch==2:
      time.sleep(1)
      print('Thank you.')
      sys.exit()
