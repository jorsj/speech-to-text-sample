from google.api_core.client_options import ClientOptions
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from google.cloud.speech_v2 import BatchRecognizeFileMetadata

# **Instantiate a client object for interacting with Google Cloud Speech-to-Text**
# * Customize the API endpoint if needed for your region.
client = SpeechClient(
    client_options=ClientOptions(api_endpoint="us-central1-speech.googleapis.com")
)

# **Project ID for billing and resource management**
project_id = "sandcastle-401718"  # Replace with your Google Cloud project ID

# **Input audio file's location in Google Cloud Storage (GCS)**
input_gcs_path = f"gs://{project_id}/bch/flac/6538427.flac" 

# **Desired output location in GCS for the generated transcript** 
output_gcs_path = f"gs://{project_id}/bch/txt/6538427.flac/"

# **Configuration for the speech recognition process**
config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),  # Automatically determine audio encoding
    model="chirp_telephony",  # Speech model optimized for phone conversations
    language_codes=["es-US"],  # Process Spanish (US) speech
    features=cloud_speech.RecognitionFeatures(
        enable_word_time_offsets=False,  # Do not provide timestamps for each word 
        multi_channel_mode=cloud_speech.RecognitionFeatures.MultiChannelMode.MULTI_CHANNEL_MODE_UNSPECIFIED, 
        # Default behavior: only transcribe the first audio channel 
    ),
)

# **Output configuration specifying GCS as the storage location**
output_config = cloud_speech.RecognitionOutputConfig(
    gcs_output_config=cloud_speech.GcsOutputConfig(
        uri=output_gcs_path
    ),
)

# **Metadata describing the input audio file**
file_metadata = BatchRecognizeFileMetadata(
    uri=input_gcs_path
)

# **Construct the speech recognition request**
request = cloud_speech.BatchRecognizeRequest(
    recognizer=f"projects/{project_id}/locations/us-central1/recognizers/_",  # Specify the recognizer resource
    config=config, 
    files=[file_metadata], 
    recognition_output_config=output_config,
    processing_strategy=cloud_speech.BatchRecognizeRequest.ProcessingStrategy.DYNAMIC_BATCHING 
    # Allow Google Cloud to streamline file batching for efficiency
)

# **Initiate the speech recognition operation (asynchronous)**
# * This starts a background operation; use operation.result() to wait for completion and get results.  
operation = client.batch_recognize(request=request)

operation.result()  # Access the transcription results once the operation is finished
