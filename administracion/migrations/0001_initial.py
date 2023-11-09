# Generated by Django 3.2.18 on 2023-09-12 17:08

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('max_capacity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Disponibilidades',
            },
        ),
        migrations.CreateModel(
            name='Campsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(null=True, upload_to='imagenes/')),
            ],
            options={
                'db_table': 'Campings',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('capacity', models.IntegerField()),
                ('price', models.FloatField(max_length=10)),
            ],
            options={
                'db_table': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='NaturalPark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('province', models.IntegerField(choices=[(1, 'Buenos Aires'), (2, 'Ciudad Autónoma de Buenos Aires'), (3, 'Catamarca'), (4, 'Chaco'), (5, 'Chubut'), (6, 'Córdoba'), (7, 'Corrientes'), (8, 'Entre Ríos'), (9, 'Formosa'), (10, 'Jujuy'), (11, 'Salta'), (12, 'Tucumán'), (13, 'La Pampa'), (14, 'La Rioja'), (15, 'San Juan'), (16, 'Mendoza'), (17, 'Misiones'), (18, 'Neuquén'), (19, 'Río Negro'), (20, 'San Luis'), (21, 'Santa Cruz'), (22, 'Santa Fé'), (23, 'Santiago del Estero'), (24, 'Tierra del Fuego')])),
                ('image', models.ImageField(null=True, upload_to='imagenes/')),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Parques_Naturales',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('percentage', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('number_guests', models.IntegerField()),
                ('total_cost', models.FloatField(max_length=10)),
                ('reservation_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('baja', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Abonada', 'Abonada'), ('Pendiente', 'Pendiente de Pago')], default='Pendiente de Pago', max_length=20)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.availability')),
                ('campsite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='administracion.campsite')),
                ('temporada', models.ManyToManyField(related_name='campsites', to='administracion.Season')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=255)),
                ('is_client', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('is_saved', models.BooleanField(default=False)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.reservation')),
            ],
            options={
                'db_table': 'Guests',
            },
        ),
        migrations.AddField(
            model_name='campsite',
            name='categories',
            field=models.ManyToManyField(related_name='campsites', to='administracion.Category'),
        ),
        migrations.AddField(
            model_name='campsite',
            name='natural_park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campsites', to='administracion.naturalpark'),
        ),
        migrations.AddField(
            model_name='availability',
            name='campsite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='administracion.campsite'),
        ),
    ]
