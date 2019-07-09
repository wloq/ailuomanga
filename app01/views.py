from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login#django自带登陆验证函数库
from django.contrib.auth import logout
from  . models import UserProfile,Duanzi
from django.urls import reverse#反向解析网址
from django.contrib.auth.hashers import make_password#加密密码库
import datetime

# Create your views here.

def index(request):
    num = UserProfile.objects.all().count()
    return render(request,'index.html',{"num":num})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username","")
        pass_word = request.POST.get("password","")
        user = authenticate(username=user_name,password=pass_word)#django自带登陆验证函数
        if user is not None:
            login(request,user)#登陆成功，把user通过request传入index.html中
            request.session["user_id"] = user.id
            return render(request,"index.html")
        else:
            return render(request,'index.html',{"msg":"用户名或者密码错误"})#可以传字符串或者变量到指定页面
    else:
        return render(request,'index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        address = request.POST.get('address')
        if username and password and password1 and email and address:
            if password == password1:
                uc = UserProfile.objects.filter(username=username).all().count()  # 验证用户名是否被注册
                if uc == 0:#用户名不存在
                    user_info = {
                        'username': username,
                        'password': make_password(password),
                        'email' :email,
                        'address' : address,
                    }
                    try:
                        UserProfile.objects.create(**user_info)
                        to_url = reverse('index')
                        return HttpResponseRedirect(to_url)  # 注册成功跳转到首页
                    except Exception as e:
                        msg = '系统繁忙,注册失败 '
                        return render(request, 'error.html', {"msg": msg})
                else:
                    msg = "用户名已存在，请重新注册"
                    return render(request,"error.html",{"msg":msg})
            else:
                msg = "两次输入密码不一样，请重新输入"
                return render(request, "error.html", {"msg": msg})
        else:
            msg = "用户名，密码，邮件，地址不能为空"
            return render(request,"error.html",{"msg":msg})
    else:
        return render(request,"error.html")



def question(request):
    return render(request,"question.html")

def duanzi(request):
    duanzi_all = Duanzi.objects.all()
    num = Duanzi.objects.all().count()
    return render(request, "duanzi.html",{"duanzi_all":duanzi_all,"num":num})

def add_duanzi(request):
    if request.method == 'POST':
        user_id = request.session.get("user_id")
        title = request.POST.get('duanzi_title')
        content = request.POST.get('duanzi_content')
        add_time = datetime.datetime.now()
        if title and content:
            duanzi_info = {
                'title': title,
                'content': content,
                'add_time': add_time,
                'author_id': user_id,
            }
            Duanzi.objects.create(**duanzi_info)
            return redirect('/duanzi/')
        else:
            return render(request, "add_duanzi.html")
    else:
        return render(request,"add_duanzi.html")




    return render(request,"add_duanzi.html")

def tuichu(request):
    logout(request)
    return render(request,"index.html")