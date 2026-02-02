import json
from gemini import analyze_article

def safe_parse_json(text):
    """
    Tries to extract JSON even if Gemini adds extra text.
    """
    if not text:
        return None
    try:
        # Try finding JSON block
        start = text.find("{")
        end = text.rfind("}") + 1
        if start != -1 and end != 0:
            return json.loads(text[start:end])
        return None
    except Exception as e:
        print(f"⚠️ JSON Parse Error: {e}")
        return None

def process_articles(mla, articles):
    results = []
    
    if not articles:
        print(f"⚠️ No articles to process for {mla['name']}")
        # Ensure at least one diagnostic row if no articles found
        results.append({
            "Name": mla["name"],
            "State": mla["state"],
            "Party": mla["party"],
            "Source": "N/A",
            "Category": "NO_ARTICLES_FOUND",
            "Summary": f"No news articles were found for this query."
        })
        return results

    for a in articles:
        article = {
            "title": a.get("title", "No Title"),
            "description": a.get("description", ""),
            "source": a.get("source", {}).get("name", "Unknown")
        }

        print(f"🧪 Analyzing article: {article['title'][:50]}...")
        raw = analyze_article(mla, article)
        
        # Debug: see what Gemini actually returns
        print(f"--- Gemini Result for {mla['name']} ---")
        print(raw)
        print("---------------------------------------")

        parsed = safe_parse_json(raw)

        if not parsed:
            # Drop into results even if parsing fails - keep the raw data!
            results.append({
                "Name": mla["name"],
                "State": mla["state"],
                "Party": mla["party"],
                "Source": article["source"],
                "Category": "PARSE_ERROR",
                "Summary": raw[:500] if raw else "Empty response from Gemini"
            })
            continue

        # Check for 'match' but don't strictly discard unless we really want to
        # Simplfying strict filters as requested
        match_val = parsed.get("match")
        category = parsed.get("category", "UNKNOWN")
        summary = parsed.get("summary", "")

        # If it's a mismatch, we still include it but label it
        if match_val is False:
            category = f"[MISMATCH] {category}"

        results.append({
            "Name": mla["name"],
            "State": mla["state"],
            "Party": mla["party"],
            "Source": article["source"],
            "Category": category,
            "Summary": summary
        })

    print(f"✅ Processed {len(results)} rows for {mla['name']}")
    return results