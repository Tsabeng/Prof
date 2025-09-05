from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Quiz, Evaluation, Contest, Correction
from .serializers import CourseSerializer, QuizSerializer, EvaluationSerializer, ContestSerializer, CorrectionSerializer
from .tasks import process_image_ocr
import pytesseract
from PIL import Image

class CourseUploadView(APIView):
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save(user=request.user)
            # Trigger async OCR processing
            process_image_ocr.delay(course.id, course.image_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizView(APIView):
    def get(self, request, course_id):
        quizzes = Quiz.objects.filter(course_id=course_id)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

class ContestView(APIView):
    def post(self, request):
        serializer = ContestSerializer(data=request.data)
        if serializer.is_valid():
            contest = serializer.save()
            # Simulate quiz generation
            quiz = Quiz.objects.create(
                course_id=contest.quiz.course_id,
                questions=[{"text": "Sample question?", "answer": "Sample"}],
                quiz_type='CONTEST',
                difficulty='MEDIUM'
            )
            contest.quiz = quiz
            contest.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmitEvaluationView(APIView):
    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            evaluation = serializer.save(user=request.user)
            # Simulate IA correction
            correction = Correction.objects.create(
                text="Sample correction: Correct answer is X.",
                source='IA',
                validated=False
            )
            evaluation.correction = correction
            evaluation.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)