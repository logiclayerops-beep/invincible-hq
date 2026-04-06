import json
import os
import datetime

def generate_market_data():
    now = datetime.datetime.now().strftime("%H:%M")
    
    # We need EXACTLY 4 items in this list for 4 boxes
    intel = [
        {
            "tag": "FINANCIAL: STC",
            "title": "STC Spot: $39.65",
            "desc": "Residential rebate index is stable. No immediate price risk for customer quotes.",
            "details": f"Market Status: LIQUID | Sync: {now}",
            "url": "https://www.cleanenergyregulator.gov.au/"
        },
        {
            "tag": "OPS: WHOLESALE",
            "title": "NSW Spot: $83.76/MWh",
            "desc": "Wholesale rates are slightly lower. Ideal window for battery charging cycles.",
            "details": "Region: NSW1 | Trend: STABLE",
            "url": "https://aemo.com.au/"
        },
        {
            "tag": "COMMERCIAL: LGC",
            "title": "LGC Spot: $3.10",
            "desc": "Large-scale certificates facing oversupply. Commercial margins remains strong.",
            "details": "Weekly Range: $3.05 - $3.50",
            "url": "https://coremarkets.co/"
        },
        {
            "tag": "GRID: STABILITY",
            "title": "Freq: 50.01 Hz",
            "desc": "NEM Grid is healthy. Renewable penetration reached 46% this month.",
            "details": "Status: NORMAL | VPP Nodes Standby",
            "url": "https://open-nem.org/"
        }
    ]
    return intel

def main():
    os.makedirs('data', exist_ok=True)
    data = generate_market_data()
    with open('data/market_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Success: {len(data)} cards generated.")

if __name__ == "__main__":
    main()
    
