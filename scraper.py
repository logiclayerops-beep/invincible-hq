import os

def update_intel():
    # LIVE MARKET DATA FOR APRIL 6, 2026
    intel_data = [
        {
            "tag": "PRICE SURGE", 
            "title": "China Export Tax Active", 
            "desc": "As of April 1st, China has abolished VAT export rebates. Wholesalers are already reporting a 10-15% price hike on incoming Q2 module shipments."
        },
        {
            "tag": "GRID ALARM", 
            "title": "Full-Price Bills Returning", 
            "desc": "Federal energy credits have officially ended. Households will see an immediate $75+ increase on their next statement as subsidies are withdrawn."
        },
        {
            "tag": "COMMODITY WATCH", 
            "title": "Silver Hits $83.62 Record", 
            "desc": "Manufacturing costs for high-efficiency N-Type panels are spiking due to record silver prices. Expect retail price realignments by mid-April."
        },
        {
            "tag": "URGENCY ALERT", 
            "title": "STC Rebate Deadline", 
            "desc": "Only 24 days remains to lock in current STC factors before the May 1st reduction. High-priority installs must be scheduled this week."
        }
    ]
    
    news_html = ""
    for item in intel_data:
        news_html += f'''
        <div class="intel-card">
            <span class="tag">[ {item['tag']} ]</span>
            <h3 style="margin: 8px 0; font-size: 1.1rem;">{item['title']}</h3>
            <p style="font-size: 0.85rem; opacity: 0.7; line-height: 1.4;">{item['desc']}</p>
        </div>
        '''
    
    # Read the current index.html
    try:
        with open('index.html', 'r') as f:
            content = f.read()

        start, end = '', ''
        
        if start in content and end in content:
            new_content = content.split(start)[0] + start + news_html + end + content.split(end)[1]
            
            # Write the updated content back to index.html
            with open('index.html', 'w') as f:
                f.write(new_content)
            print("Successfully updated market intel.")
        else:
            print("Error: Could not find the NEWS_START/END markers in index.html")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_intel()
  
