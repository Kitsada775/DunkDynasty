# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ล็อกอินผู้ใช้หลังจากสมัคร
            return redirect('home')  # รีไดเรกต์ไปที่หน้า Home หลังจากสมัคร
    else:
        form = UserCreationForm()  # ฟอร์มที่ใช้สมัครสมาชิก
    return render(request, 'signup.html', {'form': form})

# ฟังก์ชันสำหรับล็อกอิน
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # รีไดเรกต์ไปที่หน้า home หลังจากล็อกอิน
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ฟังก์ชันสำหรับหน้า Home ที่ต้องการให้ล็อกอินก่อน
@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # รีไดเรกต์ไปที่หน้า login หลังจากออกจากระบบ