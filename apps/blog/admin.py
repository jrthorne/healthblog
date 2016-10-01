from django.contrib import admin
from .models import Question, Answer, Poster


# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ['votes', ]

admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poster)
