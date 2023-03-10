# Generated by Django 3.2.4 on 2023-02-05 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20230205_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsForm',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('updated_date', models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc))),
                ('title', models.CharField(default='designation', max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='carrer/Screenshot_3.png', upload_to='Carrer/%Y/%m/%d')),
                ('Email', models.CharField(max_length=200)),
                ('company', models.CharField(default='designation', max_length=200)),
                ('event', models.CharField(default='department', max_length=200)),
                ('linkedin', models.CharField(default='qualififcation', max_length=200)),
                ('website', models.CharField(default='qualififcation', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='birac',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carrer',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logo',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mission',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sisfs',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tbi',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='value',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vision',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 5, 8, 4, 32, 915873, tzinfo=utc)),
        ),
    ]
