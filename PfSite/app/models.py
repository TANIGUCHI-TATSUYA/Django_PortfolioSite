from django.db import models

# Create your models here.
class Profile(models.Model):
    title=models.CharField('タイトル',max_length=100,null=True,blank=True)
    sub_title=models.CharField('サブタイトル',max_length=100,null=True,blank=True)
    name=models.CharField('名前',max_length=100,null=True,blank=True)
    job=models.TextField('仕事',)
    intoroduction=models.TextField('自己紹介')
    github=models.CharField('github',max_length=100,null=True,blank=True)
    twitter=models.CharField('twitter',max_length=100,null=True,blank=True)
    topimage = models.ImageField(upload_to='images',verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images',verbose_name='サブ画像')

    def __str__(self):
        return self.name
