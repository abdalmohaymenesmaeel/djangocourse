from django.db import models
# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.Name

class Product(models.Model):
    lst=[("ggg","ggg"), ("ddd","ddd"), ("eee","eee") ]

    name = models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to="photos/%y/%m/%d")
    active=models.BooleanField(default=True)
    #category=models.CharField(max_length=50,choices=lst)
    categories=models.ForeignKey(Category,on_delete=models.CASCADE,default="")
    #published=models.DateField()
    #time=models.TimeField()
    #datetime=models.DateTimeField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="ttt"