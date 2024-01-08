from http import requests
import PyPDF2
from io import BytesIO

pdf_path = "C:\Users\Rash\Downloads\Climatechange.pdf"

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

    response = requests.post(tts_api_url, json=data, headers=headers)
    if response.status_code == 200:
        with open(output_file, 'wb') as audio_file:
            audio_file.write(response.content)
        print(f"Audio file '{output_file}' created successfully")
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    pdf_file_path = "C:\Users\Rash\Downloads\climate_change.pdf"
    output_audio_file = "climate_change.mp3"

    pdf_text = extract_text_from_pdf(pdf_file_path)
    convert_text_to_speech(pdf_text, output_audio_file)

