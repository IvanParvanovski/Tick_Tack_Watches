# Generated by Django 3.1.4 on 2020-12-10 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('teenagers', 'Teenagers'), ('children', 'Children'), ('unisex', 'Unisex')], default=('male', 'Male'), max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WatchDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_shape', models.CharField(choices=[('circle', 'Circle'), ('square', 'Square'), ('rectangle', 'Rectangle'), ('triangle', 'Triangle'), ('other', 'Other')], default=('other', 'Other'), max_length=20)),
                ('chronograph', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=20)),
                ('dial_colour', models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('gray', 'Gray'), ('silver', 'Silver'), ('maroon', 'Maroon'), ('red', 'Red'), ('rose_gold', 'Rose Gold'), ('other', 'Other')], default=('black', 'Black'), max_length=20)),
                ('strap_colour', models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('gray', 'Gray'), ('silver', 'Silver'), ('maroon', 'Maroon'), ('red', 'Red'), ('rose_gold', 'Rose Gold'), ('other', 'Other')], default=('black', 'Black'), max_length=20)),
                ('water_resistance', models.PositiveIntegerField(blank=True, default=0)),
                ('analogue_or_digital', models.CharField(choices=[('analogue', 'Analogue'), ('digital', 'Digital')], default=(('analogue', 'Analogue'), ('digital', 'Digital')), max_length=20)),
                ('watch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='watches.watch')),
            ],
        ),
    ]
