# ScopeINT 🔍
<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/OSINT-Security-blue?style=for-the-badge&logo=spyware&logoColor=white" alt="OSINT">
</p>

**Domain Intelligence & OSINT Framework**


ScopeINT is a professional, production-ready CLI tool designed for cybersecurity reconnaissance. It gathers OSINT data on a target domain, performs DNS and SSL analysis, fingerprints HTTP headers, and provides a heuristic risk score.

> [!IMPORTANT]
> **Ethical Disclaimer**: This tool is for defensive security and OSINT research only. Ensure you have authorization before scanning assets that you do not own.

## 🚀 Features
- **WHOIS Intelligence**: Registrar details, domain age, and privacy detection.
- **DNS Enumeration**: A, AAAA, MX, TXT, NS records + SPF/DMARC detection.
- **Subdomain Discovery**: Enumerates subdomains via Certificate Transparency (crt.sh).
- **SSL/TLS Analysis**: Certificate issuer, validity, and weak TLS version detection.
- **HTTP Fingerprinting**: Security header analysis and server tech hints.
- **Risk Scoring Engine**: Heuristic scoring (0-100) based on domain age, missing security configs, and TLS weaknesses.
- **JSON Export**: Automated report generation in JSON format.

## 🛠 Project Structure
```text
ScopeINT/
├── core/
│   ├── whois.py       # WHOIS gathering
│   ├── dns.py         # DNS & Subdomains
│   ├── ssl_scan.py    # SSL/TLS Analysis
│   ├── headers.py     # HTTP Fingerprinting
│   └── risk_engine.py # Heuristic Risk Scoring
├── utils/
│   └── banner.py      # ASCII Branding
├── reports/           # Generated JSON Reports
├── main.py            # Entry Point
└── README.md
```

## 📦 Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/vision-dev1/ScopeINT
   cd ScopeINT
   
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage
Simply run the tool and follow the interactive prompts:
```bash
python main.py
```

**Flow:**
1.  **Banner**: Terminal clears and ScopeINT branding is displayed.
2.  **Input**: Enter the target domain (e.g., `owasp.org`).
3.  **Scan**: Automated intelligence gathering across all modules.
4.  **Menu**: Interactive options to save as **PDF**, **JSON**, or Quit.

## 🛡 Risk Scoring Explanation
Scale: **0–100**
- **Low (0-30)**: Minimal risk, well-configured.
- **Medium (31-70)**: Common misconfigurations or relatively young domains.
- **High (71-100)**: Critical security gaps, new domains, or expired SSL.

## 🔗 Author
VISION KC
[GITHUB](https://github.com/vision-dev1)
[WEBSITE](https://visionkc.com.np)
