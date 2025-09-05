from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes_taught')
    students = models.ManyToManyField(User, related_name='classes_enrolled')

class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/',null=True, blank=True) 
    ocr_text = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    notions = models.JSONField(default=list)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    versions = models.ManyToManyField('self', symmetrical=False)

class Quiz(models.Model):
    TYPE_CHOICES = (
        ('QUIZ', 'Quiz'),
        ('MINI_EVAL', 'Mini Evaluation'),
        ('CONTEST', 'Contest'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.JSONField(default=list)
    quiz_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    difficulty = models.CharField(max_length=20, default='MEDIUM')

class Evaluation(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    correction = models.OneToOneField('Correction', on_delete=models.SET_NULL, null=True)

class Contest(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    leaderboard = models.JSONField(default=dict)

class Correction(models.Model):
    SOURCE_CHOICES = (
        ('IA', 'IA'),
        ('TEACHER', 'Teacher'),
    )
    text = models.TextField()
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    validated = models.BooleanField(default=False)

class Schedule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    revisions = models.JSONField(default=list)