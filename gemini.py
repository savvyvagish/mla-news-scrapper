import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Do not initialize client globally or it crashes if API key is missing
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    return genai.Client(api_key=api_key)

MODEL = "gemini-2.0-flash" 

def analyze_article(mla, article):
    client = get_client()
    prompt = f"""
You are analyzing PUBLIC information about an Indian MLA.

MLA:
Name: {mla['name']}
State: {mla['state']}
Constituency: {mla['constituency']}
Party: {mla['party']}

News Article:
Title: {article['title']}
Description: {article.get('description','')}
Source: {article['source']}

Tasks:
1. Is this article about THIS MLA? (true/false)
2. Categorize:
   - Criminal Case (Pending)
   - Criminal Case (Convicted)
   - Criminal Case (Acquitted)
   - Allegation / Controversy
   - Asset / Election Info
   - Neutral / Irrelevant
3. Give a 1-line factual summary.

Return STRICT JSON:
{{
  "match": true/false,
  "category": "...",
  "summary": "..."
}}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text