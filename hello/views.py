from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import name, per_info,profo_details, expec_salary, post_salary, regform, information, signup
from django.db.models import Q
from django.contrib import messages
#from django.template import loader

# Create your views here.
x=datetime.now

def avgsamp1(request):
    print(HttpResponse("This is my First Danjo project"))
    return HttpResponse("<h1>This is my First Danjo project</h1><p>")
def avgsamp2(request):
    return HttpResponse("This is a basic project")
def avgsamp3(request):
    return HttpResponse("This is fro my understanding")
def index(request):
    print(render(request,'hello world.html'))
    return render(request,'hello world.html')
def square(request):
    range1= range(1,4)
    return render(request,'Div square.html',{'x': range1})
def login(request):
    
    if request.method =='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        
        try:
            user = signup.objects.get(EmailId=email)
            request.session['fname']=user.fname
            if user is not None:
                if pwd==user.pass_1:
                    
                    
                    return redirect('/index1')
                else:
                    messages.error(request,'Password is wrong')
                    
            else:
                messages.error(request,'User doesnot exist')
    
        except:
            messages.error(request,'User doesnot exist')
    return render(request, 'login.html')

def register(request):
    print(request)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        bday = request.POST['dob']
        age = request.POST['age']
        gender = request.POST.get('gender1')
        lang = request.POST.get('lang1')
        email = request.POST['id']
        email_1 = request.POST['id_1']
        if email == email_1:
            pwd_1 = request.POST['pwd_1']
            pwd_2 = request.POST['pwd_2']
            if pwd_1 == pwd_2:
                user=signup(fname=fname, lname=lname,DateOfBirth=bday, Gender=gender,KnownLang=lang, Age=age, EmailId=email, EmailId_1=email_1, pass_1=pwd_1, pass_2=pwd_2)
                user.save()
            else:
                raise("Password does not Match")
        else:
            raise("Email ID does not Match")
        
    return render(request, 'signup.html')

def index_1(request):
    a=request.session.get('fname')
    return render(request, 'index.html',{'date':x,'name':a})
def member(request):
    return render(request, 'member.html',{'date':x})
def add_member(request):
    print(request)
    if request.method == 'POST':
        name = request.POST['full_name']
        profosional = request.POST['profo']
        gender = request.POST['Gender']
        dob = request.POST['dob']
        MNumber=request.POST['mobile_no']
        email = request.POST['email']
        country = request.POST['Country']
        state = request.POST['State']
        district = request.POST['District']
        loc = request.POST['loc']
        member = information(Full_Name=name,Professional=profosional,Gender=gender,DateOfBirth=dob,MobileNumber=MNumber,EmailID=email,Country=country,State=state,District=district,Location=loc)
        member.save()
    return render(request, 'Add members.html',{'date':x})
    
def event(request):
    return render(request, 'Event.html',{'date':x})
def left(request):
    return render(request, 'left-sidebar.html',{'date':x})
def no_side(request):
    return render(request, 'no-sidebar.html',{'date':x})
def report(request):
    return render(request, 'report.html',{'date':x})
def right(request):
    return render(request, 'right-sidebar.html',{'date':x})
def two(request):
    return render(request, 'two-sidebar.html',{'date':x})
def jinja(request):
  #template = loader.get_template('sample.html')
  context = {
    'a': 1,
    'fname': ["jamuna","aarthi","bala","geetha"],
    'lname': "n",

  }
  return render(request, 'sample.html',context)
def square2(request):
    context={
    'range1': range(1,10),
    'range2': range(1,10),
    'fathername': per_info.objects.filter(FatherName__startswith='N'),
    'name': name.objects.filter (Q( fname__endswith='i') & Q(lname__endswith='u')),
    'profo_details': profo_details.objects.all(),
    'expec_salary': expec_salary.objects.filter(expect_salary__range=(70000,80000)),
    'post_salary': post_salary.objects.filter(Designation='Engineer'),
    'regform':regform.objects.filter(Age=32),
    'information' :information.objects.all()
    }
    print(context)
    return render (request, 'squ.html',  context)
  
def image(request):
    range2= range(1,10)
    return render(request,'squ.html',{'myRange': range2})

    
