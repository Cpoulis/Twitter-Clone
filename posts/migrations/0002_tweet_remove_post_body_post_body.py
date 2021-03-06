# Generated by Django 4.0.4 on 2022-05-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='Body',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='body'),
        ),
    ]
