# Generated by Django 3.0 on 2020-12-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='color',
            new_name='cuisine',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ripe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]