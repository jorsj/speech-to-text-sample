# Google Cloud Speech-to-Text V2 Batch Transcription**

**Overview**

This repository contains a Python script (`speech_to_text_v2.py`) that utilizes Google Cloud Speech-to-Text V2 to perform asynchronous speech recognition, optimized for transcribing phone conversations in US Spanish. The output transcription is stored in Google Cloud Storage.

**Key Features**

* **Optimized for telephony:** Employs the "chirp_telephony" speech model specifically tailored for telephone-quality audio.
* **US Spanish:** Configured to process speech in US Spanish (`es-US`).
* **Asynchronous operation:** Leverages batch transcription for efficient processing of audio.
* **Flexible output:** Stores the transcription results in a Google Cloud Storage location for easy retrieval.

**Prerequisites**

* A Google Cloud Platform project with the following:
   - Cloud Speech-to-Text V2 API enabled.
   - A service account with permissions to use the Speech-to-Text API. 
   - A Google Cloud Storage bucket.
* Google Cloud SDK installed and configured ([https://cloud.google.com/sdk](https://cloud.google.com/sdk)).

**Setup**

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install google-cloud-speech google-api-core
   ```
3. Set up a suitable recognizer resource. Learn more here: [https://cloud.google.com/speech-to-text/v2/docs/recognizers](https://cloud.google.com/speech-to-text/v2/docs/recognizers). 
4. Set the following environment variables:
   * `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud service account credentials file.
   * `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID

**Usage**

1. Update **line 20 (`project_id = ...`)**, **line 22 (`input_gcs_path = ...`)**, and **line 24 (`output_gcs_path = ...`)** in the `speech_to_text_v2.py` file with your Google Cloud project details and input/output file locations in GCS.

2. Run the script:
   ```bash
   python speech_to_text_v2.py
   ```

3. The transcription will be available in the output GCS bucket upon completion.

**Notes**

* The script assumes the "chirp_telephony" model and other relevant recognizer resources have already been set up within your Google Cloud project. 
* Asynchronous transcription means the operation runs in the background. To obtain detailed results and any potential errors, consult the operation object returned by the `batch_recognize` call.
* Adjust the configuration settings (e.g., model, language codes) as needed for your specific transcription requirements.
* For production systems, implement proper error handling and logging.

**Additional Information**

* Google Cloud Speech-to-Text V2 documentation:  [https://cloud.google.com/speech-to-text/v2/docs](https://cloud.google.com/speech-to-text/v2/docs)
