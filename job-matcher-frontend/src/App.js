import { useState } from "react";
import axios from "axios";

function App() {
  const [cvText, setCvText] = useState("");
  const [jobs, setJobs] = useState([]);

  const handleSubmit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/match", {
      cv_text: cvText,
    });

    setJobs(res.data);
  };

  const getColor = (score) => {
    if (score > 70) return "green";
    if (score > 40) return "orange";
    return "red";
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Job Matcher</h1>

      <textarea
        rows="10"
        cols="50"
        value={cvText}
        onChange={(e) => setCvText(e.target.value)}
      />

      <br />

      <button onClick={handleSubmit}>Analyze</button>

      <div>
        {jobs.map((job, index) => (
          <div key={index} style={{ marginTop: "20px" }}>
            <h3>
              {job.title} - {job.company}
            </h3>

            <p style={{ color: getColor(job.score) }}>Score: {job.score}%</p>

            <p>Matched: {job.matched_skills.join(", ")}</p>
            <p>Missing: {job.missing_skills.join(", ")}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
