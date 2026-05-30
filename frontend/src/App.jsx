import { useState, useRef } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [imgFile, setImgFile] = useState(null)
  const [audioUrl, setAudioUrl] = useState(null)
  const [loading, setLoading] = useState(false)
  const audioRef = useRef(null)

  const generateStory = async (e) => {
    e.preventDefault()
    if (!imgFile) {
      alert("Please upload an image first.")
      return
    }

    setLoading(true)
    setAudioUrl(null)

    const formData = new FormData()
    formData.append('imgFile', imgFile)

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/generate-story', 
        formData,
        {
          responseType: 'blob', 
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      )

      if (response.status === 200) {
        const blob = new Blob([response.data], { type: 'audio/wav' })
        const url = URL.createObjectURL(blob)
        setAudioUrl(url)
      } else {
        console.error("Failed to generate story:", response.statusText)
        alert("Failed to generate audio story.")
      }
    } catch (error) {
      console.error("Error generating story:", error)
      alert("Error connecting to backend.")
    } finally {
      setLoading(false)
    }
  }

  return (
    // ADDED: Container to wrap the content layout
    <div className="app-container">
      <section className="hero-section">
        <h2>Welcome to the Story Creator</h2>
        <p>Upload an image to generate and hear an immersive AI story.</p>
      </section>

      <section className="upload-section">
        <h2>Upload your image</h2>
        <label className="file-upload-label">
          <span>{imgFile ? imgFile.name : "Choose an image file..."}</span>
          <input 
            type="file" 
            accept="image/*"
            onChange={(e) => setImgFile(e.target.files[0])} 
          />
        </label>
      </section>

      <section className="action-section">
        <button onClick={generateStory} disabled={loading} className="submit-btn">
          {loading ? (
            <>
              <span className="loading-spinner"></span>
              Generating Story...
            </>
          ) : "Generate & Play Story"}
        </button>
      </section>

      {audioUrl && (
        <section className="audio-section">
          <h2>Generated Story Audio</h2>
          <audio ref={audioRef} controls src={audioUrl}>
            Your browser does not support the audio element.
          </audio>
        </section>
      )}
    </div>
  )
}

export default App