from connectors.openai_connector import detect_language_openai
from connectors.gemini_connector import detect_language_gemini
from connectors.sarvamai_connector import detect_language_sarvamai

def runAll(audio_path : str):
    results = []
    for func in [
        detect_language_sarvamai,
        detect_language_gemini,
    ]:
        results.append(func(audio_path))
    return results