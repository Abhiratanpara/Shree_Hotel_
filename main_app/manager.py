from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True

def create_user(self, email, password=None, **extra_fieldes):
    if not email:
        raise ValueError("email")
    user=self.model(email=email,**extra_fieldes)
    user=self.normalize_email(email)
    user.set_password(password)
    user.save(using=self.db)
    return user

def create_superuser(self,email,password=None, **extra_fieldes):
    extra_fieldes.setdefault('is_staff',True)
    extra_fieldes.setdefault('is_superuser',True)
    extra_fieldes.setdefault('is_active',True)
    
    return self.create_user(email,password,**extra_fieldes)