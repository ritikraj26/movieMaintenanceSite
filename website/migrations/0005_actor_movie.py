# Generated by Django 4.0.4 on 2022-04-22 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_movie_rename_actorlist_actor_delete_movielist'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='website.movie'),
        ),
    ]
