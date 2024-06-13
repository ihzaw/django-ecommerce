# Generated by Django 5.0.6 on 2024-06-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_product_created_at_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture_url',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
    ]