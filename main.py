from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import torchaudio

model_name = "my_stt"
model = Wav2Vec2ForCTC.from_pretrained(model_name)
processor = Wav2Vec2Processor.from_pretrained(model_name)


def generate_stt(audio_path):
    audio, rate = torchaudio.load(audio_path)
    if rate != 16000:
        audio = torchaudio.transforms.Resample(rate, 16000)(audio)

    input_values = processor(audio.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    return transcription



audio_p = "8703.wav"  # Path audio file
print(f"STT Natijasi : {generate_stt(audio_p)}")



# error path : sudo apt-get install sox libsox-dev libsox-fmt-all