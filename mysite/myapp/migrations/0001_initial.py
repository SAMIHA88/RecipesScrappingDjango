# Generated by Django 4.2 on 2023-05-02 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationCommentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileUtilisateur',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.personne')),
                ('adresse', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
            ],
            bases=('myapp.personne',),
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('temps_preparation', models.IntegerField()),
                ('etapes', models.TextField()),
                ('commentaires', models.ManyToManyField(through='myapp.AssociationCommentaire', to='myapp.personne')),
                ('images', models.ManyToManyField(to='myapp.image')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('recette', models.ManyToManyField(to='myapp.recette')),
            ],
        ),
        migrations.AddField(
            model_name='associationcommentaire',
            name='commentaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.commentaire'),
        ),
        migrations.AddField(
            model_name='associationcommentaire',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.note'),
        ),
        migrations.AddField(
            model_name='associationcommentaire',
            name='personne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.personne'),
        ),
        migrations.AddField(
            model_name='associationcommentaire',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recette'),
        ),
    ]