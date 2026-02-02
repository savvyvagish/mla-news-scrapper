import csv
import os
import time
from news import fetch_news
from analyzer import process_articles
from export import export_excel

print("🚀 Starting MLA Scraper Analysis Pipeline...")

all_rows = []

try:
    with open("mlas.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        mlas = list(reader)
        total_mlas = len(mlas)
        print(f"📖 Loaded {total_mlas} MLAs from file. Processing ALL rows...")

        for i, mla_data in enumerate(mlas, 1):
            # Map CSV headers to internal keys
            mla = {
                "name": mla_data.get("MLA Name") or mla_data.get("name"),
                "state": mla_data.get("State") or mla_data.get("state"),
                "party": mla_data.get("Party") or mla_data.get("party"),
                "constituency": mla_data.get("Constituency") or mla_data.get("constituency")
            }
            
            if not mla["name"]:
                print(f"⏩ Skipping row {i} due to missing name.")
                continue

            print(f"\n[{i}/{total_mlas}] Processing: {mla['name']} ({mla['state']})")
            query = f"{mla['name']} {mla['state']} news"
            
            articles = fetch_news(query)
            rows = process_articles(mla, articles)
            
            print(f"➕ Appending {len(rows)} results to the master list.")
            all_rows.extend(rows)
            
            # Save progress every 10 MLAs
            if i % 10 == 0:
                print(f"💾 Periodic save at {i}/{total_mlas}...")
                export_excel(all_rows)
            
            # Delay to respect GNews free tier (approx 1 request per sec)
            time.sleep(1.1)

except Exception as e:
    print(f"❌ Critical Error in pipeline: {e}")
    import traceback
    traceback.print_exc()

if all_rows:
    print(f"\n💾 Generating final report with {len(all_rows)} rows...")
    export_excel(all_rows)
    print("✅ MLA report generated: output.xlsx")
else:
    print("\n⚠️ No data found to export. Check your CSV headers and API keys.")
    export_excel([])