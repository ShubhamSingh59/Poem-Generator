# 🎙️ AI Multimodal Storyteller (Image-to-Speech)

A full-stack, multimodal AI application that transforms uploaded images into spoken-word stories and poems. 

This project stitches together three distinct AI models (Computer Vision, Large Language Models, and Text-to-Speech) into a seamless, in-memory pipeline using FastAPI and React.

## ✨ How It Works
The pipeline executes entirely in RAM without ever saving files to the hard drive:
1. **The Eyes (Vision):** The React frontend sends an image to the FastAPI backend, where Salesforce's **BLIP** model analyzes the image and generates a text caption.
2. **The Brain (Story):** The caption is passed through a **LangChain** pipeline to **Llama-3.1 (8B)** via the Hugging Face API, which writes an emotional, contextual poem based on the visual scene.
3. **The Voice (Audio):** The poem is fed into a local instance of Meta's **MMS-TTS** model. The raw mathematical waveforms are converted into a virtual `.wav` file in RAM and streamed directly back to the native HTML5 audio player in the browser.

---

## 🛠️ Tech Stack
**Backend:**
* [FastAPI](https://fastapi.tiangolo.com/) - High-performance web server.
* [Transformers](https://huggingface.co/docs/transformers/index) - AI model execution.
* [LangChain](https://www.langchain.com/) - LLM orchestration and prompt templating.
* `soundfile` & `io.BytesIO` - In-memory audio processing.

**Frontend:**
* [React](https://react.dev/) (Vite) - Component-based UI.
* [Axios](https://axios-http.com/) - Blob/Form-Data network requests.
* CSS - Custom, responsive dark-mode styling.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Node.js & npm
* A [Hugging Face](https://huggingface.co/) API token (for the Llama 3.1 inference).

### 1. Backend Setup
Navigate to the backend directory and create a virtual environment:

```bash
cd backend
python -m venv myenv

# Windows
myenv\Scripts\activate
# Mac/Linux
source myenv/bin/activate
