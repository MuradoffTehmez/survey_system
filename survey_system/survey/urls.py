from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyQuestionViewSet, UserResponseViewSet

router = DefaultRouter()
router.register(r'v1/questions', SurveyQuestionViewSet)
router.register(r'v1/responses', UserResponseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
