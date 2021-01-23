import CheckShare as csh

def getshare(share_name):
	if(csh.exists(share_name)):
		file = "/etc/samba/smb.conf"
		flag = False
		f = open(file,'r')
		sharecontent = []
		for line in f:
			if(line == "[" + share_name + "]\n"):
				flag = True
				sharecontent.append(line[:-1])
				continue
			elif((line[0] == '[' or line == '\n') and flag):
				flag = False
			elif(flag):
				sharecontent.append(line.split("=")[1][1:-1])
			else:
				continue
		if(len(sharecontent) == 7):
			sharecontent[-1] = sharecontent[-1].split(" ")
		return sharecontent
	else:
		return []



# a = ["[share3]","path=/etc","writable=yes","radonly=no"]
# for item in a:
# 	label.item
