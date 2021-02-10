# Generated by Django 3.0.5 on 2021-02-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saravanan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avName', models.CharField(max_length=100)),
                ('avlUsers', models.IntegerField(default=1)),
                ('avlYears', models.IntegerField(default=1)),
                ('avlKey', models.TextField(max_length=500, unique=True)),
                ('avlEmail', models.CharField(default=' ', max_length=100)),
                ('avAgent', models.CharField(choices=[('PNR', 'PNR'), ('NAR', 'ANMOL'), ('MAD', 'MADHU'), ('KAR', 'KARTHICK')], default='NAR', max_length=3)),
                ('avActivated', models.BooleanField(default=False)),
                ('avClient', models.CharField(default=' ', max_length=100)),
                ('avExpiry', models.CharField(max_length=100)),
            ],
        ),
    ]
