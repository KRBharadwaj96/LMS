from django.urls import path
from Adminapp import views


urlpatterns = [
    path('AdminIndex/',views.AdmIndex,name="AdmIndex"),

    path('Modules/',views.AddModule,name= "AddModule"),
    path('Savemodule/',views.SaveModule,name="SaveModule"),
    path('Displaymodule/',views.Moduledisplay,name="Moduledisplay"),
    path('Editmodule/<int:moduleid>/',views.Moduleedit,name="Moduleedit"),
    path('Updatemodule/<int:moduleid>/',views.Moduleupdate,name="Moduleupdate"),
    path('Deletemodule/<int:moduleid>/',views.Moduledelete,name="Moduledelete"),

    path('Admin_LoginPage/',views.Adminlogin_render,name="Adminlogin_render"),
    path('Admin_Login/',views.Admin_login,name="Admin_login"),
    path('Admin_Logout/',views.Admin_logout,name="Admin_logout"),

    path('Lessons/',views.AddLesson,name= "AddLesson"),
    path('LessonsSave/',views.SaveLesson,name= "SaveLesson"),
    path('LessonsDisplay/',views.Lessondisplay,name= "Lessondisplay"),
    path('Lessonedit/<int:lessonid>/',views.Lessonedit,name= "Lessonedit"),
    path('Lessonupdate/<int:lessonid>/',views.Lessonupdate,name= "Lessonupdate"),
    path('LessonsDisplay/<int:lessonid>/',views.Lessondelete,name= "Lessondelete"),

    path('Displaycontact/',views.Displaycontact,name="Displaycontact"),
    path('DisplaySubmission/',views.DisplaySubmission,name="DisplaySubmission"),
    path('Submitdelete/<int:dataid>/',views.Submitdelete,name="Submitdelete"),
]

