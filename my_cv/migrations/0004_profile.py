# Generated by Django 4.1.9 on 2023-06-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0003_personal_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1500)),
            ],
        ),
    ]