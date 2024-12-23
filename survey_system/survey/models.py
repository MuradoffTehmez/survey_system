from django.db import models

class SurveyQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    answer_options = models.JSONField()  # Cavabların JSON formatında saxlanması
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user_id} - {self.selected_option}"
