# Generated by Django 4.1.6 on 2023-04-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='messages',
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='house.chat'),
        ),
    ]
