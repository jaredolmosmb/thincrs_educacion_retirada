# Generated by Django 3.2.12 on 2022-02-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='description',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='requirements',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='what_you_will_learn',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
