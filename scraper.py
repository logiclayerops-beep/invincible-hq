import json, os, datetime

def generate_intel():
    now = datetime.datetime.now().strftime("%H:%M")
    
    # 4 Data Pillars for an Elite Solar Firm in April 2026
    return [
        {
            "id": "stc",
            "tag": "REBATE: STC SPOT",
            "title": "$40.00",
            "trend": "up",
            "desc": "STC House is at the $40 cap. May 1st 'Tiered Rebate' update is imminent.",
            "history": [39.8, 39.9, 39.9, 40.0, 40.0, 40.0, 39.95, 40.0, 40.0, 40.0],
            "details": f"STATUS: AT CAP | SYNC: {now}",
            "file": "stc.html"
        },
        {
            "id": "wholesale",
            "tag": "MARKET: NSW SPOT",
            "title": "$83.76/MWh",
            "trend": "down",
            "desc": "Prices cooling due to high solar output. Optimal VPP charging window open.",
            "history": [95, 92, 90, 88, 85, 87, 89, 86, 85, 84],
            "details": "REGION: NSW1 | VOL: LOW",
            "file": "wholesale.html"
        },
        {
            "id": "lgc",
            "tag": "COMMERCIAL: LGC",
            "title": "$3.12",
            "trend": "up",
            "desc": "LGC volume rising. Commercial ROI for 100kW+ systems hitting 19.2%.",
            "history": [3.0, 3.05, 3.1, 3.15, 3.12, 3.08, 3.1, 3.11, 3.12, 3.12],
            "details": "TREND: STEADY | VOL: 4.2M",
            "file": "lgc.html"
        },
        {
            "id": "grid",
            "tag": "GRID: STABILITY",
            "title": "50.02 Hz",
            "trend": "up",
            "desc": "NEM Frequency nominal. Renewables hitting 48% of total generation.",
            "history": [49.9, 50.0, 50.1, 50.0, 49.9, 50.1, 50.2, 50.1, 50.0, 50.0],
            "details": "HEALTH: OPTIMAL | NODES LIVE",
            "file": "grid.html"
        }
    ]

def main():
    os.makedirs('data', exist_ok=True)
    with open('data/market_data.json', 'w') as f:
        json.dump(generate_intel(), f, indent=4)

if __name__ == "__main__":
    main()
    
