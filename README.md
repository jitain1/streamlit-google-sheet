📊 Google Sheets Data Viewer (Streamlit App)

This Streamlit app fetches and displays data from a Google Sheets spreadsheet securely using a Google Cloud Service Account.

🚀 Features

Read data from a Google Sheet.

Display data in an interactive table.

Secure authentication using Streamlit Secrets.

Deployable on Streamlit Cloud for free.

📌 Prerequisites

Python 3.8+ installed

Google Cloud Platform (GCP) account

Service Account JSON key (GCP IAM & Admin)

A Google Sheet with shared access to the service account

GitHub repository (for deployment)

📥 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

2️⃣ Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Google Cloud Service Account

Go to Google Cloud Console

Navigate to IAM & Admin → Service Accounts

Click Create Service Account → Assign Editor or BigQuery Data Viewer role.

Click Create Key → Choose JSON → Download the file.

Share your Google Sheet with the service account email.

🔑 Configure Streamlit Secrets

1️⃣ Open secrets.toml File (Create if not exists)

[google_service_account]
type = "service_account"
project_id = "bigquery-demo-436010"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_service_account_email"
client_id = "your_client_id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"

2️⃣ Add Secrets in Streamlit Cloud

Go to Streamlit Cloud

Navigate to Settings → Secrets Manager

Paste the contents of secrets.toml

Click Save

🏃‍♂️ Run the App Locally

streamlit run app.py

🚀 Deploy on Streamlit Cloud

1️⃣ Push Code to GitHub

git add .
git commit -m "Initial commit"
git push origin main

2️⃣ Deploy on Streamlit Cloud

Go to Streamlit Cloud

Click "New App" → Select your GitHub repository.

Choose the "main" branch and set the app file path (app.py).

Click "Deploy". 🚀

🎯 Troubleshooting

App crashes?

Check if Google Sheet is shared with the service account.

Verify Streamlit Secrets contain correct credentials.

Wrong sheet name?

Double-check the worksheet name in app.py.

No data appearing?

Ensure the Google Sheet ID is correct.

🎉 Done! 🎉

Your Streamlit app is now live and fetching real-time data from Google Sheets! 🚀

