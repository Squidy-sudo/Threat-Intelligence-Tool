# Live Threat Intelligence Feed

![Threat Intelligence Dashboard](https://your-image-url.com)

## 🚀 Project Overview
The **Live Threat Intelligence Feed** is a real-time threat monitoring system that collects, analyzes, and displays malicious IPs, domains, and URLs. It integrates public threat feeds to provide up-to-date intelligence, helping SOC analysts and penetration testers track potential security threats.

## 🔥 Key Features
- **Automated Threat Data Ingestion** – Fetches data from **AlienVault OTX, AbuseIPDB**.
- **Flask-Based Web Dashboard** – Real-time monitoring of active threats with historical analysis.
- **Threat Scoring & Analysis** – Assigns risk scores to track potential threats.
- **SQLite Database** – Lightweight and efficient storage for threat logs.
- **API Integration** – Can be extended to interact with **firewalls, SIEMs, and SOAR tools**.
- **Potential Firewall Rule Integration** – Helps automate threat blocking mechanisms.

## 📌 Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite
- **API Integration:** REST APIs (AlienVault OTX, AbuseIPDB)
- **Frontend:** HTML/CSS (Flask Templates)

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/threat-intel-feed.git
   cd threat-intel-feed
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set API Keys (AlienVault OTX, AbuseIPDB)**
   - Create a `.env` file in the project root and add:
     ```env
     OTX_API_KEY=your_otx_api_key
     ABUSEIPDB_API_KEY=your_abuseipdb_api_key
     ```
   **Note:** The `.env` file is ignored by Git (via `.gitignore`). Do not share your API keys.

5. **Run the Application:**
   ```bash
   python app.py
   ```
   The app will be accessible at `http://127.0.0.1:5000`.

## 📊 Usage
- View live threat intelligence data on the Flask dashboard.
- Filter by IP, domain, or URL to analyze specific threats.
- Extend functionality by integrating firewall rules for automated blocking.

## 🚀 Future Enhancements
- **Machine Learning-based Threat Scoring**
- **SIEM Integration (Splunk, Elastic Security, etc.)**
- **Multi-user Authentication & Role-Based Access**

## 🤝 Contributing
Pull requests are welcome! Feel free to enhance the project by adding new threat sources or improving the dashboard.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🔍 **Built for SOC Analysts & Pen Testers to streamline real-time threat tracking!**

