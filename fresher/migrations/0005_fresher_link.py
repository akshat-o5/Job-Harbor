# Generated by Django 5.0.3 on 2024-03-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresher', '0004_fresher_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='fresher',
            name='link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
