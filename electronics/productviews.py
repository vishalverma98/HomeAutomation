from django.shortcuts import render
import MySQLdb
def product_interface(request):
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='electronics')
    cmd=conn.cursor()
    q='select * from devices'
    cmd.execute(q)
    result=cmd.fetchall()
    conn.close()
    return render(request,'product.html',{"msg":"","result":result})
def product_submit(request):
    if(request.method=="POST"):
        try:
            file=request.FILES['image']
            conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='Electronics')
            cmd=conn.cursor()
            q="insert into products(deviceid,productid,productname,productmodel,price,description,image) values('{}','{}','{}','{}','{}','{}','{}')".format(request.POST['deviceid'],request.POST['productid'],request.POST['productname'],request.POST['productmodel'],request.POST['price'],request.POST['description'],file.name)
            cmd.execute(q)
            conn.commit()
            conn.close()
            msg="Record Submitted..."
            f=open('e:/Electronics/asset/'+file.name,'wb')
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
        except Exception as e:
            msg=e;
    return render(request,'product.html',{"msg":msg})

def product_display(request):
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='Electronics')
    cmd=conn.cursor()
    q='select * from products'
    cmd.execute(q)
    result=cmd.fetchall()
    conn.close()
    return render(request,'displayallproduct.html',{'result':result})

def product_display_id(request):
    conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='Electronics')
    cmd=conn.cursor()
    q="select * from products where productid='{}'".format(request.GET['productid'])
    print(q)
    cmd.execute(q)
    result=cmd.fetchone()
    print(result)
    conn.close()
    return render(request,'displaybyproductid.html',{'result':result})

def product_edit_delete(request):
    if request.method=='POST':
     conn=MySQLdb.connect(host='localhost',port=3307,user='root',passwd='123',db='Electronics')
     cmd=conn.cursor()
     if(request.POST['btn']=='Delete'):
      q="delete from products where productid='{}'".format(request.POST['productid'])
      cmd.execute(q)
      conn.commit()
     elif(request.POST['btn']=='Edit'):
      q="update products set deviceid='{}',productname='{}',productmodel='{}',price='{}',description='{}' where productid='{}'".format(request.POST['deviceid'],request.GET['productname'],request.GET['productmodel'],request.GET['price'],request.POST['description'],request.POST['productid'])
      cmd.execute(q)
      conn.commit()
     elif(request.POST['btn']=='Edit Picture'):
      file=request.FILES['image']    
      q="update products set image='{}' where productid='{}'".format(file.name,request.POST['productid'])
      cmd.execute(q)
      conn.commit()
      f=open("E:/electronics/asset/"+file.name,'wb')
      for chunk in file.chunks():
       f.write(chunk)
      f.close()  
      conn.close()
    return product_display(request)