from celery import shared_task
from .models import Course

@shared_task
def process_image_ocr(course_id, image_url):
    # Simulate OCR (replace with Tesseract/Google Vision)
    try:
        course = Course.objects.get(id=course_id)
        # Example: image = Image.open(image_url)  # For local testing
        # text = pytesseract.image_to_string(image)
        text = "Sample OCR text"  # Placeholder
        course.ocr_text = text
        course.summary = "Sample summary"  # Placeholder for NLP
        course.notions = ["notion1", "notion2"]  # Placeholder
        course.save()
    except Exception as e:
        print(f"Error in OCR: {e}")