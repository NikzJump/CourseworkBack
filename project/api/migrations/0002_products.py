# Generated by Django 5.1.1 on 2025-05-29 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ram')),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.case')),
                ('coolers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cooler')),
                ('discs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.disc')),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fan')),
                ('graphic_cards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.graphiccard')),
                ('headphones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.headphones')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.keyboard')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.monitor')),
                ('motherboards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.motherboard')),
                ('mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mouse')),
                ('power_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.powerunit')),
                ('processors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.processor')),
            ],
        ),
    ]
