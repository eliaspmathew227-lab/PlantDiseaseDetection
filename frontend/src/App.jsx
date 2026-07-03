import React from "react";
import { Camera, CheckCircle2, ImageUp, Loader2, RefreshCcw, ShieldCheck } from "lucide-react";
import { useMemo, useState } from "react";
import { predictDisease } from "./api";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState("");
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const confidenceLabel = useMemo(() => {
    if (!prediction) return "";
    return `${Number(prediction.confidence).toFixed(1)}% confidence`;
  }, [prediction]);

  function handleFileChange(event) {
    const file = event.target.files?.[0];
    if (!file) return;

    setSelectedFile(file);
    setPreviewUrl(URL.createObjectURL(file));
    setPrediction(null);
    setError("");
  }

  async function handlePredict() {
    if (!selectedFile) {
      setError("Choose a tomato leaf image first.");
      return;
    }

    setIsLoading(true);
    setError("");

    try {
      const result = await predictDisease(selectedFile);
      setPrediction(result);
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setIsLoading(false);
    }
  }

  function resetFlow() {
    setSelectedFile(null);
    setPreviewUrl("");
    setPrediction(null);
    setError("");
  }

  return (
    <main className="app-shell">
      <section className="workspace">
        <div className="intro">
          <span className="eyebrow">Smart crop monitoring</span>
          <h1>Tomato Disease Detector</h1>
          <p>
            Upload a tomato leaf image to identify common diseases and receive practical prevention guidance.
          </p>
        </div>

        <div className="tool-layout">
          <section className="upload-panel" aria-label="Image upload">
            <div className="preview-box">
              {previewUrl ? (
                <img src={previewUrl} alt="Selected tomato leaf" />
              ) : (
                <div className="empty-preview">
                  <ImageUp size={44} />
                  <span>Leaf image preview</span>
                </div>
              )}
            </div>

            <div className="controls">
              <label className="file-button">
                <Camera size={18} />
                Choose image
                <input accept="image/png,image/jpeg,image/webp" type="file" onChange={handleFileChange} />
              </label>

              <button className="primary-button" type="button" onClick={handlePredict} disabled={isLoading}>
                {isLoading ? <Loader2 className="spin" size={18} /> : <ShieldCheck size={18} />}
                {isLoading ? "Analyzing..." : "Analyze leaf"}
              </button>

              <button className="ghost-button" type="button" onClick={resetFlow}>
                <RefreshCcw size={17} />
                Reset
              </button>
            </div>

            {selectedFile && <p className="file-name">{selectedFile.name}</p>}
            {error && <p className="error-message">{error}</p>}
          </section>

          <section className="result-panel" aria-label="Prediction result">
            {prediction ? (
              <>
                <div className="result-header">
                  <CheckCircle2 size={26} />
                  <div>
                    <span>Prediction</span>
                    <h2>{prediction.prediction}</h2>
                    <p>{confidenceLabel}</p>
                  </div>
                </div>

                {prediction.model_mode === "mock" && (
                  <p className="mock-note">
                    MVP mode: using a deterministic mock predictor until a trained CNN model is added.
                  </p>
                )}

                <InfoBlock title="About" items={[prediction.description]} />
                <InfoBlock title="Symptoms" items={prediction.symptoms} />
                <InfoBlock title="Prevention" items={prediction.prevention} />
                <InfoBlock title="Treatment" items={prediction.treatment} />
                <p className="expert-note">{prediction.consult_expert}</p>
              </>
            ) : (
              <div className="empty-result">
                <ShieldCheck size={42} />
                <h2>Results will appear here</h2>
                <p>Disease name, confidence score, symptoms, and farmer-friendly actions are shown after analysis.</p>
              </div>
            )}
          </section>
        </div>
      </section>
    </main>
  );
}

function InfoBlock({ title, items }) {
  const safeItems = Array.isArray(items) ? items : [items].filter(Boolean);

  if (safeItems.length === 0) return null;

  return (
    <section className="info-block">
      <h3>{title}</h3>
      <ul>
        {safeItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}

export default App;
