def generate_heatmap_data(chunks, analysis):
    heatmap = []

    for i, chunk in enumerate(chunks):
        score = (
            analysis["chunks"][i]["genericity"] * 0.4 +
            analysis["chunks"][i]["style"] * 0.3 +
            (1 / analysis["chunks"][i]["perplexity"]) * 0.3
        )

        heatmap.append({
            "text": chunk,
            "risk": round(score, 3)
        })

    return heatmap
