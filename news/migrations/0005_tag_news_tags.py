# Generated by Django 4.2.5 on 2023-10-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.tag'),
        ),
    ]
