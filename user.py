import requests
import os
import sys
import time
import json
import string, random, os
from bs4 import BeautifulSoup
 

def Tikuser():
  tiq = requests.Session()
  os.system('clear')
  allti = 0
  tiktoklogo = """
\033[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
\033[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
\033[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
\033[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
\033[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
\033[1;97m           ||                                                                  
\033[1;97m           |' 

\033[1;97mMy Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMy Chanell : \033[1;97m@A7AeMARG
    """                   
  print(tiktoklogo)
  print(" ")
  print("\u001b[37;1mRead User.txt List......\u001b[0m")
  time.sleep(2)
  tiuserfile = open('user.txt', 'r').readlines()
  for line in tiuserfile:
    tw = line.strip()
    allti += 1
  oi = 0
  bi = 0
  ei = 0
  print("\u001b[37;1mUser : "+str(allti))
  print("Check All User.......")
  time.sleep(2)
  print(" ")
  print("\u001b[37;1mCheck Stared.....")
  print("======================")
  print(" \u001b[0m")
  try:
    os.mkdir('ti_user')
  except:
    pass
  oktik = 0
  badtik = 0
  errtik = 0
  head = {
  'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1'
  }
  for sur in tiuserfile:
    tim = sur.strip()
    curl = 'https://www.tiktok.com/@'+tim
    tq = tiq.get(curl, headers=head)
    soup = BeautifulSoup(tq.text, 'html.parser')
    results = soup.find('title')
    text = results.text
    stats = len(text)
    if stats==0:
      oktik += 1
      print("\u001b[32;1msuccessfull \u001b[37;1m "+tim+" ✅\u001b[1;92m")
      rk = open('ti_user/ok_tik.txt', 'a')
      rk.write(tim+"\n")
      rk.close()
    elif stats>0:
      badtik += 1
      print ("\u001b[37;1mcheck-point \u001b[37;1m "+tim+" ❌\u001b[0m")
      pa = open('ti_user/bad_tik.txt', 'a')
      pa.write(tim+"\n")
      pa.close()
    else:
      errtik += 1                             
      print("\u001b[36;1mcheck-point \u001b[37;1m "+tim+" ⛔\u001b[0m")
      ep = open('ti_user/err_tik.txt', 'a')
      ep.write(tim+"\n")
      ep.close()
    time.sleep(2)
  print("\u001b[37;1mAll User Checked......")
  print("All User have been saved in ti_user folder")
  print(" \u001b[0m")
  time.sleep(2)
  print("\u001b[32;1mOK => \u001b[37;1m"+str(oktik))
  print("\u001b[31;1mCP => \u001b[37;1m"+str(badtik))
  print("\u001b[33;1mERORR => \u001b[37;1m"+str(errtik))
  print(" ")
  input("\u001b[37;1m[ENTER FOR BACK]\u001b[0m")
  menu()

def twitteruser():
  teq = requests.Session()
  os.system('clear')
  alltw = 0
  usertewtlogo = """
\033[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
\033[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
\033[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
\033[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
\033[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
\033[1;97m           ||                                                                  
\033[1;97m           |' 

\033[1;97mMy Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMy Chanell : \033[1;97m@A7AeMARG
    """                   
  print(usertewtlogo)
  print(" ")
  print("\u001b[37;1mRead User.txt List......\u001b[0m")
  time.sleep(2)
  twuserfile = open('user.txt', 'r').readlines()
  for line in twuserfile:
    tw = line.strip()
    alltw += 1
  ou = 0
  bu = 0
  eu = 0
  print("\u001b[37;1mUser : "+str(alltw))
  print("Check All User.......")
  time.sleep(2)
  print(" ")
  print("Check Stared.....")
  print("======================")
  print("\u001b[0m ")
  try:
    os.mkdir('tw_user')
  except:
    pass
  for sur in twuserfile:
    thm = sur.strip()
    xurl = 'https://mobile.twitter.com/'+thm
    pew = teq.get(xurl)
    chktw = pew.status_code
    if chktw==200:
      print("\u001b[37;1mcheck-point \u001b[37;1m"+thm+" ❌")
      bu += 1
      ta = open('tw_user/bad_tw.txt', 'a')
      ta.write(thm+"\n")
      ta.close()
    elif chktw==404:
      print("\u001b[32;1msuccessfull \u001b[37;1m "+thm+" ✅")
      ou += 1
      lt = open('tw_user/ok_tw.txt', 'a')
      lt.write(thm+"\n")
      lt.close()
    else:
      print("\u001b[33;1mcheck-point \u001b[37;1m"+thm+" ⛔")
      eu += 1
      era = open('tw_user/err_tw.txt', 'a')
      era.write(thm+"\n")
      era.close()
    time.sleep(4)
  print("\u001b[37;1mAll User Checked......")
  print("All User have been saved in tw_user folder")
  print("\u001b[0m ")
  time.sleep(2)
  print("\u001b[32;1mOK => \u001b[37;1m"+str(ou))
  print("\u001b[31;1mBAD => \u001b[37;1m"+str(bu))
  print("\u001b[33;1mERR => \u001b[37;1m"+str(eu))
  print("\u001b[0m ")
  input("\u001b[37;1m[ENTER FOR BACK]\u001b[0m")
  menu()
def facebookuser():
  feq = requests.Session()
  os.system('clear')
  allfb = 0
  userfblogo = """
\033[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
\033[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
\033[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
\033[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
\033[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
\033[1;97m           ||                                                                  
\033[1;97m           |' 

\033[1;97mMy Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMy Chanell : \033[1;97m@A7AeMARG
    """                   
  print(userfblogo)
  print("  \u001b[37;1m")
  print("Read User.txt List......")
  time.sleep(2)
  fbuserfile = open('user.txt', 'r').readlines()
  for line in fbuserfile:
    iu = line.strip()
    allfb += 1
  okuser = 0
  baduser = 0
  errouser = 0
  print("User : "+str(allfb))
  print("Check All User.......")
  time.sleep(2)
  print(" ")
  print("Check Stared.....")
  print("======================")
  print("  \u001b[0m ")
  try:
    os.mkdir('fb_user')
  except:
    pass
  for usr in fbuserfile:
    fbuser = usr.strip()
    link = 'https://m.facebook.com/'+fbuser
    cfk = feq.get(link)
    statefb = cfk.status_code
    if statefb==200:
      print("\u001b[37;1mcheck-point \u001b[37;1m  "+fbuser+" ❌")
      baduser += 1
      bf = open('fb_user/bad_fb.txt', 'a')
      bf.write(fbuser+"\n")
      bf.close()
    elif statefb==404:
      print("\u001b[32;1msuccessfull \u001b[37;1m "+fbuser+" ✅")
      okuser += 1
      of = open('fb_user/ok_fb.txt', 'a')
      of.write(fbuser+"\n")
      of.close()
    else:
      print("\u001b[33;1mcheck-point \u001b[37;1m "+fbuser+" ⛔")
      errouser += 1
      ef = open('fb_user/bad_fb.txt', 'a')
      ef.write(fbuser+"\n")
      ef.close()
    time.sleep(4)
  print(" ")
  print("All User Checked......")
  print("All User save in fb_user folder........")
  time.sleep(2)
  print("\u001b[32;1mOK : \u001b[37;1m "+str(okuser))
  print("\u001b[31;1mBAD :\u001b[37;1m  "+str(baduser))
  print("\u001b[33;1mERR : \u001b[37;1m "+str(errouser))
  input("\u001b[37;1m[ ENTER TO BACK ]\u001b[0m")
  menu()
def intsauser(): 
  req = requests.Session()
  os.system('clear')
  alluser = 0
  userinstalogo = """
\033[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
\033[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
\033[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
\033[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
\033[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
\033[1;97m           ||                                                                  
\033[1;97m           |' 

\033[1;97mMy Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMy Chanell : \033[1;97m@A7AeMARG
    """                   
  print(userinstalogo)
  print("\u001b[37;1m ")
  print("Read User.txt file.....")
  time.sleep(2)
  instauserfile = open('user.txt', 'r').readlines()
  for line in instauserfile:
    ui = line.strip()
    alluser += 1
  print("User : "+str(alluser))
  print("Check All User.......")
  time.sleep(2)
  print(" ")
  print("Check Stared.....")
  print("======================\u001b[0m")
  head = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'content-length':'270',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'ig_cb=1; ig_did=BF4465A9-017D-4668-B5C3-EBD3DA65B2A6; csrftoken=b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC; rur=ASH; mid=XzHZAQALAAEagshAZoRCgkUeXmJP',
    'origin':'https://www.instagram.com',
    'referer':'https://www.instagram.com/',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'x-csrftoken':'b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'a9aec8fa634f',
    'x-requested-with':'XMLHttpRequest'
  }
  okuser = 0
  baduser = 0
  erruser = 0
  url = "https://www.instagram.com/accounts/login/ajax/"
  try:
    os.mkdir('user_insta')
  except:
    pass
  for lines in instauserfile:
    uin = lines.strip()
    payload = {                         
    'username' : uin,
    'enc_password':'Admin123123',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
    }
    http = req.post(url, data=payload, headers=head).text
    if '"user": true' in http:
      print("\u001b[37;1mcheck-point \u001b[37;1m "+uin+" ❌")
      baduser += 1
      bi = open('user_insta/bad_user.txt', 'a')
      bi.write(uin+"\n")
      bi.close()
    elif '"user": false' in http:
      print("\u001b[32;1msuccessfull \u001b[37;1m "+uin+" ✅")
      okuser += 1
      oi = open('user_insta/ok_user.txt', 'a')
      oi.write(uin+"\n")
      oi.close()
    else:
      print("\u001b[33;1mcheck-point \u001b[37;1m "+uin+" ⛔")
      erruser += 1
      ei = open('user_insta/err_user.txt', 'a')
      ei.write(uin+"\n")
      ei.close()
    time.sleep(4)
  print("\u001b[37;1mAll User Checked......")
  print("All User have been saved in user_insta folder")
  print(" ")
  time.sleep(2)
  print("\u001b[32;1mOK => \u001b[37;1m "+str(okuser))
  print("\u001b[31;1mBAD => \u001b[37;1m "+str(baduser))
  print("\u001b[33;1mERR => \u001b[37;1m "+str(erruser))
  print(" ")
  input("\u001b[37;1m[ENTER FOR BACK]\u001b[0m")
  menu()

def mk():
  os.system("clear")
  mkuserlogo = """
\033[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
\033[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
\033[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
\033[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
\033[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
\033[1;97m           ||                                                                  
\033[1;97m           |' 

\033[1;97mMe Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMe Chanell     : \033[1;97m@A7AeMARG
    """                   
  os.system('rm -rif user.txt')
  print(mkuserlogo)
  text = string.ascii_letters + string.digits
  length = int(input('USER CHAN PETE BET : '))
  count = int(input('CHAN USER DRWST KAT : '))
  with open('user.txt', 'a+') as file:
      for x in range(count):
          word = ''.join(random.choice(text) for x in range(length))
          if x == range(count)[-1]:
              file.write(word)
              
          else:
              file.write(word+"\n")
  time.sleep(3)
  print("ALL USER SAVED IN USER.TXT.....")
  time.sleep(3)
  os.system('clear')
  menu()

def menu():
  os.system('clear')
  menulogo = """
\033[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
\033[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
\033[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
\033[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
\033[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
\033[1;97m           ||                                                                  
\033[1;97m           |' 

\033[1;97mMy Telegram : \033[1;97m@A7Ae_MARG

\033[1;97mMy Chanell : \033[1;97m@A7AeMARG
    """                   
  
  print(menulogo)
  print(" \u001b[37;1m")
  print("[ 1 : Username Checker ]")
  print("[ 2 : Username Maker ]")
  print("[ 0 : EXIT ]")
  print("\u001b[0m ")
  menuinput = input("Option : ")
  if menuinput=="1":
    print("\u001b[37;1m  ")
    print("[ 1 ] USER FACEBOOK ")
    print("[ 2 ] USER INSTAGRAM ")
    print("[ 3 ] USER Tiktok ")
    print("[ 4 ] USER TWETAR ")
    print("[ 0 ] BACK ")
    print(" \u001b[0m")
    usercheckinput = input("Option : ")
    if usercheckinput=="1":
      time.sleep(2)
      facebookuser()
    elif usercheckinput=="2":
      time.sleep(2)
      intsauser()
    elif usercheckinput=="3":
      time.sleep(2)
      Tikuser()
    elif usercheckinput=="4":
      time.sleep(2)
      twitteruser()
    elif usercheckinput=="0":
      menu()
    else:
      menu()
  elif menuinput=="0":
    sys.exit()
  elif menuinput=="2":
    time.sleep(2)
    mk()
  else:
    print("\u001b[31;1mI don't Understand what do you want please write correct option\u001b[0m")
    time.sleep(2)
    menu()


menu()
