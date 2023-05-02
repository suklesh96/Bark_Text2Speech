from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
import uvicorn
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/text_to_speech/{user_input}")
async def gen_audio(user_input:str):

    # download and load all models
    preload_models(force_reload=True)

    # generate audio from text
    text_prompt = """{user_input}"""
    audio_array = generate_audio(text_prompt)

    # play text in notebook
    return Audio(audio_array, rate=SAMPLE_RATE)

port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=port)