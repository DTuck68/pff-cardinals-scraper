import os
import json
import pandas as pd
import asyncio
from scraper import scrape_pff_roster
from google.oauth2.service_account import Credentials
import gspread

# Authenticate with Google Sheets
def get_sheet_client():
    credentials_info = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])
    creds = Credentials.from_service_account_info(credentials_info, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    return gspread.authorize(creds)

# Update Google Sheet
def update_sheet(df, sheet_url):
    gc = get_sheet_client()
    sh = gc.open_by_url(sheet_url)
    worksheet = sh.sheet1
    worksheet.clear()
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

if __name__ == "__main__":
    df = asyncio.run(scrape_pff_roster())
    update_sheet(df, os.environ["GOOGLE_SHEET_URL"])