from django.shortcuts import render
import MySQLdb
def showUserProduct(request):
  return render(request,'userProduct.html',{'mesg':''})

def submitUserProduct(request):
 try:
   conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
   cmd=conn.cursor()
   q="insert into userproducts(productid,channel,place,email) values('{}','{}','{}','{}')".format(request.GET['productid'],request.GET['channel'],request.GET['place'],request.GET['email'])
   cmd.execute(q)
   conn.commit()
   conn.close()
   mesg='Record Submitted'
 except Exception as e:
   mesg=e
 return render(request,'userProduct.html',{'mesg':mesg})      	

    	