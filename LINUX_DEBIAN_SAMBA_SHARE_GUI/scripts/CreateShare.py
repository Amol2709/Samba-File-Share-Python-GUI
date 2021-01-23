import CheckShare as cs

def create(share_name,path,public,writeable,browseable,read_only,validusers):
    if(not cs.exists(share_name)):
        file = "/etc/samba/smb.conf"
        f=open(file,"a")
        f.write("["+share_name+"]\n")
        f.write("\tpath = "+path+"\n")
        if(read_only):
        	f.write("\tread only = yes\n")
        else:
        	f.write("\tread only = no\n")
        if(browseable):
        	f.write("\tbrowseable = yes\n")
        else:
        	f.write("\tbrowseable = no\n")
        if(writeable):
            f.write("\twriteable = yes\n")
        else:
            f.write("\twriteable = no\n")
        if(public):
            f.write("\tpublic = yes\n")
        else:
            f.write("\tpublic = no\n")
            f.write("\tvalid users = ")
            for user in validusers:
                f.write(user.lower() + " ")
            f.write("\n")
        f.close()
        return True
    else:
        return False
