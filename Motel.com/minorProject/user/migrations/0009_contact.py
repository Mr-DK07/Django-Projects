# Generated by Django 3.2.4 on 2023-10-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_homeguest_hgprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('cno', models.IntegerField(max_length=13, null=True)),
                ('cmesge', models.TextField(null=True)),
            ],
        ),
    ]
