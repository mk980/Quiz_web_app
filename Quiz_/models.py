from django.db import models


class User(models.Model):
	user_first_name = models.CharField(max_length=100, null=False, blank=False)
	user_last_name = models.CharField(max_length=100, null=False, blank=False)
	user_age = models.IntegerField(null=False, blank=False, default=0)
	username = models.CharField(max_length=100, null=False, blank=False)
	user_email = models.EmailField(max_length=100, null=False, blank=False)
	user_location = models.CharField(max_length=100, null=False, blank=False)
	game = models.ForeignKey('Game', on_delete=models.PROTECT)


class Game(models.Model):
	trivia_question = models.ForeignKey('TriviaQuestion', on_delete=models.PROTECT)
	score = models.IntegerField(null=True, blank=True, default=0)


class TriviaQuestion(models.Model):
	category = models.CharField(max_length=200, null=False, blank=False)
	difficulty = models.CharField(max_length=10, null=False, blank=False)
	question = models.TextField(max_length=500, null=False, blank=False)
	type = models.CharField(max_length=15, null=False, blank=False)
	answer_set = models.OneToOneField(
		'AnswersSet',
		on_delete=models.CASCADE,
		primary_key=True)


class AnswersSet(models.Model):
	correct_answer = models.CharField(max_length=128, null=False, blank=False)
	incorrect_answer1 = models.CharField(max_length=128, null=False, blank=False)
	incorrect_answer2 = models.CharField(max_length=128, null=False, blank=False)
	incorrect_answer3 = models.CharField(max_length=128, null=False, blank=False)


class LeaderBoard(models.Model):
	score = models.IntegerField(10, null=True, blank=True)
	player_id = models.ForeignKey('User', on_delete=models.PROTECT, null=False, blank=False)


