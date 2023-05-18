# Generated by Django 4.2.1 on 2023-05-14 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_image_alter_listing_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('about', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('skype', models.CharField(max_length=30)),
                ('telegtam', models.CharField(max_length=30)),
                ('whatsapp', models.CharField(max_length=30)),
                ('viber', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='ad_status',
            field=models.CharField(choices=[('Продам', 'Продам'), ('Сдам', 'Сдам')], default='Продам', max_length=10),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='floor_plan',
            field=models.ImageField(blank=True, null=True, upload_to='plans/%y'),
        ),
        migrations.AddField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='type_of_housing',
            field=models.CharField(choices=[('Дом', 'Дом'), ('Коттедж', 'Коттедж'), ('Квартира', 'Квартира'), ('Комната', 'Комната')], default='Квартира', max_length=10),
        ),
        migrations.AddField(
            model_name='listing',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/%y'),
        ),
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.agent'),
        ),
    ]