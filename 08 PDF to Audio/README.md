
# PDF to Speech Converter

This Python script utilizes the Google Text-to-Speech API to convert text extracted from a PDF file into speech. The resulting audio is saved as an MP3 file, effectively creating a free audiobook.

## Prerequisites

Before running the script, ensure you have the required libraries installed:

```bash
pip install PyPDF2 requests
```

You also need a Google Cloud API key with access to the Text-to-Speech API.

## Usage

1. Replace `"YOUR_GOOGLE_CLOUD_API_KEY"` in the script with your actual Google Cloud API key.

2. Specify the input PDF file path (`pdf_file_path`) and the desired output audio file path (`output_audio_file`) in the script.

3. Run the script:

   ```bash
   python pdf_to_speech.py
   ```

## Script Explanation

- The script uses the PyPDF2 library to extract text from the specified PDF file.

- It then makes an HTTP request to the Google Text-to-Speech API, passing the extracted text and receiving the synthesized audio in response.

- The resulting audio is saved as an MP3 file.

## Important Note

- Using the Google Text-to-Speech API may incur charges. Please check the pricing details on the [Google Cloud Platform](https://cloud.google.com/text-to-speech/pricing) website.

- API usage and authentication mechanisms may change, so consult the [official API documentation](https://cloud.google.com/text-to-speech/docs/reference/rest) for the latest information.

## License
```
This PDF to Speech Converter script is provided under the [MIT License](LICENSE).
```

 README.md can be customized based on any additional details or instructions you want to provide.



# Every line of code
```python
import requests
import PyPDF2
from io import BytesIO
```

1. `import requests`: Imports the `requests` library, which is used for making HTTP requests.

2. `import PyPDF2`: Imports the `PyPDF2` library, a PDF manipulation library in Python.

3. `from io import BytesIO`: Imports the `BytesIO` class from the `io` module, which provides an in-memory binary stream.

```python
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text
```

4. Defines a function `extract_text_from_pdf` that takes a PDF file path as an argument and returns the extracted text.

5. Opens the PDF file in binary mode and creates a `PdfFileReader` object.

6. Iterates through the pages of the PDF, extracts text from each page using `extractText()`, and concatenates it into the `text` variable.

7. Returns the extracted text.

```python
def convert_text_to_speech(text, output_file, language='en-US', voice_name='en-US-Wavenet-D'):
    tts_api_url = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
    api_key = "YOUR_GOOGLE_CLOUD_API_KEY"

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
        print(f"Audio file '{output_file}' created successfully.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
```

8. Defines a function `convert_text_to_speech` that takes text, output file path, language, and voice name as arguments.

9. Sets the Google Text-to-Speech API URL and the API key.

10. Defines headers for the API request, including the `Authorization` header with the API key.

11. Constructs the data payload for the API request, specifying the input text, voice settings, and audio encoding.

12. Makes an HTTP POST request to the Text-to-Speech API with the provided data and headers.

13. If the response status code is 200 (OK), writes the content (audio data) to the specified output file in binary mode.

14. Prints a success message if the audio file is created, otherwise prints an error message with the status code and response text.

```python
if __name__ == "__main__":
    pdf_file_path = "your_pdf_file.pdf"
    output_audio_file = "output_audio.mp3"

    pdf_text = extract_text_from_pdf(pdf_file_path)
    convert_text_to_speech(pdf_text, output_audio_file)
```

15. Checks if the script is being run as the main program.

16. Specifies the PDF file path (`pdf_file_path`) and the output audio file path (`output_audio_file`).

17. Calls the `extract_text_from_pdf` function to extract text from the PDF file.

18. Calls the `convert_text_to_speech` function to convert the extracted text to speech and save it as an MP3 file.

19. The script execution completes.