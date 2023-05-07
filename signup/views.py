from django.shortcuts import render
import mysql.connector as sql
nm=''
cry=''
cl=''
s=''
em=''
no=''
dment=''
yr=''
pwd=''
# Create your views here.
def signupaction(request):
    global nm,cry,cl,s,em,no,dment,yr,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Ankush@123",database='yantrapro')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                nm=value
            if key=="country":
                cry=value
            if key=="college":
                cl=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="contactNo":
                no=value
            if key=="Department":
                dment=value 
            if key=="year":
                yr=value    
            if key=="password":
                pwd=value
        c="insert into info Values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nm,cry,cl,s,em,no,dment,yr,pwd)  
        cursor.execute(c)
        m.commit()
    return render(request,'signup.html')