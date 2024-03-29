# Generated by Django 5.0.1 on 2024-02-07 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.CharField(max_length=128)),
                ('incorrect_answer1', models.CharField(max_length=128)),
                ('incorrect_answer2', models.CharField(max_length=128)),
                ('incorrect_answer3', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TriviaQuestion',
            fields=[
                ('category', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=10)),
                ('question', models.TextField(max_length=500)),
                ('type', models.CharField(max_length=15)),
                ('answer_set', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Quiz_.answersset')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=100)),
                ('user_last_name', models.CharField(max_length=100)),
                ('user_age', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_location', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Quiz_.game')),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name=10)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Quiz_.user')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='trivia_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Quiz_.triviaquestion'),
        ),
    ]
