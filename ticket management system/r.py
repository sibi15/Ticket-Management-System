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

ticket_id='%s%s'
l=random.choice(letters)
n=random.choice(numbers)
ticket_id=ticket_id%(l,n)
print('Your ticket ID is:',ticket_id)
print('Please remember it, to stop your timer.')

time.sleep(2)
print('The timer has started.')
start=time.perf_counter()
