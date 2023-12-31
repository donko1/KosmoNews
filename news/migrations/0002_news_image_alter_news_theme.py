# Generated by Django 4.2.5 on 2023-12-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='none', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='theme',
            field=models.CharField(choices=[('theme1', 'Политика'), ('theme2', 'Регионы'), ('theme3', 'Инвестиции')], default='', max_length=50),
        ),
    ]
