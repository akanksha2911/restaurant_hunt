# Generated by Django 4.2.3 on 2023-07-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
