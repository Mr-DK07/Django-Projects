# Generated by Django 3.2.4 on 2023-10-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Mobile', models.CharField(max_length=20, null=True)),
                ('Message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='explore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=200, null=True)),
                ('epic', models.ImageField(null=True, upload_to='static/explorepic/')),
                ('edate', models.DateField()),
            ],
        ),
    ]
