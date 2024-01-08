from http import requests
import PyPDF2
from io import BytesIO


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def convert_text_to_speech(text, output_file, language='en-US', voice_name='en-US-Wavenet-D'):
    tts_api_url = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
    api_key = "GOOGLE_CLOUD_API_KEY"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": language,
            "name": voice_name,
            "ssmlGender": "NEUTRAL"
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        }
    }


