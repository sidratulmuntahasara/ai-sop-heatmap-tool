from app.models.perplexity import calculate_perplexity
from app.models.style_deviation import style_score
from app.models.semantic_genericity import genericity_score

def analyze_chunks(chunks):
    results = []
    for c in chunks:
        results.append({
            "perplexity": calculate_perplexity(c),
            "style": style_score(c),
            "genericity": genericity_score(c)
        })

    summary = {
        "avg_perplexity": sum(r["perplexity"] for r in results)/len(results),
        "avg_genericity": sum(r["genericity"] for r in results)/len(results)
    }

    return {"chunks": results, "summary": summary}
