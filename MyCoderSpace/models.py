from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from ckeditor.fields import RichTextField
=======
from ckeditor_uploader.fields import RichTextUploadingField
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
<<<<<<< HEAD
    cuerpo = RichTextField(verbose_name="Contenido")
=======
<<<<<<< HEAD
    cuerpo = RichTextUploadingField()
=======
    cuerpo = models.TextField()
    imagen = models.URLField(max_length=300)
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> refs/remotes/origin/main
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    imagen = models.URLField()
    
    def __str__(self):
        return self.titulo

    
