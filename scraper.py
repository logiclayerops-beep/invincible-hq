def generate_market_data():
    now = datetime.datetime.now().strftime("%H:%M")
    
    intel = [
        {
            "tag": "FINANCIAL: STC",
            "title": "STC Spot: $39.65",
            "desc": "The residential rebate index is holding steady. No immediate price risk for current quotes.",
            "details": f"Market Status: LIQUID | Verified: {now}",
            "url": "https://cer.gov.au/"
        },
        {
            "tag": "OPS: WHOLESALE",
            "title": "NSW Spot: $83.76/MWh",
            "desc": "Wholesale rates are 7% lower than 2025. Good window for battery charging cycles.",
            "details": "Region: NSW1 | Trend: DECREASING",
            "url": "https://aemo.com.au/"
        },
        {
            "tag": "COMMERCIAL: LGC",
            "title": "LGC Spot: $3.10",
            "desc": "Large-scale certificates facing oversupply. Commercial ROI remains strong but margins are tightening.",
            "details": "Weekly Range: $3.05 - $3.50",
            "url": "https://coremarkets.co/"
        },
        {
            "tag": "GRID: STABILITY",
            "title": "Freq: 50.01 Hz",
            "desc": "NEM Grid is healthy. Renewable penetration reached 46.4% this month.",
            "details": "Status: NORMAL | VPP Nodes Standby",
            "url": "https://open-nem.org/"
        }
    ]
    return intel
    
    
