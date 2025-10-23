import requests
from bs4 import BeautifulSoup

URL = "https://www.indiatoday.in/"
HEADLINES_FILE = "headlines.txt"

def fetch_headlines():
    try:
        # Send GET request
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
        
        # Check HTTP status
        if response.status_code != 200:
            print("⚠️ Failed to retrieve webpage")
            return []
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # IndiaToday uses h2 tags with story titles
        headlines = soup.find_all("h2")
        
        extracted = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]
        return extracted[:20]  # Get top 20 headlines
    
    except Exception as e:
        print("Error:", e)
        return []

def save_headlines(headlines):
    with open(HEADLINES_FILE, "w", encoding="utf-8") as file:
        for i, hl in enumerate(headlines, 1):
            file.write(f"{i}. {hl}\n")
    print("✅ Headlines saved to headlines.txt!")

def main():
    print("Fetching India news headlines...")
    headlines = fetch_headlines()
    
    if headlines:
        save_headlines(headlines)
        print("📰 Top India headlines scraped successfully!")
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
