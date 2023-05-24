# Generated by Django 4.1.7 on 2023-04-27 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=50, verbose_name='Nombre de Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMarca', models.CharField(max_length=50, verbose_name='Nombre de la marca')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMunicipio', models.CharField(max_length=50, verbose_name='Nombre del municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIV', models.CharField(help_text='NIV del vehiculo', max_length=20)),
                ('noMotor', models.CharField(blank=True, max_length=30)),
                ('linea', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=4)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.marca')),
            ],
            options={
                'verbose_name_plural': 'VEHICULOS',
                'db_table': 'vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RFC', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apPaterno', models.CharField(max_length=30)),
                ('apMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('CURP', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=40)),
                ('CP', models.CharField(max_length=5)),
                ('edad', models.IntegerField(default=0)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Placa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('numTC', models.CharField(max_length=20)),
                ('fecha', models.DateField(auto_now=True)),
                ('estatus', models.BooleanField(default=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.oficina')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.propietario')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.vehiculo')),
            ],
        ),
    ]
