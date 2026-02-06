import { useState } from "react";
import FileUpload from "./components/FileUpload";
import HeatmapViewer from "./components/HeatmapViewer";
import StatsPanel from "./components/StatsPanel";

function App() {
  const [data, setData] = useState(null);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold mb-6">SOP AI Heatmap Tool</h1>
      <FileUpload setData={setData} />
      {data && (
        <div className="mt-6">
          <StatsPanel stats={data.stats} />
          <HeatmapViewer heatmap={data.heatmap} />
        </div>
      )}
    </div>
  );
}

export default App;
