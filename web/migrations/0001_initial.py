# Generated by Django 2.2.2 on 2019-06-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
                ('description', models.CharField(max_length=124)),
                ('image', models.ImageField(upload_to='blog')),
                ('category', models.CharField(max_length=124)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
                ('posted_by', models.CharField(max_length=124)),
                ('description', models.CharField(max_length=124)),
                ('content', models.CharField(max_length=124)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=124)),
                ('product', models.CharField(max_length=124)),
                ('price', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
                ('description', models.CharField(max_length=124)),
                ('Category', models.CharField(max_length=124)),
                ('price', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='products')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
