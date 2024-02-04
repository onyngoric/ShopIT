# Generated by Django 4.1.5 on 2024-02-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0012_ad_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('adId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.ad')),
            ],
            options={
                'verbose_name_plural': 'AdMessages',
            },
        ),
    ]
