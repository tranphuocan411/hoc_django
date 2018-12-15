from django.db import models

# Create your models here.
class M_Khach_hang(models.Model):    
    ho_ten = models.CharField(max_length=264, blank=True)
    ten_dang_nhap = models.CharField(max_length=50, blank=True)
    mat_khau = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=264, blank=True)
    email = models.EmailField(max_length=264, blank=True)
    dia_chi = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.ho_ten
    class Meta:
        db_table = u'KhachHang'
