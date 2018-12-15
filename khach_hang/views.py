from django.shortcuts import render
from khach_hang.models import *
from django.shortcuts import redirect
from khach_hang import forms
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Create your views here.
def dang_nhap(request):
    err = ''
    hasher = PBKDF2PasswordHasher()
    if request.method == 'POST':
        _ten = request.POST.get('ten_dang_nhap')
        _mat_khau = hasher.encode(request.POST.get('mat_khau'), '123')
        kh = M_Khach_hang.objects.filter(ten_dang_nhap=_ten, mat_khau=_mat_khau)
        if kh.count() > 0:
            request.session['username'] = kh[0].ho_ten
            err = 'Da luu khach hang vao session'
            return redirect('khach_hang:quan_tri')
        else:
            err = 'Dang nhap khong thanh cong'
    return render(request, 'khach_hang/dang_nhap.html', {'err': err})

def quan_tri(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'khach_hang/quan_tri.html', {'username': username})
    else:
        return redirect('dang_nhap')

def dang_xuat(request):
    if request.session.has_key('username'):
        del request.session['username']
    return redirect('khach_hang:dang_nhap')

def dang_ky(request):
    registered = False
    if request.method == 'POST':
        from_user = forms.FormDangKy(request.POST, M_Khach_hang)
        hasher = PBKDF2PasswordHasher()
        if from_user.is_valid() and from_user.cleaned_data['mat_khau'] == from_user.cleaned_data['confirm']:
            request.POST._mutable = True
            post = from_user.save(commit=False)
            post.ho_ten = from_user.cleaned_data['ho_ten']
            post.ten_dang_nhap = from_user.cleaned_data['ten_dang_nhap']
            post.mat_khau = hasher.encode(from_user.cleaned_data['mat_khau'], '123')
            # chuỗi '123' là tuỳ ý
            post.email = from_user.cleaned_data['email']
            post.phone = from_user.cleaned_data['phone']
            post.email = from_user.cleaned_data['email']
            post.dia_chi = from_user.cleaned_data['dia_chi']
            post.save()
            print('Da ghi vao CSDL')
        elif from_user.cleaned_data['mat_khau'] != from_user.cleaned_data['confirm']:
            from_user.add_error('confirm', 'the password do not match')
            print('password and confirm password are not the same!')
    else:
        from_user = forms.FormDangKy()
    return render(request, 'khach_hang/registration.html' , {'user_form': from_user, 'registered': registered})