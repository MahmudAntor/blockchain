# Generated by Django 2.0.9 on 2019-07-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0002_auto_20190723_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='policy_header',
        ),
        migrations.AddField(
            model_name='block',
            name='policy_header',
            field=models.ManyToManyField(blank=True, to='local.PolicyHeader'),
        ),
    ]