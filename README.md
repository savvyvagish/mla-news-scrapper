# MLA News Scraper & Intelligent Analyzer

This tool automates the process of fetching and analyzing news articles for Indian Members of Legislative Assembly (MLAs). It utilizes **Google News RSS** for fetching high-quality, localized news and **Google Gemini AI** (Generative AI) to intelligently analyze, categorize, and summarize the articles.

## 🚀 Features

*   **Bulk Processing**: Reads a list of MLAs from a CSV file (`mlas.csv`).
*   **Localized News Fetching**: Uses Google News RSS tailored for India (`gl=IN`, `hl=en-IN`) to find relevant articles.
*   **AI-Powered Analysis**:
    *   Verifies if the article matches the specific MLA (filters out name collisions).
    *   Categorizes news into:
        *   Criminal Cases (Pending/Convicted/Acquitted)
        *   Allegations / Controversies
        *   Asset / Election Info
        *   Neutral / Irrelevant
    *   Generates a concise 1-line factual summary.
*   **Excel Export**: Saves the final report to `output.xlsx`, periodically saving progress to avoid data loss.
*   **Rate Limiting**: Includes delays to respect Google News rate limits.

## 🛠️ Prerequisites

*   Python 3.8+
*   A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/))

## 📦 Installation

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

## 📋 Usage

1.  **Prepare Input**: Ensure `mlas.csv` is in the root directory. It must contain at least the following headers (or similar):
    *   `MLA Name` or `name`
    *   `State` or `state`
    *   `Party` or `party`

2.  **Run the Scraper**:
    ```bash
    python3 main.py
    ```

3.  **View Results**: The script will generate `output.xlsx` containing the analyzed news data.

## 📂 Project Structure

*   `main.py`: Orchestrates the entire pipeline (loading CSV, fetching news, analyzing, saving).
*   `news.py`: Handles fetching news from Google News RSS.
*   `analyzer.py`: Manages the interaction with Gemini AI and parsing the JSON response.
*   `gemini.py`: Configures the Gemini AI client.
*   `export.py`: Handles exporting the results to Excel.
*   `mlas.csv`: Input file containing MLA data.

## ⚠️ Disclaimer

This tool uses public news sources and Generative AI. AI models can sometimes hallucinate or misinterpret context. Always verify critical information from primary sources.
