import os
from coordinator import runAll


PUBLIC_FOLDER = "public"

GROUND_TRUTH = ["a1.mp3","a2.mp3","a3.mp3"]

def test_all_files():
    files = [f for f in os.listdir(PUBLIC_FOLDER) if f.lower().endswith((".wav",".mp3"))]
    
    for file in files:
        audio_path = os.path.join(PUBLIC_FOLDER,file)
        
        print(f"Testing file : {file} | Expected")
        results = runAll(audio_path)
        
        for r in results:
            print(r)
            
            
if __name__ == "__main__":
    test_all_files()