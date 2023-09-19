from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import Registerdb,Usersubmitdb,Contactdb
from Adminapp.models import CModulesDB,LessonDB
from django.contrib import messages
from webapp.forms import ChangePasswordForm

# Create your views here.
def indexpage(req):
    moddata = CModulesDB.objects.all()
    return render(req,"Indexpage.html",{'moddata':moddata})

def about(req):
    moddata = CModulesDB.objects.all()
    return render(req,"About.html",{'moddata':moddata})

def contact(req):
    moddata = CModulesDB.objects.all()
    return render(req,"Contact.html",{'moddata':moddata})

def contactsave(req):
    if req.method == "POST":
        msg= req.POST.get('message')
        name= req.POST.get('name')
        email= req.POST.get('email')
        subject= req.POST.get('subject')
        obj1 = Contactdb(Message= msg, Name= name, Email= email, Subject= subject)
        obj1.save()
        return redirect(indexpage)

def module(req,lesson_get):
    moddata = CModulesDB.objects.all()
    ldata = LessonDB.objects.filter(SubName=lesson_get)
    mddata = CModulesDB.objects.filter(Subject=lesson_get)

    data1 = Usersubmitdb.objects.filter(Uname=req.session['username'])
    return render(req,"Modules.html",{'moddata':moddata,'data1':data1,'ldata':ldata,'mddata':mddata})

def module1(req,lesson_get):
    moddata = CModulesDB.objects.all()
    ldata = LessonDB.objects.filter(SubName=lesson_get)
    mddata = CModulesDB.objects.filter(Subject=lesson_get)

    data1 = Usersubmitdb.objects.filter(Uname=req.session['username'])
    return render(req,"Module1.html",{'moddata':moddata,'data1':data1,'ldata':ldata,'mddata':mddata})

def lesson(req,lessonid):
    moddata = CModulesDB.objects.all()
    ldata = CModulesDB.objects.all()
    lessondata = CModulesDB.objects.filter(id=lessonid)
    data1 = Usersubmitdb.objects.filter(Uname=req.session['username'])
    return render(req,lessonid,"Lessons.html",{'moddata':moddata,'lessondata':lessondata,'data1':data1,'ldata':ldata,'lessonid':lessonid})

def assignment(req,lessonid):
    moddata = CModulesDB.objects.all()

    lessondata = LessonDB.objects.filter(id=lessonid)
    mddata = CModulesDB.objects.filter(id=lessonid)
    data1 = Usersubmitdb.objects.filter(Uname=req.session['username'])
    return render(req,"Assignment.html",{'moddata':moddata,'lessondata':lessondata,'data1': data1,'mddata':mddata})

def assignment_save(request):
    if request.method=="POST":
        assign = request.POST.get('assignment_name')
        stdname = request.POST.get('student_name')
        email = request.POST.get('email')
        cmnts = request.POST.get('comments')
        file = request.FILES['upload']

        obj = Usersubmitdb(Modname=assign,Name=stdname,Email=email,Comments=cmnts,Upload=file)
        obj.save()
        messages.success(request,"Assignment Submitted Successfully!!!")
        return redirect(indexpage)


def Register(req):
    return render(req,"Registration.html")

def Register_save(req):
    if req.method == "POST":
        uname = req.POST.get('name')
        mail = req.POST.get('email')

        pwd = req.POST.get('password')

        obj = Registerdb(Name=uname, Email= mail, Password=pwd)
        obj.save()
        messages.success(req,"Registered Successfully!!")
        return redirect(Register)

def Userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('email')
        pwd = request.POST.get('password')

        if Registerdb.objects.filter(Email = uname, Password = pwd).exists():
            request.session['username']=uname
            request.session['password']=pwd

            messages.success(request,"Login Successfull")
            return redirect(indexpage)
        else:
            messages.error(request,"Invalid Username/Password")
            return redirect(Register)

    return redirect(Register)

def change_password(request):
    return render(request, 'Change_password.html')

@login_required
def change_passwords(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update session hash
            messages.success(request, 'Your password was successfully updated!')
            return redirect('indexpage')  # Redirect to user profile or another view
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'Change_password.html', {'form': form})

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Register)
