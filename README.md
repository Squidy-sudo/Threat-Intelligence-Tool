# Threat Intelligence Tool

A real-time threat intelligence system to track and analyze malicious IPs, domains, and URLs using public threat feeds.

## Features
- **Live Threat Monitoring**: Fetches threat intelligence data from AlienVault OTX and AbuseIPDB.
- **Flask-based Web Dashboard**: View results on a webpage instead of the terminal.
- **Automated Updates**: Retrieves fresh data from threat feeds.
- **Potential Firewall Integration**: Can be extended to automate security responses.

## Installation & Setup
### Prerequisites
- Install **Python 3.10+**
- Install **Git**

### Clone the Repository
```sh
git clone https://github.com/Squidy-sudo/Threat-Intelligence-Tool.git
cd Threat-Intelligence-Tool
```

### Set Up a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application
```sh
python app.py
```
Then, open your browser and go to `http://127.0.0.1:5000/`.

## GitHub Configuration & Push Instructions
### **1️⃣ Set Up Your Git Identity**
```sh
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```
Check if it worked:
```sh
git config --global --list
```

### **2️⃣ Commit Your Changes**
```sh
git add .
git commit -m "Initial commit - Threat Intelligence Tool"
```

### **3️⃣ Push to GitHub**
```sh
git branch -M main
git push -u origin main
```
✅ **Your project should now be on GitHub!** 🎉  

## Future Enhancements
- Add **historical data analysis**.
- Improve UI with interactive charts.
- Enable **email alerts** for detected threats.
- Develop **firewall integration** for automatic blocking.

---
Let me know if you need any tweaks! 🚀

