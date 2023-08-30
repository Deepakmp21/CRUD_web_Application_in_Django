from django.urls import path ,include
from . import views
urlpatterns = [
        path("index/", views.IndexPage,name="index"),
        path("upload/",views.UploadImage,name="imageupload"),
        path("showing/",views.ImageFetch,name="show1"),
        path("form",views.htmlform,name="htmlform"),
        path("",views.InsertPageView,name="insertpage"),
        path("insert/",views.InsertData,name="insert"),
        path("showpage/",views.ShowPage,name="showpage"),
        path("editpage/<int:pk>",views.EditPage,name="editpage"),
        path("update/<int:pk>",views.UpdateData,name="update"),
        path("register/",views.Register,name="registerpage"),
        path("registered/",views.UserRegister,name="register"),
        path("loginpage/",views.LoginPage,name="loginpage"),
        path("loginuser/",views.LoginUser,name="login"),

] 