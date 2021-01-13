from  django.shortcuts import render
import MySQLdb
def admin_login(request):
    return render(request,'adminlogin.html',{'msg':''})
def check_admin_login(request):
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
    cmd=conn.cursor()
    q="select * from admins where adminid='{}' and password='{}'".format(request.GET['adminid'],request.GET['password'])
    print(q)
    cmd.execute(q)
    result=cmd.fetchone()
    if(result==None):
     return render(request,'adminlogin.html',{'msg':'Invalid Adminid/Password'})
    else:
     return render(request,'adminhome.html',{'result':result})   