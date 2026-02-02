# MLA News Scraper

A Python script to fetch and analyze news articles about Indian MLAs.

It pulls news from Google News RSS, verifies if the article is actually about the MLA, categorizes it using Gemini AI, and exports everything to an Excel file.

What it does
- Reads MLAs from mlas.csv
- Fetches India-specific news via Google News RSS
- Uses Gemini AI to verify relevance, categorize news, and generate a 1-line summary
- Saves results to output.xlsx
- Auto-saves progress to avoid data loss

Requirements
- Python 3.8+
- Google Gemini API key

Setup & Run

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/savvyvagish/mla-news-scrapper.git
    cd mla-news-scrapper
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, install manually: `pip install requests google-genai pandas openpyxl python-dotenv`)*

3.  **Configure API Key**:
    *   Create a `.env` file in the root directory.
    *   Add your Google Gemini API key:
        ```bash
        GEMINI_API_KEY=your_api_key_here
        ```


Run the script:
python3 main.py

Input
mlas.csv should contain columns like:
- name
- state
- party

Output
Results are saved in output.xlsx

Project Structure
main.py        - runs the pipeline
news.py        - Google News RSS fetching
analyzer.py    - Gemini analysis
gemini.py      - Gemini client setup
export.py      - Excel export
mlas.csv       - input data

Disclaimer
This tool uses public news sources and AI.
AI can be wrong. Verify important info manually.
