# Generated by Django 3.1.7 on 2022-02-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('description', models.CharField(max_length=150)),
                ('kind', models.CharField(max_length=30)),
                ('avatar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Check_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('description', models.CharField(max_length=150)),
                ('kind', models.CharField(max_length=30)),
                ('avatar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('image', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=120)),
                ('date', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=120)),
                ('file_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=120)),
                ('message', models.CharField(max_length=120)),
                ('date', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
            ],
        ),
    ]
