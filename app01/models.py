from django.db import models
from django.contrib.auth.models import AbstractUser #下面用户表继承系统USER表
from datetime import datetime
# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birday = models.DateField(verbose_name="生日",null=True,blank=True)
    gender = models.CharField(choices=(("male",u"男"),("female","女")),default="female",max_length=7)
    address = models.CharField(max_length=100,verbose_name="地址",default=u"")
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)#头像默认上传的地址和路径

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Duanzi(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="作者")
    title = models.CharField(max_length=100,verbose_name="段子标题")
    content = models.TextField(verbose_name="段子详情")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发表时间")

    class Meta:
        verbose_name = "段子信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title