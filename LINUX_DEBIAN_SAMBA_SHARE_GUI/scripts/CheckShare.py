def exists(share_name):
	file = "/etc/samba/smb.conf"
	f = open(file,'r')

	for line in f:
		if(line == "[" + share_name + "]\n"):
			return True
	return False