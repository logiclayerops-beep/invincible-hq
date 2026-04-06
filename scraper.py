import json
import os
from datetime import datetime

def generate_market_data():
    # Simulated AI Market Scan for April 2026
    intel = [
        {
            "tag": "MARKET ALERT",
            "title": "Grid Price Surge",
            "desc": "Wholesale rates in NSW/VIC have spiked 12% this morning. AI recommends shifting battery discharge to 6:00 PM peak."
        },
        {
            "tag": "SYSTEM STATUS",
            "title": "VPP Sync Active",
            "desc": "Virtual Power Plant nodes are reporting 98.5% efficiency. All systems go for overnight arbitrage."
        }
    ]
    return intel

def main():
    # Create data directory if missing
    os.makedirs('data', exist_ok=True)
    
    data = generate_market_data()
    
    # Save the file that index.html looks for
    with open('data/market_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("✅ Intel successfully synced to data/market_data.json")

if __name__ == "__main__":
    main()
    

