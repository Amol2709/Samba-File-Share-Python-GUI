import DeleteShare as ds
import CreateShare as cs
import ModifyShare as ms
import GetShare as gs
# ds.delete("share2")
# cs.create("public-samba","/public",True,False)
# ms.modify("share10",True,True,False,False,[])
info = gs.getshare("share10")
print(info)