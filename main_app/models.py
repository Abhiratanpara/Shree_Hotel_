from django.db import models

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    message=models.TextField()
    
class services(models.Model):
    image=models.FileField(upload_to="services_img/",max_length=500,null=True,default=None)
    title=models.CharField(max_length=50)
    description=models.TextField()

class slider(models.Model):
    image=models.FileField(upload_to="slider_img/",max_length=500,null=True,default=None)
    title=models.CharField(max_length=50)
    description=models.TextField()
    
class staff(models.Model):
    image=models.FileField(upload_to="staff_img/",max_length=500,null=True,default=None)
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    facebook_link=models.CharField(max_length=500,null=True,blank=True,default='#')
    linkedin_link=models.CharField(max_length=500,null=True,blank=True,default='#')
    instagram_link=models.CharField(max_length=500,null=True,blank=True,default='#')
    twitter_link=models.CharField(max_length=500,null=True,blank=True,default='#')
    
class category_rooms(models.Model):
    image=models.FileField(upload_to="category_rooms_img/",max_length=500,null=True,default=None)
    category_name=models.CharField(max_length=25)
    description=models.TextField(max_length=155)
    foot=models.IntegerField(max_length=3)
    people_Capacity=models.IntegerField(max_length=3)
    room_price=models.IntegerField(max_length=10)
    
# class user(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField(max_length=100)
#     phone_no=models.BigIntegerField(max_length=12)
#     image=models.FileField(upload_to="user_img/",max_length=500,null=True,default=None)
#     address=models.TextField()
#     pincode=models.BigIntegerField(max_length=6)
#     birth=models.DateField()
#     password=models.CharField(max_length=200)
#     confirm_password=models.CharField(max_length=200)
    
    
    
# class room(models.Model):
#     room_no = models.IntegerField()
#     image = models.FileField(upload_to="room_img/", max_length=500)
#     room_name = models.CharField(max_length=50)
#     aboults = models.IntegerField()
#     children = models.IntegerField()
#     room_price = models.IntegerField()

# class booking(models.Model):
#     room = models.ForeignKey(room, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.BigIntegerField()
#     city = models.CharField(max_length=50)
#     adulte = models.IntegerField()
#     children = models.IntegerField()
#     check_in = models.DateField()     
#     check_out = models.DateField()

    
class room(models.Model):
    Room_No=models.IntegerField(max_length=5)
    image=models.FileField(upload_to="room_img/",max_length=500)
    room_name=models.CharField(max_length=50)
    aboults=models.IntegerField(max_length=20)
    children=models.IntegerField(max_length=20)
    room_price=models.IntegerField(max_length=5)
    
class booking(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField(max_length=12)
    city=models.CharField(max_length=50)
    adulte=models.IntegerField(max_length=5)
    children=models.IntegerField(max_length=5)
    check_in=models.DateField()     
    check_out=models.DateField()
    Room_No=models.ForeignKey(room,on_delete=models.CASCADE)   
    
    @property 
    def RoomNo(self):
        return self.Room_No

# Create your models here.

