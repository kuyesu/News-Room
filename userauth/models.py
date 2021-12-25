from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)

    verbose_name = "Users"


class Code(models.Model):
    number = models.CharField(blank=True, null=True, max_length=5)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



    def __str__(self):
        return '{}'.format(self.number) + ' - code for : ' + '{}'.format(self.user)

    def save(self, *args, **kwargs):
        numbers_list = [x for x in range(10)]
        code_items = []
        for i in range(5):
            num = random.choice(numbers_list)
            code_items.append(num)
        code_string = "".join(str(items) for items in code_items)
        self.number = code_string
        super().save(*args, **kwargs)
    
            
    