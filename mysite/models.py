# Create your models here.
# 如果不指定，字段名默认为app_name， 而表明默认为app名+类名： [app_name]_info.
# verbose_name指定在admin管理界面中显示中文；verbose_name表示单数形式的显示，
# verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
from django.db import models

class nowcity(models.Model):  #疫情所有城市的最新数据
    province= models.CharField(db_column='province', max_length=255, blank=True)  # Field name made lowercase.
    city = models.CharField(db_column='city', max_length=255, blank=True,  primary_key=True)  # Field name made lowercase.
    confirmedCount = models.CharField(db_column='confirmedCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deadCount= models.CharField(db_column='deadCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    curedCount= models.CharField(db_column='curedCount', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'nowcity'
class weibo(models.Model):  #疫情微博评论据
    weiboid= models.CharField(db_column='weiboid', max_length=255, blank=True,primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='content', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'weibo'
class nowcountry(models.Model):  #疫情所有国家的最新数据
    province= models.CharField(db_column='province', max_length=255, blank=True, primary_key=True)  # Field name made lowercase.
    confirmedCount = models.CharField(db_column='confirmedCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deadCount= models.CharField(db_column='deadCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    curedCount= models.CharField(db_column='curedCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        #managed = False
        db_table = 'nowcountry'


# date,province,confirm,dead,heal
class alldaycity(models.Model):  #疫情各省份的数据，从2020.1.23  截至目前
    province= models.CharField(db_column='province', max_length=255, blank=True)  # Field name made lowercase.
    date= models.CharField(db_column='data', max_length=255, blank=True,primary_key=True)  # Field name made lowercase.
    confirm = models.CharField(db_column='confirm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dead= models.CharField(db_column='dead', max_length=255, blank=True, null=True)  # Field name made lowercase.
    heal= models.CharField(db_column='heal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        #managed = False
        db_table = 'alldaycity'
class migratehuibei(models.Model):  #疫情各省份的数据，从2020.1.23  截至目前
    province= models.CharField(db_column='province', max_length=255, blank=True)  # Field name made lowercase.
    date= models.CharField(db_column='data', max_length=255, blank=True, primary_key=True)  # Field name made lowercase.
    invalue = models.CharField(db_column='invalue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outvalue=models.CharField(db_column='outvalue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date= models.ForeignKey('alldaycity', to_field='date', on_delete=models.CASCADE)   #外键
    class Meta:
        #managed = False
        db_table = 'migratehubei'

