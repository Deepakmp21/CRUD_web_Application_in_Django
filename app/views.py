from django.shortcuts import render,redirect

from .models import *

# Create your views here.

def IndexPage(request): # Index.html View
    return render(request,"app/index.html")

def UploadImage(request):
    if request.method =="POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg = ImageData.objects.create(Imagename=imagename,Image=pics)
        return redirect('show1')
    
def ImageFetch(request):
    all_img = ImageData.objects.all()
    return render(request,"app/show1.html",{'key3':all_img})


def htmlform(request):
    return render(request,"app/Forms.html")

def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    # Data comes to server or Data come from HTML to View
    fname =request.POST['fname']
    lname =request.POST['lname']
    email =request.POST['email']
    contact =request.POST['contact']


    #Creating Object of Model Class
    #Inserting data into Table

    newuser = Student.objects.create(Firstname = fname , Lastname = lname,
                                     Email = email, Contact = contact)
    
    # After Insert render on ShowPage View
    return redirect('showpage')
    
# show page view

def ShowPage(request):
    #select * from table name
    # for fetcthing all the data of the table
    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

#Edit page view

def EditPage(request,pk):
    # Fetching the data of Particular ID
    get_data = Student.objects.get(id = pk)
    return render(request,"app/edit.html",{'key2':get_data})

# Update Data View

def UpdateData(request,pk):
    udata=Student.objects.get(id = pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    # Query for Update

    udata.save()

    # Render to Show Page

    return redirect('showpage')


def Register(request):
    return render(request,"app/registration.html")


def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname= request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = User.objects.filter(email=email)

        if user:
            message = "User already exits"
            return render(request,"app/registration.html",{'msg':message})
        
        else:
            if password == cpassword:
                newuser = User.objects.create(firstname=fname,lastname=lname,email=email,contact=contact,password=password)

                message = "User registered successfully"
                return render(request,"app/login.html",{'msg':message})
            
            else:
                message = "password and confirm password does not match "
                return render(request,"app/registration.html",{'msg':message})
            
# Login View

def LoginPage(request):
    return render(request,"app/login.html")


def LoginUser(request):
    if request.method =="POST":
        email =request.POST['email']
        password = request.POST['password']
        
        user = User.objects.get(email=email)

        if user:
            if user.password == password:

                request.session['firstname'] = user.firstname
                request.session['lastname'] = user.lastname
                request.session['email'] = user.email
                return render(request,"app/home.html")
            
            else:
                message ="password does not match"
                return render(request,"app/login.html",{'msg': message})
            
        else:
            message = "User does not exist"
            return render(request,"app/registration.html",{'msg':message})