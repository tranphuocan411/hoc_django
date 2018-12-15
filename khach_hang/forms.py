from django import forms
from .models import M_Khach_hang

class FormDangNhap():    
    ten_dang_nhap = forms.CharField(max_length=50)
    mat_khau = forms.CharField(max_length=100)
    
class FormDangKy(forms.ModelForm):    
    ho_ten = forms.CharField(max_length=264)
    ten_dang_nhap = forms.CharField(max_length=50)
    mat_khau = forms.CharField(widget= forms.PasswordInput())
    confirm = forms.CharField(widget= forms.PasswordInput())
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    dia_chi = forms.CharField(max_length=264)

    class Meta:
        model = M_Khach_hang
        fields = ['ho_ten','ten_dang_nhap','mat_khau','phone','dia_chi']