# Generated by Django 2.2.2 on 2019-06-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.CharField(default=None, max_length=124),
            preserve_default=False,
        ),
    ]
