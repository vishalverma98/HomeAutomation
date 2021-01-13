from  django.shortcuts import render
import MySQLdb
def device_interface(request):
    return render(request,'deviceinterface.html',{'msg':''})
def device_submit(request):
 if(request.method=='POST'):
   try:
    file=request.FILES['deviceimage']  
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
    cmd=conn.cursor()
    q="insert into devices(devicename,description,image) values('{}','{}','{}')".format(request.POST['devicename'],request.POST['description'],file.name)
    cmd.execute(q)
    conn.commit()
    conn.close() 
    msg='Record Submitted...'
    f=open("E:/electronics/asset/"+file.name,'wb')
    for chunk in file.chunks():
       f.write(chunk)
    f.close() 
   except Exception as e:
    msg=e
   return render(request,'deviceinterface.html',{'msg':msg})
def device_display(request):
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
    cmd=conn.cursor()
    q='select * from devices'
    cmd.execute(q)
    result=cmd.fetchall()
    conn.close()
    return render(request,'displayalldevice.html',{'result':result})

def device_display_id(request):
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
    cmd=conn.cursor()
    q='select * from devices where deviceid={}'.format(request.GET['deviceid'])
    cmd.execute(q)
    result=cmd.fetchone()
    conn.close()
    return render(request,'displaybyid.html',{'result':result})
def device_edit_delete(request):
    if request.method=='POST':
     conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
     cmd=conn.cursor()
     if(request.POST['btn']=='Delete'):
      q='delete from devices where deviceid={}'.format(request.POST['deviceid'])
      cmd.execute(q)
      conn.commit()
     elif(request.POST['btn']=='Edit'):
      q="update devices set devicename='{}',description='{}' where deviceid={}".format(request.POST['devicename'],request.POST['description'],request.POST['deviceid'])
      cmd.execute(q)
      conn.commit()  
     elif(request.POST['btn']=='Edit Picture'):
      file=request.FILES['deviceimage']    
      q="update devices set image='{}' where deviceid={}".format(file.name,request.POST['deviceid'])
      cmd.execute(q)
      conn.commit()
      f=open("E:/electronics/asset/"+file.name,'wb')
      for chunk in file.chunks():
       f.write(chunk)
      f.close()  

      conn.close()
    return device_display(request)
    #return render(request,'displaybyid.html',{'result':result})
