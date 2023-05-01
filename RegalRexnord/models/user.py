from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extrafields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(("Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        
        user.set_password(password)
        user.save()
        return user 



class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    #USERNAME_FIELD = "uid"

    @property
    def totalscore(self):
        from .results import Results
        scores = Results.objects.all().filter(user=self) #asi se hace el query?
        total = 0
        for score in scores:
            total += score.score
        return total
    
    @property
    def avg_time(self):
        from .results import Results
        total_time = 0
        times = Results.objects.all().filter(user=self)
        for time in times:
            total_time += time.time
        if len(times) > 0:
            return total_time / len(times)
        else:
            return 0
        
    @property
    def games_completed(self):
        from .results import Results
        number_completed = 0
        results = Results.objects.all().filter(user=self)
        for result in results:
            if (result.completed == True):
                number_completed += 1
            if number_completed > 5: # cambiar este numero dependiendo de cuantos juegos sean
                number_completed = 5
        return number_completed


# 
#  como editar permissions en carpeta utils???