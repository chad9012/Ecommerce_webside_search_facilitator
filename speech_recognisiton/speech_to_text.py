import openai
openai.api_key="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"

audio_path="test_audio/1_to_6.mp3"

audio_file=open(audio_path,"rb")
response=openai.Audio.transcribe("whisper-1",audio_file)
print(response)