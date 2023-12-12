# Generated by Django 4.2.7 on 2023-12-03 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cours', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_salle', models.CharField(max_length=100)),
                ('capacite', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EmploiDuTemps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour_semaine', models.CharField(max_length=100)),
                ('heure_debut', models.CharField(max_length=100)),
                ('heure_fin', models.CharField(max_length=100)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduleManagement.cours')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduleManagement.salle')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduleManagement.utilisateur')),
            ],
        ),
    ]