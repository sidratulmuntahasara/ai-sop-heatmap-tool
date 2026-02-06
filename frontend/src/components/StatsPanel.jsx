export default function StatsPanel({ stats }) {
  return (
    <div className="p-4 bg-gray-100 rounded shadow">
      <h2 className="font-semibold mb-2">AI Contribution Stats</h2>
      <p>Average Perplexity: {stats.avg_perplexity.toFixed(2)}</p>
      <p>Average Genericity: {stats.avg_genericity.toFixed(2)}</p>
    </div>
  );
}
