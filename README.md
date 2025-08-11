# 📈 Real-time Crypto Price Anomaly Monitor

A real-time cryptocurrency price tracking and anomaly detection system that monitors multiple exchanges, flags unusual price movements, and sends alerts via web dashboard and notifications. Designed for traders, analysts, and developers who want to detect early signs of volatility or potential market manipulation.

---

## 🚀 Features
- **Live Price Streaming** – Fetches real-time data from major crypto exchanges via WebSocket & REST APIs.
- **Anomaly Detection** – Detects sudden price spikes, dips, or unusual volatility using statistical and ML-based methods.
- **Multi-Exchange Support** – Aggregates prices from multiple sources for accuracy and resilience.
- **Interactive Dashboard** – Visualizes live prices and anomaly events in real-time charts.
- **Custom Alerts** – Sends push/email notifications when anomalies are detected.
- **Scalable Architecture** – Built with asynchronous processing to handle large volumes of tick data.

---

## 🛠 Tech Stack
| Component             | Technology Used |
|-----------------------|-----------------|
| Data Ingestion        | Python, WebSocket, REST APIs |
| Data Processing       | Pandas, NumPy, AsyncIO |
| Anomaly Detection     | Scikit-learn, Statistical Models (Z-Score, IQR, Isolation Forest) |
| Backend API           | FastAPI |
| Dashboard & Charts    | React.js, Chart.js / D3.js |
| Alerts & Notifications| Webhooks, SMTP, Push API |
| Deployment            | Docker, AWS (EC2 / Lambda / S3) |

---

## 📊 Architecture Diagram

flowchart LR
    A[Crypto Exchanges] -->|Live Prices (WebSocket / REST)| B[Data Ingestion Service]
	
    B --> C[Data Preprocessing & Cleaning]
	
    C --> D[Anomaly Detection Engine]
	
    D -->|Detected Anomalies| E[Notification Service]
	
    D --> F[Backend API (FastAPI)]
	
    F --> G[React Dashboard]

    E -->|Email / Push / Webhooks| H[End Users]
	
    G --> H


⸻
📷 Dashboard Preview
<img width="1536" height="1024" alt="317EA8EE-5F44-4EBC-9373-6C5E5C00BA90" src="https://github.com/user-attachments/assets/501e10d1-a1fc-4be6-a17f-a7a99e6bd945" />


📊 Anomaly Detection Methods
	•	Statistical Thresholding: Z-Score, Interquartile Range (IQR)
	•	Machine Learning: Isolation Forest, One-Class SVM
	•	Rolling Window Volatility Analysis: Detects unusual standard deviation changes

⸻

⚙️ Installation & Setup

# Clone the repository
git clone https://github.com/yourusername/crypto-price-anomaly-monitor.git
cd crypto-price-anomaly-monitor

# Install dependencies
pip install -r requirements.txt

# Start backend
uvicorn app.main:app --reload

# Start frontend
cd frontend
npm install
npm start


⸻

🔍 Usage
	1.	Run the backend to connect to live crypto price feeds.
	2.	Open the dashboard in your browser to view live charts.
	3.	Configure alerts in config.yaml to set your anomaly thresholds and notification preferences.

⸻

📈 Example Output

[ALERT] BTC/USD anomaly detected!
Timestamp: 2025-08-11 14:52:03 UTC
Price Change: +6.4% in 2 minutes
Anomaly Score: 0.98
