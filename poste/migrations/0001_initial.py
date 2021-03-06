# Generated by Django 4.0.2 on 2022-02-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrats',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('detail_contrat', models.TextField()),
                ('status', models.IntegerField()),
                ('employe_id', models.PositiveBigIntegerField()),
                ('post_id', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contrats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FailedJobs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('connection', models.TextField()),
                ('queue', models.TextField()),
                ('payload', models.TextField()),
                ('exception', models.TextField()),
                ('failed_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'failed_jobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Migrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('migration', models.CharField(max_length=255)),
                ('batch', models.IntegerField()),
            ],
            options={
                'db_table': 'migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PasswordResets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'password_resets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalAccessTokens',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tokenable_type', models.CharField(max_length=255)),
                ('tokenable_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=64, unique=True)),
                ('abilities', models.TextField(blank=True, null=True)),
                ('last_used_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'personal_access_tokens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Postes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'postes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('password', models.CharField(max_length=255)),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
