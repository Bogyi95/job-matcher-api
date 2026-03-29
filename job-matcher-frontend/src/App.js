import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [cvText, setCvText] = useState("");
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    const res = await axios.post("http://127.0.0.1:8000/match", {
      cv_text: cvText,
    });

    setJobs(res.data);
    setLoading(false);
  };

  const getColor = (score) => {
    if (score > 70) return "#22c55e";
    if (score > 40) return "#f59e0b";
    return "#ef4444";
  };

  return (
    <div
      style={{
        fontFamily: "Arial",
        padding: "40px",
        maxWidth: "800px",
        margin: "auto",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Job Matcher</h1>

      {/* CV INPUT */}
      <div style={{ marginBottom: "20px" }}>
        <textarea
          rows="8"
          style={{ width: "100%", padding: "10px", fontSize: "14px" }}
          placeholder="Paste your CV..."
          value={cvText}
          onChange={(e) => setCvText(e.target.value)}
        />
      </div>

      <button
        onClick={handleSubmit}
        style={{
          width: "100%",
          padding: "12px",
          backgroundColor: "#2563eb",
          color: "white",
          border: "none",
          cursor: "pointer",
          fontSize: "16px",
          borderRadius: "8px",
        }}
      >
        Analyze Jobs
      </button>

      {loading && <div className="spinner"></div>}

      {/* JOB LIST */}
      <div style={{ marginTop: "30px" }}>
        {jobs.map((job, index) => (
          <div
            key={index}
            style={{
              border: "1px solid #ddd",
              borderRadius: "10px",
              padding: "20px",
              marginBottom: "20px",
              boxShadow: "0 2px 8px rgba(0,0,0,0.05)",
            }}
          >
            {job.url ? (
              <a href={job.url} target="_blank" rel="noreferrer">
                <h3 style={{ color: "#2563eb", cursor: "pointer" }}>
                  {job.title}
                </h3>
              </a>
            ) : (
              <h3>{job.title}</h3>
            )}

            <p style={{ color: "#555" }}>{job.company}</p>

            {/* SCORE */}
            <div style={{ marginTop: "10px" }}>
              <div
                style={{
                  height: "10px",
                  width: "100%",
                  backgroundColor: "#eee",
                  borderRadius: "5px",
                }}
              >
                <div
                  style={{
                    height: "10px",
                    width: `${job.score}%`,
                    backgroundColor: getColor(job.score),
                    borderRadius: "5px",
                  }}
                />
              </div>

              <p style={{ marginTop: "5px", color: getColor(job.score) }}>
                {job.score}%
              </p>
            </div>

            {/* SKILLS */}
            <div style={{ marginTop: "10px" }}>
              <strong>Matched:</strong> {job.matched_skills.join(", ")}
            </div>

            <div style={{ marginTop: "5px", color: "#ef4444" }}>
              <strong>Missing:</strong> {job.missing_skills.join(", ")}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
