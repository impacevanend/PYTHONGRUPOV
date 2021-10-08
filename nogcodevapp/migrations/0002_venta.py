# Generated by Django 3.2.8 on 2021-10-07 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nogcodevapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta', to='nogcodevapp.factura')),
            ],
        ),
    ]