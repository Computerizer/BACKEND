# Generated by Django 4.0.5 on 2022-07-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password1',
            field=models.CharField(default='test123', max_length=20),
            preserve_default=False,
        ),
    ]
