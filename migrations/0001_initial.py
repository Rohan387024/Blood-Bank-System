# Generated by Django on 16=07-2022

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('blood_group', models.CharField(max_length=4)),
                ('dob', models.DateField()),
                ('mobile_no', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=15)),
                ('availability', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'UserDetails',
            },
        ),
    ]
