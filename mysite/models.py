# Create your models here.
# 如果不指定，字段名默认为app_name， 而表明默认为app名+类名： [app_name]_info.
# verbose_name指定在admin管理界面中显示中文；verbose_name表示单数形式的显示，
# verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
from django.db import models
class RatingsExplicit(models.Model):
    userid = models.CharField(db_column='userID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookrating = models.CharField(db_column='bookRating', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'RatingsExplicit'


class RatingsImplicit(models.Model):
    userid = models.CharField(db_column='userID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookrating = models.CharField(db_column='bookRating', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'RatingsImplicit'