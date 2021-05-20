from django.contrib.auth.backends import ModelBackend as BaseModel
from .models import User

class ModelsBackEnd(BaseModel):
    
    def authenticate(self,request,username=None, password=None, **kwargs):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except user.DoesNotExist:
                pass
                
            return super().authenticate(request, username=username, password=password, **kwargs)

