# Generated by Django 2.1.7 on 2019-04-16 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(verbose_name='date posted')),
                ('mod_time', models.DateTimeField(verbose_name='date last modified')),
            ],
        ),
    ]