# Generated by Django 4.1.6 on 2023-02-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0013_house_image1_house_image10_house_image11_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image1',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image10',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image11',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image12',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image13',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image14',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image15',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image16',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image8',
        ),
        migrations.RemoveField(
            model_name='house',
            name='image9',
        ),
        migrations.AddField(
            model_name='image',
            name='image10',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image11',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image12',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image13',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image14',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image15',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image16',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image7',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image8',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image9',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house', to='house.house'),
        ),
    ]