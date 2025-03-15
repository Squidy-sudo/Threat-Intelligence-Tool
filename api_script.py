import requests
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify

# Load API Keys from .env file
load_dotenv()
OTX_API_KEY = os.getenv("OTX_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

app = Flask(__name__)

# Function to get threat data from AlienVault OTX
def get_otx_data(ip):
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    headers = {"X-OTX-API-KEY": OTX_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Function to get threat data from AbuseIPDB
def get_abuseipdb_data(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check():
    ip = request.form.get("ip")
    if not ip:
        return jsonify({"error": "No IP provided"})
    
    otx_data = get_otx_data(ip)
    abuseipdb_data = get_abuseipdb_data(ip)
    
    return render_template("result.html", ip=ip, otx_data=otx_data, abuseipdb_data=abuseipdb_data)

if __name__ == "__main__":
    app.run(debug=True)
