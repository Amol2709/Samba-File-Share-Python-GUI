import CreateShare as cs
import DeleteShare as ds
import CheckShare as csh

def modify(share_name,public,writeable,browseable,read_only,validusers):
	if(csh.exists(share_name)):
		file = "/etc/samba/smb.conf"
		lines = []
		f = open(file,'r')
		flag = False
		for line in f:
			if(line == "[" + share_name + "]\n"):
				flag = True
				continue
			elif(flag):
				if(line[:5] == "\tpath"):
					path = line[8:-1]
					flag = False
			else:
				continue

		f.close()

		a = ds.delete(share_name)
		b = cs.create(share_name,path,public,writeable,browseable,read_only,validusers)
		return True
	else:
		return False
