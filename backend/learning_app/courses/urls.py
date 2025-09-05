from django.urls import path
from .views import CourseUploadView, QuizView, ContestView, SubmitEvaluationView

urlpatterns = [
    path('courses/upload/', CourseUploadView.as_view(), name='course-upload'),
    path('quizzes/<int:course_id>/', QuizView.as_view(), name='quiz-list'),
    path('contests/', ContestView.as_view(), name='contest-create'),
    path('evaluations/', SubmitEvaluationView.as_view(), name='evaluation-submit'),
]