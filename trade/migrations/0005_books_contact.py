# Generated by Django 3.1.5 on 2021-01-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20210131_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='contact',
            field=models.IntegerField(max_length=12, null=True),
        ),
    ]
