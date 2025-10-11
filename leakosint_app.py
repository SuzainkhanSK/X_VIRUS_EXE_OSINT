import streamlit as st
import requests
import time
import json
import pandas as pd
from datetime import datetime
import plotly.express as px
import random
import string

# ================== CONFIGURATION ==================
API_URL = "https://leakosintapi.com/"
API_TOKEN = "7885801908:D216JQbv"
TELEGRAM_USERNAME = "@SuzainkhanSK"
TELEGRAM_CHANNEL = "@SKModTechOfficial"
DEVELOPER_NAME = "𝕏_𝕍𝕀ℝ𝕌𝕊_𝔼𝕏𝔼"
# ===================================================

# Set page config for mobile
st.set_page_config(
    page_title="⚡ 𝕏_𝕍𝕀ℝ𝕌𝕊_𝔼𝕏𝔼",
    page_icon="🔓",
    layout="wide",
    initial_sidebar_state="auto"
)

# Mobile-optimized hacker theme CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Share+Tech+Mono&display=swap');

* {
    font-family: 'Share Tech Mono', monospace;
    box-sizing: border-box;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stApp {
    background: #000000;
    background-image: linear-gradient(180deg, rgba(0, 255, 0, 0.05) 0%, transparent 50%);
    color: #00ff00;
}

.cyber-header {
    background: linear-gradient(135deg, rgba(0, 0, 0, 0.98) 0%, rgba(0, 20, 0, 0.98) 100%);
    border: 2px solid #00ff00;
    padding: 1rem;
    margin-bottom: 1rem;
    text-align: center;
    box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
}

.cyber-title {
    color: #00ff00;
    font-size: clamp(1.5rem, 5vw, 2.5rem);
    font-weight: 900;
    text-shadow: 0 0 10px #00ff00;
    margin: 0.5rem 0;
    line-height: 1.2;
}

.cyber-subtitle {
    color: #00ffff;
    font-size: clamp(0.8rem, 2.5vw, 1rem);
    text-shadow: 0 0 5px #00ffff;
    font-weight: 700;
    margin: 0.5rem 0;
}

.terminal-box {
    background: rgba(0, 0, 0, 0.95);
    border: 2px solid #00ff00;
    border-radius: 8px;
    padding: 1rem;
    margin: 0.5rem 0;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
    position: relative;
}

.terminal-box::before {
    content: ">";
    color: #00ff00;
    position: absolute;
    left: 8px;
    top: 8px;
    font-weight: bold;
    font-size: 0.9rem;
}

.metric-card {
    background: linear-gradient(135deg, rgba(0, 50, 0, 0.9) 0%, rgba(0, 0, 50, 0.9) 100%);
    border: 2px solid #00ff00;
    border-radius: 8px;
    padding: 0.8rem;
    text-align: center;
    transition: transform 0.3s ease;
    margin: 0.25rem 0;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 255, 0, 0.3);
    border-color: #00ffff;
}

.data-row {
    background: rgba(0, 255, 0, 0.1);
    border-left: 3px solid #00ff00;
    padding: 0.8rem;
    margin: 0.5rem 0;
    border-radius: 5px;
    color: #00ff00;
    font-size: 0.95rem;
    font-weight: bold;
    word-break: break-all;
}

.data-row:hover {
    background: rgba(0, 255, 0, 0.2);
    transform: translateX(3px);
}

.stTabs [data-baseweb="tab-list"] {
    background: rgba(0, 0, 0, 0.95);
    border: 2px solid #00ff00;
    border-radius: 8px;
    padding: 0.3rem;
    overflow-x: auto;
    white-space: nowrap;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #00ff00;
    border-radius: 5px;
    padding: 0.5rem 0.8rem;
    font-weight: bold;
    transition: all 0.3s ease;
    text-transform: uppercase;
    font-size: 0.85rem;
    min-width: fit-content;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(0, 255, 0, 0.1);
    color: #00ffff;
    border-color: #00ffff;
}

.stTabs [aria-selected="true"] {
    background: rgba(0, 255, 0, 0.2);
    color: #00ffff;
    border: 1px solid #00ffff;
}

.cyber-button {
    background: linear-gradient(135deg, #00ff00, #00ffff);
    color: #000000;
    border: 2px solid #00ff00;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    font-weight: 900;
    cursor: pointer;
    text-transform: uppercase;
    font-size: 0.9rem;
    width: 100%;
    margin: 0.25rem 0;
}

.cyber-button:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #00ffff, #00ff00);
    box-shadow: 0 5px 15px rgba(0, 255, 0, 0.3);
}

.risk-critical {
    background: linear-gradient(135deg, #ff0000, #ff00ff);
    color: white;
    border: 2px solid #ff0000;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9rem;
}

.risk-high {
    background: linear-gradient(135deg, #ff6600, #ff0000);
    color: white;
    border: 2px solid #ff6600;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9rem;
}

.risk-medium {
    background: linear-gradient(135deg, #ffaa00, #ff6600);
    color: black;
    border: 2px solid #ffaa00;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9rem;
}

.risk-low {
    background: linear-gradient(135deg, #00ff00, #00aa00);
    color: black;
    border: 2px solid #00ff00;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9rem;
}

.cyber-input {
    background: rgba(0, 0, 0, 0.95);
    border: 2px solid #00ff00;
    color: #00ff00;
    padding: 0.8rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: bold;
    width: 100%;
}

.cyber-input:focus {
    border-color: #00ffff;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
    outline: none;
}

.download-btn {
    background: linear-gradient(135deg, #00ff00, #00ffff);
    color: #000000;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    display: inline-block;
    font-weight: 900;
    text-transform: uppercase;
    border: 2px solid #00ff00;
    font-size: 0.9rem;
    width: 100%;
    text-align: center;
    margin: 0.25rem 0;
}

.download-btn:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #00ffff, #00ff00);
    box-shadow: 0 5px 15px rgba(0, 255, 0, 0.3);
}

.telegram-section {
    background: linear-gradient(135deg, rgba(0, 136, 204, 0.95) 0%, rgba(0, 255, 255, 0.95) 100%);
    border: 2px solid #00ffff;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1rem 0;
    text-align: center;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
}

.telegram-section h3 {
    color: #000000;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    font-weight: 900;
}

.telegram-link {
    background: #000000;
    color: #00ffff;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    display: inline-block;
    margin: 0.5rem 0.25rem;
    font-weight: 900;
    text-transform: uppercase;
    border: 2px solid #00ffff;
    font-size: 0.9rem;
}

.telegram-link:hover {
    background: #ffffff;
    color: #0088cc;
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
}

.status-indicator {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-right: 8px;
}

.status-online {
    background: #00ff00;
    box-shadow: 0 0 8px #00ff00;
}

.stTextInput > div > div > input {
    background: rgba(0, 0, 0, 0.95);
    border: 2px solid #00ff00;
    color: #00ff00;
    border-radius: 8px;
    font-size: 1rem;
}

.stTextInput > div > div > input:focus {
    border-color: #00ffff;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
}

.stButton > button {
    background: linear-gradient(135deg, #00ff00, #00ffff);
    color: #000000;
    border: 2px solid #00ff00;
    font-weight: 900;
    text-transform: uppercase;
    border-radius: 8px;
    font-size: 0.9rem;
    padding: 0.8rem;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #00ffff, #00ff00);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 255, 0, 0.3);
}

code {
    background: rgba(0, 0, 0, 0.9);
    border: 1px solid #00ff00;
    color: #00ff00;
    padding: 0.5rem;
    border-radius: 5px;
    font-size: 0.9rem;
    font-weight: bold;
    word-break: break-all;
    display: inline-block;
    width: 100%;
}

.streamlit-expanderHeader {
    background: rgba(0, 50, 0, 0.9);
    border: 2px solid #00ff00;
    border-radius: 8px;
    color: #00ff00;
    font-weight: bold;
    font-size: 0.95rem;
}

.streamlit-expanderContent {
    background: rgba(0, 0, 0, 0.9);
    border: 1px solid #00ff00;
    border-top: none;
    border-radius: 0 0 8px 8px;
}

[data-testid="metric-container"] {
    background: rgba(0, 50, 0, 0.9);
    border: 2px solid #00ff00;
    border-radius: 8px;
    padding: 0.8rem;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
    margin: 0.25rem 0;
}

.stAlert {
    background: rgba(0, 0, 0, 0.95);
    border: 2px solid #00ff00;
    border-radius: 8px;
    margin: 0.5rem 0;
}

.stAlert > div {
    color: #00ff00;
    font-weight: bold;
    font-size: 0.95rem;
}

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.9);
    border: 1px solid #00ff00;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #00ff00, #00ffff);
    border: 1px solid #00ff00;
    border-radius: 4px;
}

@media (max-width: 768px) {
    .cyber-header {
        padding: 0.8rem;
        margin-bottom: 0.8rem;
    }
    .terminal-box {
        padding: 0.8rem;
        margin: 0.3rem 0;
    }
    .metric-card {
        padding: 0.6rem;
        margin: 0.2rem 0;
    }
    .data-row {
        padding: 0.6rem;
        margin: 0.3rem 0;
        font-size: 0.9rem;
    }
    .telegram-section {
        padding: 1rem;
        margin: 0.8rem 0;
    }
    .telegram-link {
        padding: 0.6rem 1rem;
        font-size: 0.85rem;
        margin: 0.3rem 0.1rem;
    }
}

@media (max-width: 480px) {
    .cyber-title {
        font-size: 1.5rem;
    }
    .cyber-subtitle {
        font-size: 0.8rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 0.4rem 0.6rem;
        font-size: 0.75rem;
    }
    .data-row {
        font-size: 0.85rem;
        padding: 0.5rem;
    }
    .terminal-box {
        padding: 0.6rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'current_results' not in st.session_state:
    st.session_state.current_results = None
if 'terminal_lines' not in st.session_state:
    st.session_state.terminal_lines = []

def generate_hacker_id():
    """Generate mobile-friendly hacker ID"""
    prefixes = ["VIRUS", "NEXUS", "MATRIX", "SHADOW"]
    return f"{random.choice(prefixes)}-{random.randint(100, 999)}"

def add_terminal_line(text, color="00ff00"):
    """Add line to terminal output"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.terminal_lines.append(f"[{timestamp}] {text}")
    if len(st.session_state.terminal_lines) > 5:
        st.session_state.terminal_lines.pop(0)

def get_leak_details(query):
    """Mobile-optimized API call"""
    add_terminal_line(f"SCANNING: {query}", "00ffff")
    
    if not API_TOKEN or API_TOKEN == "YOUR_API_KEY_HERE":
        add_terminal_line("ERROR: API TOKEN MISSING", "ff0000")
        return {"error": "❌ API TOKEN NOT CONFIGURED"}

    payload = {
        "token": API_TOKEN,
        "request": query,
        "limit": 100,
        "lang": "en"
    }

    try:
        add_terminal_line("CONNECTING...", "ffff00")
        response = requests.post(API_URL, json=payload, timeout=20)
        add_terminal_line(f"RAW RESPONSE: {response.text[:100]}...", "00ff00")
        response.raise_for_status()
        data = response.json()
        add_terminal_line("SUCCESS", "00ff00")
        return data
    except requests.exceptions.Timeout:
        add_terminal_line("TIMEOUT", "ff0000")
        return {"error": "❌ CONNECTION TIMEOUT"}
    except requests.exceptions.HTTPError as e:
        add_terminal_line(f"ERROR: HTTP {e.response.status_code}", "ff0000")
        return {"error": f"❌ HTTP ERROR: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        add_terminal_line(f"NETWORK ERROR", "ff0000")
        return {"error": f"❌ NETWORK ERROR: {e}"}
    except ValueError:
        add_terminal_line("DATA ERROR", "ff0000")
        return {"error": "❌ DATA CORRUPTION"}
    except Exception as e:
        add_terminal_line(f"SYSTEM ERROR", "ff0000")
        return {"error": f"❌ SYSTEM ERROR: {e}"}

def process_and_format_response(query, api_response, execution_time):
    """Mobile-optimized response processing"""
    add_terminal_line("PROCESSING...", "ffff00")

    if isinstance(api_response, str) or 'error' in api_response:
        return {"error": api_response.get("error", "UNKNOWN ERROR"), "execution_time": f"{execution_time}s"}
    if api_response.get("Error code"):
        return {"error": f"ACCESS DENIED: {api_response['Error code']}", "execution_time": f"{execution_time}s"}
    if api_response.get("Result") == "Not found":
        add_terminal_line("NOT FOUND", "ffaa00")
        return {"result": "TARGET NOT FOUND", "requested_number": query, "execution_time": f"{execution_time}s"}

    unique_items = {
        'telephone': set(), 'address': set(), 'aadhaar': set(), 'passport': set(),
        'email': set(), 'name': set(), 'father_name': set(), 'region': set(),
        'provider': set(), 'ip': set(), 'nickname': set(), 'state': set(),
        'username': set(), 'password': set(), 'dob': set(), 'zip': set(), 'gender': set(),
        'url': set(), 'company': set(), 'job_title': set(), 'website': set(),
        'facebook_id': set(), 'twitter_id': set(), 'blood_type': set(),
        'nationality': set(), 'relationship': set()
    }

    key_map = {
        'telephone': ['phone', 'mobile', 'telephone', 'mobilenumber', 'phone2', 'phone3', 'phone4', 'phone5', 'phone6'],
        'name': ['name', 'fullname', 'owner name', 'full name', 'firstname', 'lastname'],
        'father_name': ['father name', 'fathername'],
        'address': ['address', 'owner address', 'address2', 'address3'],
        'aadhaar': ['aadhaar', 'aadhaar card', 'docnumber'],
        'passport': ['passport'],
        'email': ['email'],
        'region': ['region', 'circle', 'telecom circle', 'mobile state'],
        'provider': ['provider', 'mobileoperator'],
        'ip': ['ip'],
        'nickname': ['nickname'],
        'state': ['indianstate'],
        'username': ['username'],
        'password': ['password'],
        'dob': ['dob', 'bday', 'birthday'],
        'zip': ['zip'],
        'gender': ['gender'],
        'url': ['url'],
        'company': ['company', 'companyname'],
        'job_title': ['jobtitle', 'position'],
        'website': ['website'],
        'facebook_id': ['facebook_id', 'fb_id'],
        'twitter_id': ['twitter_id', 'twitter_username'],
        'blood_type': ['bloodtype'],
        'nationality': ['nationality'],
        'relationship': ['relationship']
    }
    inverted_key_map = {v: k for k, values in key_map.items() for v in values}

    known_providers = {'AIRTEL KARNATKA', 'VI KARNATKA', 'JIO KARNATKA', 'KARNATAKA VI', 'HUTCHISON_3', 'EXELCOMINDO'}

    search_iterations = 0
    mobile_searches = 0
    aadhaar_searches = 0
    passport_searches = 0
    database_details = []

    if "List" in api_response:
        search_iterations = len(api_response["List"])
        add_terminal_line(f"FOUND {search_iterations} DBs", "00ff00")
        for db_name, db_data in api_response["List"].items():
            found_mobile_in_db = False
            found_aadhaar_in_db = False
            found_passport_in_db = False
            info_leak = db_data.get("InfoLeak", "CLASSIFIED")
            num_results = db_data.get("NumOfResults", 0)
            fields_found = set()
            for record in db_data.get("Data", []):
                for key, value in record.items():
                    if not value or not isinstance(value, str):
                        continue
                    normalized_key = inverted_key_map.get(key.lower().strip().replace("_", " "))
                    if normalized_key:
                        fields_found.add(normalized_key)
                        if normalized_key == 'telephone':
                            normalized_value = value.lstrip('+')
                            if normalized_value.isdigit():
                                if len(normalized_value) == 10:
                                    value = f"+91{normalized_value}"
                                elif len(normalized_value) == 12 and normalized_value.startswith('91'):
                                    value = f"+{normalized_value}"
                            unique_items[normalized_key].add(value.strip())
                            found_mobile_in_db = True
                        elif normalized_key == 'region' and any(provider in value for provider in known_providers):
                            for provider in value.split(';'):
                                unique_items['provider'].add(provider.strip())
                        elif normalized_key == 'provider' and ';' in value:
                            for provider in value.split(';'):
                                unique_items[normalized_key].add(provider.strip())
                        else:
                            unique_items[normalized_key].add(value.strip())
                        if normalized_key == 'aadhaar':
                            found_aadhaar_in_db = True
                        elif normalized_key == 'passport':
                            found_passport_in_db = True
            if found_mobile_in_db:
                mobile_searches += 1
            if found_aadhaar_in_db:
                aadhaar_searches += 1
            if found_passport_in_db:
                passport_searches += 1
            database_details.append({
                "database": db_name,
                "description": info_leak,
                "num_results": num_results,
                "fields_found": sorted(list(fields_found))
            })

    # Normalize phone numbers
    normalized_phones = set()
    for phone in unique_items['telephone']:
        normalized = phone.lstrip('+')
        if normalized == query.lstrip('+'):
            normalized_phones.add(query)
        elif normalized.isdigit():
            if len(normalized) == 10:
                normalized_phones.add(f"+91{normalized}")
            elif len(normalized) == 12 and normalized.startswith('91'):
                normalized_phones.add(f"+{normalized}")
            else:
                normalized_phones.add(phone)
        else:
            normalized_phones.add(phone)
    unique_items['telephone'] = normalized_phones

    # Deduplicate addresses
    unique_items['address'] = set([addr.strip() for addr in unique_items['address']])

    results_dict = {k: sorted(list(v)) for k, v in unique_items.items()}

    final_output = {
        "execution_time": f"{execution_time}s",
        "requested_number": query,
        "results": results_dict,
        "search_iterations": search_iterations,
        "total_numbers_found": len(unique_items['telephone']),
        "total_addresses_found": len(unique_items['address']),
        "total_aadhaar_found": len(unique_items['aadhaar']),
        "total_passports_found": len(unique_items['passport']),
        "total_emails_found": len(unique_items['email']),
        "total_names_found": len(unique_items['name']),
        "total_father_names_found": len(unique_items['father_name']),
        "total_regions_found": len(unique_items['region']),
        "total_providers_found": len(unique_items['provider']),
        "total_ips_found": len(unique_items['ip']),
        "total_nicknames_found": len(unique_items['nickname']),
        "total_states_found": len(unique_items['state']),
        "total_usernames_found": len(unique_items['username']),
        "total_passwords_found": len(unique_items['password']),
        "total_dobs_found": len(unique_items['dob']),
        "total_zips_found": len(unique_items['zip']),
        "total_genders_found": len(unique_items['gender']),
        "total_urls_found": len(unique_items['url']),
        "total_companies_found": len(unique_items['company']),
        "total_job_titles_found": len(unique_items['job_title']),
        "total_websites_found": len(unique_items['website']),
        "total_facebook_ids_found": len(unique_items['facebook_id']),
        "total_twitter_ids_found": len(unique_items['twitter_id']),
        "total_blood_types_found": len(unique_items['blood_type']),
        "total_nationalities_found": len(unique_items['nationality']),
        "total_relationships_found": len(unique_items['relationship']),
        "total_mobile_searches": mobile_searches,
        "total_aadhaar_searches": aadhaar_searches,
        "total_passport_searches": passport_searches,
        "database_details": database_details
    }

    add_terminal_line("COMPLETE", "00ff00")
    return final_output

def calculate_risk_level(data):
    """Mobile-optimized risk calculation"""
    score = (data.get('total_numbers_found', 0) * 2 +
             data.get('total_addresses_found', 0) * 2 +
             data.get('total_emails_found', 0) * 2 +
             data.get('total_aadhaar_found', 0) * 5 +
             data.get('total_passports_found', 0) * 5 +
             data.get('total_passwords_found', 0) * 3 +
             data.get('total_usernames_found', 0) * 2 +
             data.get('total_ips_found', 0) * 1 +
             data.get('total_dobs_found', 0) * 2)

    if score == 0:
        return "SECURE", "risk-low"
    elif score < 10:
        return "VULNERABLE", "risk-medium"
    elif score < 25:
        return "COMPROMISED", "risk-high"
    else:
        return "CRITICAL", "risk-critical"

def create_download_link(data, filename, file_type):
    """Mobile-optimized download link"""
    import base64
    if file_type == 'json':
        json_str = json.dumps(data, indent=2)
        b64 = base64.b64encode(json_str.encode()).decode()
        return f'<a href="data:application/json;base64,{b64}" download="{filename}" class="download-btn">⚡ DOWNLOAD {file_type.upper()}</a>'
    elif file_type == 'csv':
        df_data = []
        for key, values in data.get('results', {}).items():
            for value in values:
                if key == 'password':
                    value = '[ENCRYPTED]'
                df_data.append({'Type': key, 'Value': value})
        if df_data:
            df = pd.DataFrame(df_data)
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            return f'<a href="data:file/csv;base64,{b64}" download="{filename}" class="download-btn">⚡ DOWNLOAD {file_type.upper()}</a>'
        return '<span style="color: #666;">NO DATA</span>'

# Mobile-Optimized Header
st.markdown(f"""
<div class="cyber-header">
    <h1 class="cyber-title">⚡ 𝕏_𝕍𝕀ℝ𝕌𝕊_𝔼𝕏𝔼</h1>
    <p class="cyber-subtitle">[MOBILE INTELLIGENCE]</p>
    <p class="cyber-subtitle" style="font-size: 0.8rem;">ID: {generate_hacker_id()} | <span class="status-indicator status-online"></span>ONLINE</p>
</div>
""", unsafe_allow_html=True)

# Compact Terminal Output
if st.session_state.terminal_lines:
    with st.expander("📟 TERMINAL LOG", expanded=False):
        terminal_output = '<div class="terminal-box" style="max-height: 150px; overflow-y: auto; font-size: 0.85rem;">'
        for line in st.session_state.terminal_lines:
            terminal_output += f'<div style="color: #00ff00; margin: 3px 0;">{line}</div>'
        terminal_output += '</div>'
        st.markdown(terminal_output, unsafe_allow_html=True)

# Mobile-Optimized Sidebar
with st.sidebar:
    st.markdown("""
    <div class="terminal-box">
        <h3 style="color: #00ff00; margin-top: 0; font-size: 1rem;">⚡ QUICK SCAN</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📞 PHONE", use_container_width=True):
            st.session_state.search_query = "+919876543210"
            add_terminal_line("PHONE LOADED", "00ff00")
    with col2:
        if st.button("📧 EMAIL", use_container_width=True):
            st.session_state.search_query = "user@example.com"
            add_terminal_line("EMAIL LOADED", "00ff00")

    st.markdown("---")
    st.markdown("**📜 RECENT**")
    if st.session_state.search_history:
        for query, _ in reversed(st.session_state.search_history[-3:]):
            if st.button(f"🔍 {query[:15]}...", key=f"hist_{query}", use_container_width=True):
                st.session_state.search_query = query
                add_terminal_line(f"RECALL: {query}", "00ff00")
    else:
        st.markdown('<span style="color: #666;">NO LOGS</span>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("CLEAR TERMINAL", use_container_width=True):
        st.session_state.terminal_lines = []
        st.session_state.current_results = None
        add_terminal_line("TERMINAL CLEARED", "00ff00")
        st.rerun()

# Main Search Interface
st.markdown("### 🔍 TARGET SCAN")
query = st.text_input(
    "ENTER TARGET" "(example: +919876543210)",
    placeholder="Phone/Email/Username...",
    value=st.session_state.get('search_query', ''),
    help="Enter identifier to scan",
    key="query_input"
)

if st.button("⚡ EXECUTE SCAN", type="primary", use_container_width=True) and query:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.search_history.append((query, timestamp))
    
    with st.spinner("⚡ SCANNING..."):
        start_time = time.time()
        raw_details = get_leak_details(query)
        execution_time = round(time.time() - start_time, 2)
        st.session_state.current_results = process_and_format_response(query, raw_details, execution_time)
    st.session_state.search_query = ""

# Display Results
if st.session_state.current_results:
    data = st.session_state.current_results
    
    if 'error' in data:
        st.markdown(f"""
        <div class="terminal-box">
            <h4 style="color: #ff0000; margin-top: 0;">⚠️ ERROR</h4>
            <p style="color: #ff6600;">{data['error']}</p>
        </div>
        """, unsafe_allow_html=True)
    elif data.get('result') == "TARGET NOT FOUND":
        st.markdown("""
        <div class="terminal-box">
            <h4 style="color: #ffaa00; margin-top: 0;">🔍 NO RESULTS</h4>
            <p style="color: #ffaa00;">TARGET NOT FOUND</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Mobile-Optimized Stats
        st.markdown("### 📊 RESULTS")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h4 style="color: #00ff00; margin: 0; font-size: 0.9rem;">📞 PHONES</h4>
                <h3 style="color: #00ffff; margin: 0;">{data.get('total_numbers_found', 0)}</h3>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h4 style="color: #00ff00; margin: 0; font-size: 0.9rem;">📧 EMAILS</h4>
                <h3 style="color: #00ffff; margin: 0;">{data.get('total_emails_found', 0)}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h4 style="color: #00ff00; margin: 0; font-size: 0.9rem;">🃏 AADHAAR</h4>
                <h3 style="color: #00ffff; margin: 0;">{data.get('total_aadhaar_found', 0)}</h3>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h4 style="color: #00ff00; margin: 0; font-size: 0.9rem;">🛂 PPT</h4>
                <h3 style="color: #00ffff; margin: 0;">{data.get('total_passports_found', 0)}</h3>
            </div>
            """, unsafe_allow_html=True)

        # Risk Assessment
        risk_level, risk_class = calculate_risk_level(data)
        st.markdown("### 🛡️ THREAT LEVEL")
        st.markdown(f"""
        <div class="terminal-box">
            <h4 style="color: #00ff00; margin-top: 0;">SECURITY STATUS</h4>
            <p style="margin: 10px 0;">
                <strong>THREAT:</strong> <span class="{risk_class}">{risk_level}</span><br>
                <strong>TARGET:</strong> <code>{data.get('requested_number', 'N/A')}</code><br>
                <strong>TIME:</strong> <code>{data.get('execution_time', 0)}s</code><br>
                <strong>DATABASES:</strong> <code>{data.get('search_iterations', 0)}</code>
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Mobile Data Visualization
        if sum([data.get('total_numbers_found', 0), data.get('total_emails_found', 0), 
                data.get('total_aadhaar_found', 0), data.get('total_passports_found', 0),
                data.get('total_addresses_found', 0), data.get('total_ips_found', 0)]) > 0:
            chart_data = {
                'Type': ['PHONES', 'EMAILS', 'AADHAAR', 'PASSPORTS', 'ADDRESSES', 'IPS'],
                'Count': [
                    data.get('total_numbers_found', 0),
                    data.get('total_emails_found', 0),
                    data.get('total_aadhaar_found', 0),
                    data.get('total_passports_found', 0),
                    data.get('total_addresses_found', 0),
                    data.get('total_ips_found', 0)
                ]
            }
            df_chart = pd.DataFrame(chart_data)
            fig = px.bar(df_chart, x='Type', y='Count', 
                         color='Count', color_continuous_scale=['#00ff00', '#00ffff'],
                         title="DATA FOUND")
            fig.update_layout(
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font={'color': '#00ff00', 'size': 10},
                height=250,
                margin=dict(l=20, r=20, t=30, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)

        # Mobile Tabs
        st.markdown("### 📋 LEAKED DATA")
        tab1, tab2, tab3, tab4 = st.tabs(["📞 CONTACTS", "🆔 IDENTITY", "🌐 DIGITAL", "📚 ADDITIONAL"])
        
        with tab1:
            results = data.get('results', {})
            if results.get('telephone'):
                st.markdown("**📞 PHONES**")
                for phone in results['telephone']:
                    st.markdown(f'<div class="data-row"><code>{phone}</code></div>', unsafe_allow_html=True)
            if results.get('email'):
                st.markdown("**📧 EMAILS**")
                for email in results['email']:
                    st.markdown(f'<div class="data-row"><code>{email}</code></div>', unsafe_allow_html=True)
            if results.get('provider'):
                st.markdown("**📡 PROVIDERS**")
                for provider in results['provider']:
                    st.markdown(f'<div class="data-row">{provider}</div>', unsafe_allow_html=True)
            if results.get('address'):
                st.markdown("**🏘️ ADDRESSES**")
                for address in results['address']:
                    st.markdown(f'<div class="data-row">{address}</div>', unsafe_allow_html=True)
        
        with tab2:
            results = data.get('results', {})
            if results.get('name'):
                st.markdown("**👤 NAMES**")
                for name in results['name']:
                    st.markdown(f'<div class="data-row">{name}</div>', unsafe_allow_html=True)
            if results.get('father_name'):
                st.markdown("**👨 FATHER NAMES**")
                for fname in results['father_name']:
                    st.markdown(f'<div class="data-row">{fname}</div>', unsafe_allow_html=True)
            if results.get('aadhaar'):
                st.markdown("**🃏 AADHAAR**")
                for aadhaar in results['aadhaar']:
                    st.markdown(f'<div class="data-row"><code>{aadhaar}</code></div>', unsafe_allow_html=True)
            if results.get('passport'):
                st.markdown("**🛂 PASSPORTS**")
                for passport in results['passport']:
                    st.markdown(f'<div class="data-row"><code>{passport}</code></div>', unsafe_allow_html=True)
        
        with tab3:
            results = data.get('results', {})
            if results.get('username'):
                st.markdown("**👤 USERNAMES**")
                for username in results['username']:
                    st.markdown(f'<div class="data-row">{username}</div>', unsafe_allow_html=True)
            if results.get('password'):
                st.markdown("**🔑 PASSWORDS**")
                st.warning(f"Found {len(results['password'])} encrypted passwords")
            if results.get('ip'):
                st.markdown("**🌐 IPS**")
                for ip in results['ip']:
                    st.markdown(f'<div class="data-row"><code>{ip}</code></div>', unsafe_allow_html=True)
            if results.get('facebook_id'):
                st.markdown("**📘 FACEBOOK IDS**")
                for fid in results['facebook_id']:
                    st.markdown(f'<div class="data-row"><code>{fid}</code></div>', unsafe_allow_html=True)
            if results.get('twitter_id'):
                st.markdown("**🐦 TWITTER IDS**")
                for tid in results['twitter_id']:
                    st.markdown(f'<div class="data-row"><code>{tid}</code></div>', unsafe_allow_html=True)
        
        with tab4:
            results = data.get('results', {})
            if results.get('nickname'):
                st.markdown("**😎 NICKNAMES**")
                for nickname in results['nickname']:
                    st.markdown(f'<div class="data-row">{nickname}</div>', unsafe_allow_html=True)
            if results.get('state'):
                st.markdown("**🇮🇳 STATES**")
                for state in results['state']:
                    st.markdown(f'<div class="data-row">{state}</div>', unsafe_allow_html=True)
            if results.get('dob'):
                st.markdown("**🎂 DOB**")
                for dob in results['dob']:
                    st.markdown(f'<div class="data-row">{dob}</div>', unsafe_allow_html=True)
            if results.get('zip'):
                st.markdown("**📍 ZIP**")
                for zip_code in results['zip']:
                    st.markdown(f'<div class="data-row">{zip_code}</div>', unsafe_allow_html=True)
            if results.get('gender'):
                st.markdown("**⚧️ GENDER**")
                for gender in results['gender']:
                    st.markdown(f'<div class="data-row">{gender}</div>', unsafe_allow_html=True)
            if results.get('url'):
                st.markdown("**🔗 URL**")
                for url in results['url']:
                    st.markdown(f'<div class="data-row"><code>{url}</code></div>', unsafe_allow_html=True)
            if results.get('company'):
                st.markdown("**🏢 COMPANY**")
                for company in results['company']:
                    st.markdown(f'<div class="data-row">{company}</div>', unsafe_allow_html=True)
            if results.get('job_title'):
                st.markdown("**💼 JOB TITLE**")
                for job in results['job_title']:
                    st.markdown(f'<div class="data-row">{job}</div>', unsafe_allow_html=True)
            if results.get('website'):
                st.markdown("**🌐 WEBSITE**")
                for website in results['website']:
                    st.markdown(f'<div class="data-row"><code>{website}</code></div>', unsafe_allow_html=True)
            if results.get('blood_type'):
                st.markdown("**🩸 BLOOD TYPE**")
                for blood in results['blood_type']:
                    st.markdown(f'<div class="data-row">{blood}</div>', unsafe_allow_html=True)
            if results.get('nationality'):
                st.markdown("**🏳️ NATIONALITY**")
                for nationality in results['nationality']:
                    st.markdown(f'<div class="data-row">{nationality}</div>', unsafe_allow_html=True)
            if results.get('relationship'):
                st.markdown("**❤️ RELATIONSHIP**")
                for rel in results['relationship']:
                    st.markdown(f'<div class="data-row">{rel}</div>', unsafe_allow_html=True)
        
        # Mobile Export Options
        st.markdown("### 💾 EXPORT")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                create_download_link(data, f"virus_{query}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'json'),
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                create_download_link(data, f"virus_{query}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", 'csv'),
                unsafe_allow_html=True
            )

# Mobile Telegram Section
st.markdown("---")
st.markdown(f"""
<div class="telegram-section">
    <h3>🛡️ CONNECT & ACQUIRE</h3>
    <p style="color: #000000; font-size: 1rem; font-weight: bold; margin-bottom: 1rem;">BUY THIS WEBSITE SOURCE CODE + API</p>
    <p style="color: #ffffff; font-size: 0.9rem; margin-bottom: 1rem;">Message to buy: <a href="https://t.me/{TELEGRAM_USERNAME.replace('@', '')}" target="_blank" style="color: #00ffff; font-weight: bold;">{TELEGRAM_USERNAME}</a> (Telegram)</p>
    <p style="color: #00ff00; font-size: 0.95rem; font-weight: bold; text-shadow: 0 0 5px #00ff00; margin-bottom: 1rem;">LOWEST PRICE IN ALL OF THE UNIVERSE</p>
    <a href="https://t.me/{TELEGRAM_USERNAME.replace('@', '')}" target="_blank" class="telegram-link">👤 {TELEGRAM_USERNAME}</a>
    <a href="https://t.me/{TELEGRAM_CHANNEL.replace('@', '')}" target="_blank" class="telegram-link">📢 {TELEGRAM_CHANNEL}</a>
</div>
""", unsafe_allow_html=True)

# Mobile Footer
st.markdown(f"""
<div style='text-align: center; color: #00ff00; padding: 20px; border-top: 2px solid #00ff00; background: rgba(0,0,0,0.9); margin-top: 1rem;'>
    <p style="font-size: 1.2rem; font-weight: bold; margin: 5px 0;">⚡ 𝕏_𝕍𝕀ℝ𝕌𝕊_𝔼𝕏𝔼 MOBILE</p>
    <p style="font-size: 0.9rem; margin: 5px 0;">AUTHORIZED USE ONLY</p>
    <p style="font-size: 0.8rem; margin: 5px 0; color: #00ffff;">© 2025 {DEVELOPER_NAME}</p>
</div>
""", unsafe_allow_html=True)