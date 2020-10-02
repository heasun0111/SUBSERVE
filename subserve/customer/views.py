from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Customer
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def signUp(request) :
    return render(request, 'signup.html')

def signIn(request) :
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        customer = auth.authenticate(request, username = username, password = password)
        if customer is not None:
            auth.login(request,customer)
            print(customer.username)
            return redirect("/")
        else:
            return render(request, 'signin.html', {'error': "There is No user"})
    else:
        return render(request, 'signin.html')



def myPage(request) :
    return render(request, 'mypage.html')

def editProfile(request) :
    return render(request, 'editprofile.html')

def findAccount(request) :
    return render(request, 'findaccount.html')

def confirmPassword(request) :
    return render(request, 'confirmpassword.html')

def resign(request) :
    return render(request, 'resign.html')

def signUpAPI(request) :
    print(request.POST['pwd'])
    # scenario 1. check every values correct
    if request.POST.get('pwd')!=request.POST.get('pwdconfirm'):
        print("wrong password")
        return JsonResponse({
            'status' : 'false',
            'message' : "비밀번호가 서로 다릅니다.",
        }, status=500)

    try:
        user = Customer.objects.get(name = request.POST.get('id', ''))
        print("id already been taken")
        return JsonResponse({
            'status' : 'false',
            'message' : "Id already been taken"
        }, status=500)

    except Customer.DoesNotExist:
        user = User.objects.create(username = request.POST.get('id', ''), password = request.POST.get('pwd', ''), email = request.POST.get('email', ''))
        name = request.POST.get('name', '')
        if request.POST.get('sex', '')=="male":
            sex = 1
        else:
            sex = 0
        address = request.POST.get('address', '')
        birthday = request.POST.get('birthday', '')
        phone = request.POST.get('phone', '')
        customer = Customer(name= name, address = address, birthday = birthday, phone = phone, sex = sex)
        customer.save()
        auth.login(request, user)
        return HttpResponse(status=200)


def loginAPI(request) :
    print(request.POST)
    userID = request.POST.get('id')
    userPW = request.POST.get('pw')
    user = auth.authenticate(request, username=userID, password = userPW)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'mypage.html', {'error' : 'id나 비밀번호를 다시 확인해주세요'})
    

def logout(request) :
    print("ASDFASDFA")
    auth.logout(request)
    return redirect('/')


def editProfileAPI(request) :
    address = request.POST.get('address')
    phone = request.POST.get('phone')

    # 유저정보 가져와서 업데이트하는 쿼리

    return render(request, 'mypage.html')