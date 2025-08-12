import time
import openai
from dotenv import load_dotenv
import os
from sarvamai import SarvamAI
from google import genai


load_dotenv()
api_key = os.getenv("SARVAM_AI_API_KEY")

def detect_language_sarvamai(audio_path : str):
    start_time = time.time()
    client = SarvamAI(api_subscription_key=api_key)
    try:
       response = client.speech_to_text.transcribe(
            file=open(audio_path,"rb"),
            model="saarika:v2.5",
            language_code="gu-IN"
       )    
       
       detected_text = response
       
       gemini_api_key = os.getenv("GEMINI_API_KEY")
       
       
        #? Detect Language from text
       client = genai.Client(api_key=gemini_api_key)
        
       response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= f"Detect the language of this text: {detected_text}. Restore only the ISO Code."
        )
        
       lang_code = response.text

       return {
            "provider" : "SarvamAI",
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
