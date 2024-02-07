 from django.http import JsonResponse
import requests
from .models import Game, AnswersSet, TriviaQuestion


def fetch_categories():
	try:
		response = requests.get('https://opentdb.com/api_category.php')
		return response
	except Exception as e:
		print(f"Error fetching categories: {e}")
		return None


def fetch_question():
	try:
		response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
		return response
	except Exception as e:
		print(f"Error fetching questions: {e}")
		return None




