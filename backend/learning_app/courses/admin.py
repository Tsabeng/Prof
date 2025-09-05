from django.contrib import admin
from .models import Class, Course, Quiz, Evaluation, Contest, Correction, Schedule

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'ocr_text')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('course', 'quiz_type', 'difficulty')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score', 'date')

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')

@admin.register(Correction)
class CorrectionAdmin(admin.ModelAdmin):
    list_display = ('text', 'source', 'validated')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user',)