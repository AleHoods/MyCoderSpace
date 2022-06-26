<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User
=======
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e


<<<<<<< HEAD
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
=======
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
