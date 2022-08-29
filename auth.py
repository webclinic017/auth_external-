# this not working code 
# don't use !!!


#!/usr/bin/env python3

import asyncio
from japronto import Application
from json import JSONDecodeError

import sys
import logging
import imaplib
import smtplib

logger = logging.getLogger('myapp')
hndlr = logging.FileHandler('/auth.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hndlr.setFormatter(formatter)
logger.addHandler(hndlr)
logger.setLevel(logging.INFO)

def auth_smtp(email, password):
    server = smtplib.SMTP("smtp.server.com", 587)
    # server.set_debuglevel(1) # consol
    server.ehlo()
    server.starttls()

    try:
      test_smtp = server.login(email, password)
    except:
      print('Error Logon')
      return "no"

    if test_smtp[0] == 235:
      print("True")
      return "true auth"
    else:
      print("no")
      return "no auth"
    server.quit()
    return

def auth(username, password):
    print(username, password)
    if username == "test_user":
       print('Name - OK')
       if password == "test_pass":
          print('Password - OK')
          return "true test_user"
    else:
         print(auth_smtp(username, password))

    return "no test_user"


async def reading(request):
    try:
        json = request.json   # syntax curl -X POST -H "Content-Type: application/json" -d '{"password": "testP@ss", "username": "linuxize@example.com"}' wauth.mci.cloud:8081
        if json['username'] and json['password']:
            return request.Response(text=auth(json['username'], json['password']))
    except Exception:
        pass
    return request.Response(text="{0.text}".format(request))
app = Application()

r = app.router
r.add_route('/', reading)

app.run()
