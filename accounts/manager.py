from django.contrib.auth.base_user import BaseUserManager

class CustomerManager(BaseUserManager):
    
    def create_user(self, username, password=None, **extrafields):
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(username=username, **extrafields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, username, password=None, **extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_active',True)
        
        return self.create_user(username,password,**extrafields)
        