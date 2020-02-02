import time
import random
import mechanize
from bs4 import BeautifulSoup

ua = open("user-agent.txt",'r').read().splitlines()
memek = 0 #mati
kontol = 0 #idup =bradu =branak :D

def check(email):
   global ua,memek,kontol
   live = open("live.txt",'a')
   die = open("die.txt",'a')
   br = mechanize.Browser()
   br.set_handle_robots(False)
   br.addheaders = [('User-agent', random.choice(ua))]
   br.open("https://www.ip-tracker.org/checker/email-lookup.php")
   br.select_form(nr=0)
   br.form['email'] = email
   submit = br.submit()
   res = submit.read()
   soup = BeautifulSoup(res,'html.parser')
   get = soup.find_all(class_="lookupgreen")
   if "is <br/>a valid deliverable e-mail box address" in str(get):
          live.write(email+"\n")
          print("\033[1;37m[\033[1;32mLIVE\033[1;37m] "+ email)
          kontol += 1
   else:
          die.write(email+"\n")
          print("\033[1;37m[\033[1;31mDIEE\033[1;37m] "+ email)
          memek += 1
print("""
[ checker email lookup ][ coded by VRX ]
      [ https://github.com/VrX55 ]
""")
list = input("[?] List FiLe: ")
print("="*30)
try:
	buka = open(list,'r').read().splitlines()
	for i in buka:
		check(i)
		time.sleep(1)
	print("[+] RESULT:")
	print("[+] email live:" + str(kontol))
	print("[+] email die:" + str(memek))
	print("[+] data saved \n-live.txt\n-die.txt")
except FileNotFoundError:
	print("[!] file not found")
	exit()
print("[!] Done")