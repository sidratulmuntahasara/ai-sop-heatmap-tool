export default function HeatmapViewer({ heatmap }) {
  return (
    <div className="mt-4 space-y-2">
      {heatmap.map((h, i) => (
        <p
          key={i}
          className="p-2 rounded"
          style={{
            backgroundColor:
              h.risk > 0.6 ? "#f87171" :  // red = high AI-likelihood
              h.risk > 0.3 ? "#fde047" :  // yellow = medium
              "#86efac"                    // green = low
          }}
        >
          {h.text}
        </p>
      ))}
    </div>
  );
}
