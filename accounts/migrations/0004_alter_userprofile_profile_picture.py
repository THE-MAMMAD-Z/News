# Generated by Django 4.2.5 on 2023-10-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_gender_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='pics/aks.jpg', upload_to='pics/'),
        ),
    ]
