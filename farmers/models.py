from django.db import models

# Create your models here.

class user1(models.Model):
    f_name=models.CharField(max_length=30)
    m_name=models.CharField(max_length=30,blank=True)
    l_name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    prof_pic=models.ImageField()
    class Meta:
        abstract=True
    def __str__(self):
        return (self.f_name + ' ' + self.m_name + ' ' + self.l_name)

class farmer(user1):
    addr_l1=models.CharField(max_length=100,null=True)
    addr_l2=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    is_farmer = models.BooleanField(default=False)
    def __str__(self):
        return (self.f_name + ' ' + self.m_name + ' ' + self.l_name)

class labourer(user1):
    city=models.CharField(max_length=100 ,null=True)
    state = models.CharField(max_length=100,null=True)
    is_worker = models.BooleanField(default=False)    
    def __str__(self):
        return (self.f_name + ' ' + self.m_name + ' ' + self.l_name)
    
class seller(user1):
    b_name=models.CharField(max_length=100)
    addr_l1=models.CharField(max_length=100,null=True)
    addr_l2=models.CharField(max_length=100,null=True)
    is_seller = models.BooleanField(default=False)
    city=models.CharField(max_length=100)
    state = models.CharField(max_length=100,null=True)


class transport(user1):
    transport_mode=models.CharField(max_length=100)
    weight_capacity=models.CharField(max_length=100)
    reg_no=models.CharField(max_length=100)
    is_transport = models.BooleanField(default=False)    
    permit_type=models.CharField(max_length=100,choices=((1,'state permit'),(2,'national permit')))


