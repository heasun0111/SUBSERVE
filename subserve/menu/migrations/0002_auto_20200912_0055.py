# Generated by Django 2.1.1 on 2020-09-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
