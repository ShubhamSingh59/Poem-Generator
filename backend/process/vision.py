from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

class VisionProcessor:
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
        
    def generate_caption(self, image: Image.Image):
        inputs = self.processor(image, return_tensors="pt")
        out = self.model.generate(**inputs, max_new_tokens=150)
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption