from rest_framework import serializers
from .models import Course, Quiz, Evaluation, Contest, Correction

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'image', 'ocr_text', 'summary', 'notions']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'course', 'questions', 'quiz_type', 'difficulty']

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['id', 'quiz', 'user', 'score', 'date', 'correction']

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'name', 'start_date', 'end_date', 'class_ref', 'quiz', 'leaderboard']

class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = ['id', 'text', 'source', 'validated']