import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote

def fetch_news(query):
    """
    Fetches high-quality localized Indian news using Google News RSS.
    No API key required. High accuracy for regional Indian sources.
    """
    print(f"🔍 Fetching Indian Local News for: {query}")
    
    # localized for India (gl=IN), English (hl=en-IN)
    encoded_query = quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse XML RSS feed
        root = ET.fromstring(response.content)
        articles = []
        
        # Loop through items in the RSS feed
        for item in root.findall(".//item")[:5]: # Top 5 articles
            title_node = item.find("title")
            link_node = item.find("link")
            source_node = item.find("source")
            
            articles.append({
                "title": title_node.text if title_node is not None else "No Title",
                "link": link_node.text if link_node is not None else "",
                "source": {"name": source_node.text if source_node is not None else "Local Source"},
                "description": "" # RSS results are mostly title-centric
            })
            
        print(f"✅ Found {len(articles)} localized Indian articles.")
        return articles
        
    except Exception as e:
        print(f"❌ Error fetching local news: {e}")
        return []