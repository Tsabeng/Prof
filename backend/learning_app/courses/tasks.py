from celery import shared_task
from .models import Course
from PIL import Image
import pytesseract

@shared_task
def process_image_ocr(course_id):
    try:
        print(f"Starting OCR for course ID: {course_id}")  
        course = Course.objects.get(id=course_id)
        print(f"Image path: {course.image.path}")  
        image = Image.open(course.image.path)
        print("Image opened successfully")  
        text = pytesseract.image_to_string(image)
        print(f"Extracted text: {text}")  
        course.ocr_text = text
        course.summary = "Résumé simulé: " + text[:100]
        course.notions = [word for word in text.split()[:5]]
        course.save()
        print("Course updated successfully")  
    except Exception as e:
        print(f"Error in OCR: {e}")
        raise  