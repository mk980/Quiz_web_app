from django.contrib import admin
from .models import User, TriviaQuestion, AnswersSet, LeaderBoard
# Register your models here.
admin.site.register(User)
admin.site.register(TriviaQuestion)
admin.site.register(AnswersSet)
admin.site.register(LeaderBoard)