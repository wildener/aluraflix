# Generated by Django 3.2.1 on 2021-07-27 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backflix', '0003_video_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='backflix.categoria'),
        ),
    ]