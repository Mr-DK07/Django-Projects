# Generated by Django 3.2.4 on 2023-10-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_homeguest'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeguest',
            name='hgprice',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
