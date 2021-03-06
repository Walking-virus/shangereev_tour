# Generated by Django 3.0.1 on 2020-03-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_auto_20200302_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ('-sending_date',)},
        ),
        migrations.AlterModelOptions(
            name='travel',
            options={'ordering': ('name_travel',)},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_aboutUs',
            field=models.ImageField(upload_to='images_aboutUs/'),
        ),
        migrations.AlterField(
            model_name='command',
            name='photo_employee',
            field=models.ImageField(upload_to='photo_employee/'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='photo_main',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='video_travel',
            field=models.FileField(upload_to='video_travel/'),
        ),
    ]
