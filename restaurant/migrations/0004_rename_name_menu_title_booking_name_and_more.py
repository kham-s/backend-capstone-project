# Generated by Django 4.1.6 on 2023-02-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]