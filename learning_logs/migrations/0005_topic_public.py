# Generated by Django 5.1.3 on 2024-12-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Public'),
        ),
    ]