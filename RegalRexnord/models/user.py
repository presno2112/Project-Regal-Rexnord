from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

# TODo
# metodo para conectar con unity
# metodo para dashboard

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
    password = models.CharField(_("password"), max_length=128, validators=[MinLengthValidator(6)])
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def dashboard_info(self):
        from .results import Results
        if self.is_admin:
            results = Results.objects.all().filter(user=self)
            return results
        else:
            results_everyone = Results.objects.all()
            return results_everyone

    @property
    def totalscore(self):
        from .results import Results
        scores = Results.objects.all().filter(user=self) 
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
        results = Results.objects.distinct().filter(user=self, completed=True)
        '''for result in results:
            if (result.completed == True):
                number_completed += 1
            if number_completed > 5: # cambiar este numero dependiendo de cuantos juegos sean
                number_completed = 5
                '''
        return 5 if len(results) > 5 else len(results)
    


# 
#  como editar permissions en carpeta utils???