from django.contrib import admin
from main_app.models import contact
from main_app.models import services
from main_app.models import slider
from main_app.models import staff
from main_app.models import category_rooms
from main_app.models import user

class contactadmin(admin.ModelAdmin):
    list_display=('id','name','email','message')
    
admin.site.register(contact,contactadmin)

class servicesadmin(admin.ModelAdmin):
    list_display=('id','image','title','description')
    
admin.site.register(services,servicesadmin)

class slideradmin(admin.ModelAdmin):
    list_display=('id','image','title','description')
    
admin.site.register(slider,slideradmin)

class staffadmin(admin.ModelAdmin):
    list_display=('id','image','name','position','facebook_link','linkedin_link','instagram_link','twitter_link')
    
admin.site.register(staff,staffadmin)

class category_roomsadmin(admin.ModelAdmin):
    list_display=('id','image','category_name','description','foot','people_Capacity','room_price')
    
admin.site.register(category_rooms,category_roomsadmin)

class useradmin(admin.ModelAdmin):
    list_display=('id','name','email','phone_no','image','address','pincode','birth','password','confirm_password')
    
admin.site.register(user,useradmin)
# Register your models here.

