ó
ÿc           @   s  e  Z e r# d  d  Z   Z n  yÜ d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z Wn8 e k
 r9e j d  e j d  e j d  n Xe e  e j d	  e j   Z e j e   e j e j j   d
 d d g e _ d   Z  d   Z! d   Z" d   Z# d Z$ d   Z% d  Z& g  Z' d   Z( d   Z) d   Z* d   Z+ e, d k re(   n  d S(   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   pip2 install requestss   pip2 install mechanizes   python2 hcrack.pyt   utf8t   max_timei   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   950934743o.pyR      s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   950934743o.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   950934743o.pyR   $   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   950934743o.pyt   hamza.   s    sx  
[1;97m88888888ba   88b           d88  I8,        8        ,8I  
[1;97m88      "8b  888b         d888  `8b       d8b       d8'  
[1;97m88      ,8P  88`8b       d8'88   "8,     ,8"8,     ,8"   
[1;97m88aaaaaa8P'  88 `8b     d8' 88    Y8     8P Y8     8P    
[1;97m88aaaaaaP    88  `8b   d8'  88    `8b   d8' `8b   d8'    
[1;97m88      `8b  88   `8b d8'   88     `8a a8'   `8a a8'     
[1;97m88      a8P  88    `888'    88      `8a8'     `8a8'      
[1;97m88888888P"   88     `8'     88       `8'       `8'       

[1;97mCreated By A7Ae MARG !!

[1;97mMy Telegram : [1;97m@A7Ae_MARG

[1;97mMy Chanell  : [1;97m@A7AeMARG
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [ ] Generating Access Token i   (   R   R   R   R   R   (   t   titikt   o(    (    s   950934743o.pyt   tikE   s
      c          C   sÄ   t  j d  t GHt d  }  |  d k rL t  j d  t GHd |  d GHn d GHt j d  t   t d  } | d k rÀ t  j d  t GHd |  d GHd	 | d
 GHt j d  t   n  d  S(   Nt   clears   [+] Username : t   MARGs   [ ] Username : s
    (correct)s   [!] Invalid Username.i   s   [+] Password : s   [ ] Password : s     (correct)i   (   R   t   systemt   bannert	   raw_inputR   R   t   tlogint   methodlogin(   t   usernamet   passw(    (    s   950934743o.pyR)   M   s$    c          C   s   t  j d  t GHHd GHd GHd GHt d  }  |  d k rI d GHt   n> |  d k re t  j d	  n" |  d
 k r{ t   n d GHt   d  S(   NR$   s   [1] Crack Menus%   [2] Create Access Token (New Account)s         s   
Choose Option >>  R	   s   [!]  Wrong Inputt   1s   python2 hop2.pyt   2s   Wrong Input(   R   R&   R'   R(   R   t   login_fb(   t   hos(    (    s   950934743o.pyR*   f   s     

c          C   s7  t  j d  t GHHt d  Ht d  t d  Hd d GHHt d  }  |  j d d	  } t d
  } t   t j d | d | d  } t	 j
 |  } d | k rî t d d  } | j | d  | j   d GHt j d  t   nE d | d k rd GHt j d  t   n d GHt j d  t   d  S(   NR$   s9   [1;47;31m          Generate Access Token          [1;0ms#   [!] Donot Use Your Personal Accounts    [!] Use A Fresh Account To Logini/   t   -s   [?] Number/ID : t    R	   s   [?] Password : s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens	   token.txtR   s(   
[ ] Access Token Generated Successfullyi   s   www.facebook.comt	   error_msgs2   
[!] User Must Verify His/Her Account Before Logini   s$   
[!] Number/ID/Password May Be Wrong(   R   R&   R'   R    R(   R   R#   t   brt   opent   jsont   loadR   t   closeR   R   t
   show_tokenR/   (   t   iidt   idt   pwdt   dataR   t   st(    (    s   950934743o.pyR/   x   s<    


	


c           C   sF   d GHd GHd d GHHt  j d  Hd d GHt d  t  j d  d  S(   Ns   [ ] Your Access Tokens   [ ] Copy This Tokeni/   R1   s   cat token.txts    [Press Enter To Start Cracking] s   python2 hop2.py(   R   R&   R(   (    (    (    s   950934743o.pyR:      s    		
t   __main__(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](-   t   Falset   foot   barR   R   R   t   datetimeR   t   hashlibt   ret	   threadingR7   t   urllibt	   cookielibt   getpasst	   mechanizet   requestst   multiprocessing.poolR    t   requests.exceptionsR   R   t   ImportErrorR&   t   reloadt   setdefaultencodingR5   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R'   R#   t   backR<   R)   R*   R/   R:   t   __name__(    (    (    s   950934743o.pyt   <module>   s@   
¨
			
					!	