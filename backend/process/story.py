from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
import dotenv
import os

dotenv.load_dotenv()
HF_TOKEN = os.getenv("HP_TOKEN")


class StoryGenerator:
    def __init__(self):
        prompt_template = ChatPromptTemplate.from_messages([
            (
            "system",
            "You are a helpful assistant that writes a short, emotional poem based on an image caption. "
            "The poem must reflect all emotions conveyed in the image described by the caption."
        ),
        (
            "human",
            "Write the poem using the following image caption: {caption}"
        ),
        ])
        
        llm = HuggingFaceEndpoint(
            repo_id="meta-llama/Llama-3.1-8B-Instruct",
            huggingfacehub_api_token=HF_TOKEN,
            temperature=0.6,
            max_new_tokens=650
        )
        
        chat = ChatHuggingFace(llm=llm)
        
        self.storyChain = prompt_template | chat | StrOutputParser()
        
        
    def generate_story(self, caption: str):
        story = self.storyChain.invoke({"caption": caption})
        return story