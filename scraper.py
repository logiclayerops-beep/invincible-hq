import json, os, datetime

def generate_market_data():
    return [
        {
            "tag": "FINANCIAL: STC SPOT",
            "title": "STC Spot: $39.65",
            "trend": "up",
            "risk": 15,
            "desc": "Residential rebate index is stable. No immediate price risk for customer quotes.",
            "file": "stc-details.html"
        },
        {
            "tag": "OPS: WHOLESALE",
            "title": "NSW Spot: $83.76/MWh",
            "trend": "down",
            "risk": 82,
            "desc": "Wholesale rates are slightly lower. Ideal window for battery charging cycles.",
            "file": "wholesale-details.html"
        },
        {
            "tag": "COMMERCIAL: LGC",
            "title": "LGC Spot: $3.10",
            "trend": "down",
            "risk": 90,
            "desc": "Large-scale certificates facing oversupply. Commercial margins remains strong.",
            "file": "lgc-details.html"
        },
        {
            "tag": "GRID: STABILITY",
            "title": "Freq: 50.01 Hz",
            "trend": "up",
            "risk": 10,
            "desc": "NEM Grid is healthy. Renewable penetration reached 48% today.",
            "file": "ops-details.html"
        }
    ]

def main():
    os.makedirs('data', exist_ok=True)
    with open('data/market_data.json', 'w') as f:
        json.dump(generate_market_data(), f, indent=4)

if __name__ == "__main__":
    main()
  
