from django.contrib import admin
from .models import User, Question, Response, Board

admin.site.register(Board)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Response)
# Register your models here.
