# Generated by Django 5.0.6 on 2024-05-31 08:17

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


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
                ('rol', models.CharField(choices=[('alumno', 'Alumno'), ('especialista', 'Especialista')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20)),
                ('carrera', models.CharField(max_length=100)),
                ('año', models.IntegerField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=100)),
                ('numero_licencia', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateTimeField()),
                ('tipo_cita', models.CharField(choices=[('presencial', 'Presencial'), ('virtual', 'Virtual')], max_length=20)),
                ('notas', models.TextField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alumno')),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.especialista')),
            ],
        ),
        migrations.CreateModel(
            name='PruebaAnsiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.especialista')),
            ],
        ),
        migrations.CreateModel(
            name='PruebaEvaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.especialista')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('tipo_pregunta', models.CharField(choices=[('opcion_multiple', 'Opción Múltiple'), ('verdadero_falso', 'Verdadero/Falso'), ('respuesta_abierta', 'Respuesta Abierta')], max_length=20)),
                ('dificultad', models.IntegerField()),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pruebaevaluacion')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('es_correcta', models.BooleanField()),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaPruebaAnsiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_1', models.IntegerField()),
                ('respuesta_2', models.IntegerField()),
                ('respuesta_3', models.IntegerField()),
                ('respuesta_4', models.IntegerField()),
                ('respuesta_5', models.IntegerField()),
                ('respuesta_6', models.IntegerField()),
                ('respuesta_7', models.IntegerField()),
                ('respuesta_8', models.IntegerField()),
                ('respuesta_9', models.IntegerField()),
                ('respuesta_10', models.IntegerField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pruebaansiedad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.TextField(blank=True, null=True)),
                ('respondido_el', models.DateTimeField(auto_now_add=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pregunta')),
                ('respuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.respuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoEvaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField()),
                ('comentarios', models.TextField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pruebaevaluacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoPruebaAnsiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion_total', models.IntegerField()),
                ('interpretacion', models.TextField()),
                ('recomendaciones', models.TextField()),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pruebaansiedad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField()),
                ('plan_tratamiento', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alumno')),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.especialista')),
            ],
        ),
    ]
