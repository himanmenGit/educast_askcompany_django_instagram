# Generated by Django 3.0.14 on 2021-04-09 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210409_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='24px * 24px 크기의 png/jpg 파일을 업로드 해주세요', upload_to='accounts/profile/%Y%m%d'),
        ),
    ]
