import time
import openai
from dotenv import load_dotenv
import os
from google import genai


load_dotenv()
openai.api_keyapi_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

def detect_language_gemini(audio_path : str):
    start_time = time.time()
    try:
        # with open(audio_path,"rb") as f:
        #     transcription = openai.audio.transcriptions.create(
        #         model="gpt-4o-mini-transcribe",
        #         file=f
        #     );
        # detected_text = transcription.text
        detected_text = "Bonjour, comment ça va ?"
    
        #? Detect Language from text
        client = genai.Client(api_key=gemini_api_key)
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= f"Detect the language of this text: {detected_text}. Restore only the ISO Code."
        )
        
        lang_code = response.text

        return {
            "provider" : "Gemini",
            "language" : lang_code,
            "time_taken" : round(time.time() - start_time , 2),
            "cost_estimate" : {"tokens" : 0 , "usd" : 0.001},
            "status" : "success",
            "error" : None
        }
    except Exception as e:
        return {
            "provider" : "OpenAI",
            "language" : None,
            "time_taken" : round(time.time() - start_time,2),
            "cost_estimate" : None,
            "status" : "error",
            "error" : e
        }
