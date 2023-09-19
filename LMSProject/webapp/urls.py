from django.urls import path
from webapp import views


urlpatterns = [
    path('',views.indexpage,name="indexpage"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('contactsave/',views.contactsave,name="contactsave"),

    path('module/<lesson_get>',views.module,name="module"),
    path('module1/<lesson_get>',views.module1,name="module1"),
    path('lesson/',views.lesson,name="lesson"),
    path('assignment/<int:lessonid>/',views.assignment,name="assignment"),
    path('assignment_save/',views.assignment_save,name="assignment_save"),

    path('register/',views.Register,name="Register"),
    path('register_save/',views.Register_save,name="Register_save"),
    path('change_password/',views.change_password, name="change_password"),

    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('Userlogout',views.Userlogout,name="Userlogout"),

]