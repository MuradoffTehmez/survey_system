from django.contrib import admin
from .models import SurveyQuestion, UserResponse

admin.site.register(SurveyQuestion)
admin.site.register(UserResponse)
