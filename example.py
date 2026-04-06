import requests
import json

def scrape_dynamic_website(target_url, rapidapi_key):
    # Get your FREE API key here: https://rapidapi.com/titavares33/api/ultimate-web-scraper
    api_url = "https://ultimate-web-scraper.p.rapidapi.com/api/v1/extract"
    
    headers = {
        "x-rapidapi-host": "ultimate-web-scraper.p.rapidapi.com",
        "x-rapidapi-key": rapidapi_key,
        "Content-Type": "application/json"
    }
    
    # You can also pass "wait_for_selector" to wait for specific elements to load
    payload = {
        "url": target_url,
        "use_proxy": False,
        "timeout_ms": 30000
    }
    
    print(f"Scraping fully rendered HTML from: {target_url}...")
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Scraping Successful!")
        print(f"Page Title: {data.get('title')}")
        
        # Salvando o HTML completo renderizado
        with open("rendered_page.html", "w", encoding="utf-8") as f:
            f.write(data.get('html'))
        print("Raw HTML saved as 'rendered_page.html'. Open it in your browser!")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

# --- Usage Example ---
API_KEY = "YOUR_RAPIDAPI_KEY" # Replace with your RapidAPI key
TARGET_URL = "https://quotes.toscrape.com/js/" # A JS-rendered test site

scrape_dynamic_website(TARGET_URL, API_KEY)
