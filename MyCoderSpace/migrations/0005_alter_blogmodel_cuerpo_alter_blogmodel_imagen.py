# Generated by Django 4.0.4 on 2022-06-26 19:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCoderSpace', '0004_alter_blogmodel_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='cuerpo',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='imagen',
            field=models.URLField(),
        ),
    ]
