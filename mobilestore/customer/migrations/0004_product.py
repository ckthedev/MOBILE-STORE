# Generated by Django 4.1.7 on 2023-03-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_rename_order_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
