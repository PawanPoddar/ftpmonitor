from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from rest_framework import serializers
# Create your models here.




class Folder(MPTTModel):
    name = models.CharField(max_length=50)
    folder_date = models.DateField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    def get_all_files(self):
        files=self.files_set.all()
        return files


    def __str__(self):
        return self.name
class Files(models.Model):

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50)
    file_date = models.DateField()
    file_time = models.TimeField()
    file_status= models.CharField(max_length=50,default='added')
    check   =models.BooleanField(default=False)
    size = models.CharField(max_length=50)
    folder_name = models.CharField(max_length=50)
    def __str__(self):
         return self.file_name

class auth(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username


