# Generated by Django 4.1.6 on 2023-02-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0015_alter_image_image1_alter_image_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]