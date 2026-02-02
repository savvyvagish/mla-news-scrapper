MLA News Scraper

A Python tool to fetch and analyze news articles about Indian MLAs using Google News RSS and Google Gemini.

It pulls relevant news, checks if the article actually matches the MLA (no name collisions), categorizes it, and spits everything into an Excel file.

What it does
	•	Reads MLAs from mlas.csv
	•	Fetches India-specific news from Google News RSS
	•	Uses Gemini AI to:
	•	Verify MLA relevance
	•	Categorize the article (criminal, allegations, assets, neutral, etc.)
	•	Generate a 1-line factual summary
	•	Saves results to output.xlsx
	•	Periodically saves progress so nothing breaks midway

Requirements
	•	Python 3.8+
	•	Google Gemini API key

Setup

Clone the repo:
git clone https://github.com/savvyvagish/mla-news-scrapper.git
cd mla-news-scrapper

Install dependencies:
pip install requests google-genai pandas openpyxl python-dotenv

Create a .env file:
GEMINI_API_KEY=your_api_key_here

Usage

Make sure mlas.csv exists with columns like:
	•	name
	•	state
	•	party

Run:
python3 main.py

Results will be saved in output.xlsx.

Files
	•	main.py – runs everything
	•	news.py – Google News RSS fetching
	•	analyzer.py – Gemini analysis logic
	•	gemini.py – Gemini client setup
	•	export.py – Excel export
	•	mlas.csv – input data

Note

This relies on public news + AI. Double-check anything important.
