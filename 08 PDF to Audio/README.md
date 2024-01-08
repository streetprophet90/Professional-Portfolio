
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

This PDF to Speech Converter script is provided under the [MIT License](LICENSE).
```

 README.md can be customized based on any additional details or instructions you want to provide.