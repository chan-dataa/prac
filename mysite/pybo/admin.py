from django.contrib import admin
from .models import *


class QuizAdmin(admin.ModelAdmin):
    search_fields = ['title']

class DAdmin(admin.ModelAdmin):
    search_fileds = ['tit', 'ques', 'content1', 'content2', 'content3', 'content4', 'content5']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(D, DAdmin)
