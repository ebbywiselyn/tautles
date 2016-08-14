from django.contrib import admin
from polls.models import Question
from polls.models import Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question)
admin.site.register(Choice)
