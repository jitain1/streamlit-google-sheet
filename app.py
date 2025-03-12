import streamlit as st
import gspread
import pandas as pd
import io
import openai
from google.oauth2.service_account import Credentials

# 🎨 Streamlit UI Customization
st.set_page_config(page_title="Google Sheets Viewer & AI Chatbot", page_icon="📊", layout="wide")

# 🎯 App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Google Sheets Data Viewer & AI Chatbot 🤖</h1>", unsafe_allow_html=True)

# 🔐 Load Service Account Credentials
try:
    SERVICE_ACCOUNT_INFO = st.secrets["gcp_service_account"]
    SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    creds = Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO, scopes=SCOPES)
    client = gspread.authorize(creds)
except Exception as e:
    st.error("🚨 **Error loading credentials.** Check `secrets.toml` configuration.")
    st.text(e)
    st.stop()

# 📄 Set Spreadsheet Name
SPREADSHEET_NAME = "WCS FINAL"

# 📌 Try to Access Spreadsheet
try:
    spreadsheet = client.open(SPREADSHEET_NAME)
    worksheets = spreadsheet.worksheets()
    sheet_names = [sheet.title for sheet in worksheets]
    st.success(f"✅ Successfully connected to **{SPREADSHEET_NAME}**")
except Exception as e:
    st.error("⚠️ **Could not access the spreadsheet.** Ensure the name is correct & service account has access.")
    st.text(e)
    st.stop()

# 📝 Auto-Select Worksheet
if "WCS FINAL" in sheet_names:
    selected_sheet = "WCS FINAL"
else:
    selected_sheet = st.selectbox("📑 Choose a Worksheet", sheet_names)

# 🎨 UI Styling for Selected Sheet
st.markdown(f"<h3 style='color: #2196F3;'>📄 Viewing: {selected_sheet}</h3>", unsafe_allow_html=True)

# 📊 Load & Display Data
try:
    worksheet = spreadsheet.worksheet(selected_sheet)
    data = worksheet.get_all_values()

    if data:
        df = pd.DataFrame(data)
        df.columns = df.iloc[0]  # First row as headers
        df = df[1:]  # Remove header row
        df.reset_index(drop=True, inplace=True)

        # 🎨 Display Data with Pagination
        st.dataframe(df, use_container_width=True)

        # 📥 Add Download Button
        st.subheader("📥 Download Data")
        output = io.BytesIO()
        df.to_csv(output, index=False)
        st.download_button(label="⬇️ Download CSV", data=output.getvalue(), file_name="data.csv", mime="text/csv")

    else:
        st.warning("⚠️ The selected worksheet is empty.")
except Exception as e:
    st.error("❌ **Error loading data from worksheet.**")
    st.text(e)

# 💬 AI Chatbot Feature
st.subheader("🤖 AI Chatbot")
openai.api_key = st.secrets["openai_api_key"]  # Store in `.streamlit/secrets.toml`

# Chat Function
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful AI assistant."}, {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error: {e}"

# Chat UI
user_input = st.text_input("📝 Ask AI Anything:")
if st.button("💬 Chat with AI"):
    if user_input:
        ai_response = chat_with_gpt(user_input)
        st.write("🤖 **AI Response:**", ai_response)
    else:
        st.warning("⚠️ Please enter a question.")

# ℹ️ Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center;'>
        <p style='color: gray;'>🔹 <b>Tip:</b> Ensure your Google Sheet is shared with the service account email.</p>
        <p>Made with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
