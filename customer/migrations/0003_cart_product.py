# Generated by Django 3.2.8 on 2021-10-22 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
        ('customer', '0002_auto_20211022_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='superadmin.product'),
            preserve_default=False,
        ),
    ]
