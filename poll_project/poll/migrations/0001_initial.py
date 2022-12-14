# Generated by Django 4.1.1 on 2022-09-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.CharField(max_length=30)),
                ('op2', models.CharField(max_length=30)),
                ('op3', models.CharField(max_length=30)),
                ('op1_count', models.IntegerField(default=0)),
                ('op2_count', models.IntegerField(default=0)),
                ('op3_count', models.IntegerField(default=0)),
            ],
        ),
    ]
