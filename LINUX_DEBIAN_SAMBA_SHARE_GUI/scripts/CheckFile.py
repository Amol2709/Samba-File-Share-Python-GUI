def fileexists(path = "/etc/samba/smb.conf"):
	try:
		f = open(path,'r')
		f.close()
		return True
	except FileNotFoundError:
		return False
