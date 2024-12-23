from rest_framework.viewsets import ModelViewSet
from .models import SurveyQuestion, UserResponse
from .serializers import SurveyQuestionSerializer, UserResponseSerializer

class SurveyQuestionViewSet(ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

class UserResponseViewSet(ModelViewSet):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer
