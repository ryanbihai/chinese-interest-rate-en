#!/usr/bin/env python3
"""
Chinese Interest Rate Monitor - Rate Check Script (English Version)
Track China's interest rate data, compare with history, notify on changes
"""

import json
import sys
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/rates.json')

def load_current_rates():
    """Load current rate data from file"""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_rates(data):
    """Save rate data to file"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def parse_rates_from_search(search_results):
    """
    Parse rate values from web_search results
    Returns extracted rate dictionary
    """
    rates = {}
    text = ' '.join(search_results).lower() if isinstance(search_results, list) else search_results.lower()
    
    # LPR parsing (e.g., "1-year LPR 3.45%" or "LPR 1-year 3.45%")
    lpr_patterns = [
        r'1[- ]?year[l ]?lpr[:\s]*(\d+\.?\d*)%',
        r'lpr.*1[- ]?year[:\s]*(\d+\.?\d*)%',
        r'(\d+\.?\d*)%.*1[- ]?year.*lpr',
    ]
    for pattern in lpr_patterns:
        import re
        m = re.search(pattern, text)
        if m:
            rates['LPR_1Y'] = m.group(1)
            break
    
    # 5-year LPR
    lpr5_patterns = [
        r'5[- ]?year.*lpr[:\s]*(\d+\.?\d*)%',
        r'lpr.*5[- ]?year[:\s]*(\d+\.?\d*)%',
    ]
    for pattern in lpr5_patterns:
        import re
        m = re.search(pattern, text)
        if m:
            rates['LPR_5Y'] = m.group(1)
            break
    
    # Deposit base rates
    deposit_patterns = [
        r'1[- ]?year.*deposit.*?[:\s]*(\d+\.?\d*)%',
        r'(\d+\.?\d*)%.*1[- ]?year.*deposit',
    ]
    for pattern in deposit_patterns:
        import re
        m = re.search(pattern, text)
        if m:
            rates['deposit_1Y'] = m.group(1)
            break
    
    # Government bond yield 10-year
    bond10_patterns = [
        r'10[- ]?year.*bond.*?yield[:\s]*(\d+\.?\d*)%',
        r'10[- ]?year.*yield[:\s]*(\d+\.?\d*)%',
    ]
    for pattern in bond10_patterns:
        import re
        m = re.search(pattern, text)
        if m:
            rates['bond_10Y'] = m.group(1)
            break
    
    return rates

def compare_rates(old_data, new_rates):
    """Compare old data with new data, return changes"""
    changes = []
    categories = {
        'depositRates': 'deposit',
        'LPR': 'LPR',
        'bondYields': 'bond',
        'SHIBOR': 'SHIBOR',
        'mortgageLPR': 'mortgage',
        'OMO': 'OMO',
        'RRR': 'RRR'
    }
    
    for category, prefix in categories.items():
        if category not in old_data:
            old_data[category] = {}
        if category not in new_rates:
            new_rates[category] = {}
        
        for key in set(list(old_data[category].keys()) + list(new_rates.get(category, {}).keys())):
            old_val = old_data[category].get(key, '')
            new_val = new_rates.get(category, {}).get(key, '')
            
            if old_val and new_val and old_val != new_val:
                try:
                    old_num = float(old_val)
                    new_num = float(new_val)
                    diff = new_num - old_num
                    diff_bp = round(diff * 100, 1)  # Convert to basis points
                    changes.append({
                        'category': category,
                        'key': key,
                        'old': old_val,
                        'new': new_val,
                        'diff': f"{diff:+.2f}% ({diff_bp:+.0f}bp)"
                    })
                except:
                    pass
    
    return changes

def format_notification(changes, new_data):
    """Format notification message"""
    today = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    msg = f"📊 China Interest Rate Daily Report | {today}\n\n"
    
    # Group by category
    by_category = {}
    for c in changes:
        cat = c['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(c)
    
    # Deposit rates
    if 'depositRates' in by_category:
        msg += "🏦 Bank Deposit Rates (Base)\n"
        for c in by_category['depositRates']:
            label = {'1year': '1Y', '3year': '3Y', '5year': '5Y'}.get(c['key'], c['key'])
            msg += f"- {label}: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    # LPR
    if 'LPR' in by_category:
        msg += "📊 LPR Loan Prime Rate\n"
        for c in by_category['LPR']:
            label = {'1year': '1Y', '5yearPlus': '5Y+'}.get(c['key'], c['key'])
            msg += f"- {label}: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    # Government bonds
    if 'bondYields' in by_category:
        msg += "📉 Government Bond Yields\n"
        for c in by_category['bondYields']:
            label = {'1year': '1Y', '3year': '3Y', '10year': '10Y'}.get(c['key'], c['key'])
            msg += f"- {label}: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    # SHIBOR
    if 'SHIBOR' in by_category:
        msg += "💧 SHIBOR Interbank Offered Rates\n"
        for c in by_category['SHIBOR']:
            label = {'ON': 'O/N', '1W': '1W', '1M': '1M', '3M': '3M'}.get(c['key'], c['key'])
            msg += f"- {label}: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    # Mortgage
    if 'mortgageLPR' in by_category:
        msg += "🏠 Mortgage Rates\n"
        for c in by_category['mortgageLPR']:
            msg += f"- 5Y+ LPR: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    # Open market operations
    if 'OMO' in by_category:
        msg += "🔄 Open Market Operation Rates\n"
        for c in by_category['OMO']:
            label = {'repo7d': '7D Repo', 'repo14d': '14D Repo', 'MLF1Y': 'MLF 1Y'}.get(c['key'], c['key'])
            msg += f"- {label}: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    # RRR
    if 'RRR' in by_category:
        msg += "💰 Reserve Requirement Ratio\n"
        for c in by_category['RRR']:
            label = {'large': 'Large Institutions', 'small': 'Small Institutions'}.get(c['key'], c['key'])
            msg += f"- {label}: {c['new']}% ({c['diff']})\n"
        msg += "\n"
    
    msg += "---\n"
    msg += "Data Sources: People's Bank of China, National Interbank Lending Center, China Bond Information Network\n"
    
    return msg

def main():
    """
    Main flow:
    1. Load historical data
    2. Receive new rate data (via command line argument)
    3. Compare changes
    4. Output notification if changed
    5. Update data file
    """
    old_data = load_current_rates()
    
    # Get new data from command line arguments (JSON format)
    if len(sys.argv) > 1:
        try:
            new_data = json.loads(sys.argv[1])
        except:
            print("Error: Invalid JSON input")
            sys.exit(1)
    else:
        # No argument: use last saved data as "new data" (demo mode)
        new_data = old_data.copy()
        new_data['updateDate'] = datetime.now().strftime('%Y-%m-%d')
    
    # Compare changes
    changes = compare_rates(old_data, new_data)
    
    # Output notification if changed
    if changes:
        notification = format_notification(changes, new_data)
        print("[NOTIFY]")
        print(notification)
        print("[/NOTIFY]")
    
    # Update data file
    new_data['updateDate'] = datetime.now().strftime('%Y-%m-%d')
    save_rates(new_data)
    
    if not changes:
        print("[OK] No changes detected. Data updated.")
    else:
        print(f"[OK] {len(changes)} rate(s) changed. Data updated.")

if __name__ == '__main__':
    main()
