import torch
from transformers import AutoTokenizer, AutoModelForTextToWaveform
import io
import soundfile as sf

class AudioTranscriber:
    def __init__(self):
        self.model_id = "facebook/mms-tts-eng"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForTextToWaveform.from_pretrained(self.model_id)
        self.sample_rate = self.model.config.sampling_rate

    def audio_generator(self, story: str) -> bytes:
        inputs = self.tokenizer(story, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(inputs["input_ids"])
            audio = outputs.waveform
            
        audio_data = audio.squeeze().cpu().numpy()
        
        audio_buffer = io.BytesIO()
        sf.write(audio_buffer, audio_data, self.sample_rate, format='WAV')
        
        return audio_buffer.getvalue()
    