# Generated by Django 4.1.5 on 2023-12-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_alter_adimages_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.CharField(choices=[('3D Printing & Robotics', (('3D Printing Technology', '3D Printing Technology'), ('Roboticts', 'Robotics'))), ('Automobile & Vehicles', 'Automobile & Vehicles'), ('Air Transport', 'Air Transport'), ('Business', 'Business'), ('Classes', 'Classes'), ('Clothing', 'Clothing'), ('Community', 'Community'), ('Construction & Farming Equipments', 'Construction & Farming Equipments'), ('Electronics', 'Electronics'), ('Freelancing', 'Freelancing'), ('Furniture', 'Furniture'), ('Insurance', 'Insurance'), ('Jobs', 'Jobs'), ('Matrimonial', 'Matrimonial'), ('Pets', 'Pets'), ('Real Estate, Housing & Rentals', 'Real Estate, Housing & Rentals'), ('Sales', 'Sales'), ('Services', 'Services'), ('Softwares', 'Softwares'), ('Space & Astronomy', 'Space & Astronomy'), ('Tickets', 'Tickets'), ('Travels, Holiday & Leisure', 'Travels, Holiday & Leisure'), ('Others...', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='adimages',
            name='media',
            field=models.FileField(upload_to='images/'),
        ),
    ]
