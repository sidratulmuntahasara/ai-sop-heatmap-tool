import axios from "axios";

export default function FileUpload({ setData }) {
  const upload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:8000/analyze-sop", formData);
      setData(res.data);
    } catch (err) {
      console.error("Upload failed:", err);
      alert("Failed to analyze SOP. Make sure backend is running.");
    }
  };

  return (
    <div className="mb-4">
      <input
        type="file"
        accept=".txt"
        onChange={upload}
        className="border p-2 rounded"
      />
    </div>
  );
}
