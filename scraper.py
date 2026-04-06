import json
import os

def generate_market_data():
    intel = [
        {
            "tag": "MARKET ALERT",
            "title": "Grid Price Surge",
            "desc": "Wholesale rates in NSW/VIC have spiked 12% this morning.",
            "details": "High demand in the evening peak is driving prices to $300/MWh. Recommend manual VPP discharge.",
            "url": "https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem"
        },
        {
            "tag": "SYSTEM STATUS",
            "title": "VPP Sync Active",
            "desc": "Virtual Power Plant nodes are reporting 98.5% efficiency.",
            "details": "Sync completed across 450 residential nodes. Arbitrage protocol engaged for midnight charging.",
            "url": "https://invincible.energy/vpp-status"
        }
    ]
    return intel

def main():
    os.makedirs('data', exist_ok=True)
    with open('data/market_data.json', 'w') as f:
        json.dump(generate_market_data(), f, indent=4)

if __name__ == "__main__":
    main()
    
