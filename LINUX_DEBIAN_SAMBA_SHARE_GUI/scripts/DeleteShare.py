import CheckShare as csh

def delete(share_name="public-samba"):
	if(csh.exists(share_name)):
		file = "/etc/samba/smb.conf"
		lines = []
		f = open(file,'r')
		flag = False
		for line in f:
			if(line == "[" + share_name + "]\n"):
				print("share found")
				flag = True
				continue
			elif(line[0]=='[' and flag):
				flag = False
			elif(flag):
				continue
			lines.append(line)
		f.close()

		f= open(file,'w')

		# print(lines)

		for line in lines:
			f.write(line)
		f.close()
		return True

	else:
		return False

