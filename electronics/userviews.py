from django.shortcuts import render
import MySQLdb

def showUserInterface(request):
   return render(request,'userInterface.html',{'mesg':''})

def submituser(request):
 try:
 	conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
 	cmd=conn.cursor()
 	q="insert into users values({},'{}','{}','{}','{}')".format(request.GET['mobile'],request.GET['fname'],request.GET['lname'],request.GET['email'],request.GET['password'])
 	cmd.execute(q)
 	conn.commit()
 	conn.close()
 	mesg='record submitted'
 except Exception as e:
 	mesg=e
 return render(request,'userInterface.html',{'mesg':mesg})
 
def userLogin(request):
   return render(request,'userLogin.html',{'mesg':''})

def checkUserLogin(request):
 try:	

  conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
  cmd=conn.cursor()
  q="select * from users where email='{}' and password='{}' ".format(request.GET['email'],request.GET['password'])
  cmd.execute(q)
  result=cmd.fetchone()
  if(result==None):
    return render(request,'userLogin.html',{'mesg':'Invalid Id/Password'})
  else:
    request.session['EMAIL']=request.GET['email']  
    return render(request,'userHome.html',{'result':result})
 except Exception as e:
 	mesg=e
 print(mesg)	

