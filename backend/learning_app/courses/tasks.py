from celery import shared_task
from .models import Course
from PIL import Image
import pytesseract

@shared_task
def process_image_ocr(course_id):
    try:
        course = Course.objects.get(id=course_id)
        image = Image.open(course.image.path)  # Utilise le chemin du fichier local
        text = pytesseract.image_to_string(image)
        course.ocr_text = text
        course.summary = "Résumé simulé: " + text[:100]
        course.notions = [word for word in text.split()[:5]]
        course.save()
    except Exception as e:
        print(f"Error in OCR: {e}")