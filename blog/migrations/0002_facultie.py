# Generated by Django 5.0.3 on 2024-03-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Facultie')),
                ('name', models.CharField(max_length=65)),
                ('position', models.TextField()),
            ],
        ),
    ]
