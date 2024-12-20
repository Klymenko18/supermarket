# Generated by Django 5.1.3 on 2024-12-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Zip Code')),
                ('street', models.CharField(max_length=255, verbose_name='Street')),
                ('house_number', models.CharField(max_length=10, verbose_name='House number')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('standard', 'Standart Shipping'), ('express', 'Ekspress Shipping')], default='standard', max_length=20, verbose_name='Method Shipping')),
            ],
        ),
    ]
