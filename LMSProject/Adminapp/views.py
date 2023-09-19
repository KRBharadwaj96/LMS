from django.shortcuts import render,redirect
from Adminapp.models import CModulesDB,LessonDB
from webapp.models import Contactdb,Usersubmitdb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def AdmIndex(request):
    return render(request,"AdmIndex.html")

def Displaycontact(req):
    contacting = Contactdb.objects.all()
    return render(req,"Usercontact.html",{'contacting':contacting})

def DisplaySubmission(req):
    submit = Usersubmitdb.objects.all()
    return render(req,"DisplaySubmission.html",{'submit':submit})

def Submitdelete(req,dataid):
    submit = Usersubmitdb.objects.filter(id=dataid)
    submit.delete()
    return redirect(DisplaySubmission)


def AddModule(request):
    return render(request,"AddModules.html")

def SaveModule(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        Mname = request.POST.get('ModName')
        material = request.POST.get('NewMaterial')
        image = request.FILES['imge']
        filMaterial = request.FILES['fileMaterial']


        sel = request.POST.get('select')
        obj1 = CModulesDB(Subject= sub,NewModule=Mname,Material=material,Files=filMaterial,Select=sel,Image=image)
        obj1.save()
        messages.success(request,"Modules Saved Successfully!!!")
        return redirect(AddModule)

def Moduledisplay(request):
    module = CModulesDB.objects.all()
    return render(request,"DisplayModules.html",{'module':module})

def Moduleedit(request,moduleid):
    module = CModulesDB.objects.get(id=moduleid)
    return render(request,"EditModules.html",{'module':module})

def Moduleupdate(request,moduleid):
    if request.method == "POST":
        sub = request.POST.get('subject')
        Mname = request.POST.get('ModName')
        material = request.POST.get('NewMaterial')
        sel = request.POST.get('select')
        try:
            fle = request.FILES['fileMaterial']
            fs = FileSystemStorage()
            file= fs.save(fle.name,fle)

        except MultiValueDictKeyError:
            file = CModulesDB.objects.get(id=moduleid).Files
            CModulesDB.objects.filter(id=moduleid).update(Subject=sub,NewModule=Mname,Material=material,Files=file,Select=sel)
            messages.success(request,"Saved Successfully")
            return redirect(Moduledisplay)

def Moduledelete(request,moduleid):
    module = CModulesDB.objects.filter(id=moduleid)
    module.delete()
    return redirect(Moduledisplay)

def Adminlogin_render(request):
    return render(request,"AdmLogin.html")

def Admin_login(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request,"LOGGED IN")
                return redirect(AdmIndex)
            else:
                messages.error(request,"INVALID CREDENTIALS")
                return redirect(Adminlogin_render)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Adminlogin_render)

def AddLesson(request):
    module = CModulesDB.objects.all()
    return render(request,"AddLessons.html",{'module':module})

def SaveLesson(request):
    if request.method == "POST":
        sub = request.POST.get('subName')
        lsn = request.POST.get('LessonName')
        vid = request.FILES['video']
        img = request.FILES['image']

        obj = LessonDB(SubName=sub,LessonName=lsn,Videos=vid,Study_m=img)
        obj.save()
        messages.success(request,"Lessons Saved Successfully!!")
        return redirect(AddLesson)

def Lessondisplay(request):
    lesson = LessonDB.objects.all()
    messages.success(request,"Lesson loaded!!")
    return render(request,"DisplayLessons.html",{'lesson':lesson})

def Lessonedit(request,lessonid):
    module = CModulesDB.objects.all()
    lesson = LessonDB.objects.get(id=lessonid)
    return render(request,"EditLessons.html",{'module':module,'lesson':lesson})

def Lessonupdate(request,lessonid):
    if request.method == "POST":
        sub = request.POST.get('subName')
        lsn = request.POST.get('LessonName')
        try:
            vid = request.FILES['video']
            img = request.FILES['image']
            fs = FileSystemStorage()
            vidfle = fs.save(vid.name,vid)
            imgfle = fs.save(img.name,img)

        except MultiValueDictKeyError:
            vidfle = LessonDB.objects.get(id=lessonid).Videos
            imgfle = LessonDB.objects.get(id=lessonid).Study_m
        LessonDB.objects.filter(id=lessonid).update(SubName= sub,LessonName= lsn ,Videos = vidfle,Study_m= imgfle)
        messages.success(request,"Saved Successfully")
        return redirect(Lessondisplay)

def Lessondelete(request,lessonid):
    lesson = LessonDB.objects.filter(id=lessonid)
    lesson.delete()
    return redirect(Lessondisplay)



