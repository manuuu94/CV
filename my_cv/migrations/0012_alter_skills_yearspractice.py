# Generated by Django 4.1.9 on 2023-06-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0011_alter_skills_skillname_alter_skills_yearspractice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='yearsPractice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]