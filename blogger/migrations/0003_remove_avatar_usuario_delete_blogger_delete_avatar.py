# Generated by Django 4.0.4 on 2022-06-26 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_alter_avatar_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Blogger',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
