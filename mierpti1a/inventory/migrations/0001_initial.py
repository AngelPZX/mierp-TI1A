# Generated by Django 5.1.1 on 2024-11-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.IntegerField()),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('salida', 'Salida')], max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('sucursal_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.IntegerField()),
                ('cantidad', models.PositiveIntegerField()),
                ('proveedor', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('entregado', 'Entregado')], default='pendiente', max_length=10)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAnalisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_informe', models.CharField(max_length=50)),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
                ('detalle', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='StockEnPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.IntegerField()),
                ('cantidad_en_pedido', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
