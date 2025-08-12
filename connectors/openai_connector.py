import time
import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_keyapi_key = os.getenv("OPENAI_API_KEY")

def detect_language_openai(audio_path : str):
    start_time = time.time()
    try:
        with open(audio_path,"rb") as f:
            transcription = openai.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=f
            );
        detected_text = transcription.text
    
        #? Detect Language from text
        lang_response = openai.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{
                "role" : "user",
                "content" : f"Detect the language of this text: {detected_text}. Restore only the ISO Code."
            }]
        )

        lang_code = lang_response.choices[0].message.content.strip()

        return {
            "provider" : "OpenAI",
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
