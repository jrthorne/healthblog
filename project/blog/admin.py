from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ['votes',]

admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)