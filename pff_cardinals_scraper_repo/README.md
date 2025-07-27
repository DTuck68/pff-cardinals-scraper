# PFF Cardinals Roster Scraper

This GitHub Action scrapes the Arizona Cardinals roster from [pff.com](https://www.pff.com/nfl/teams/arizona-cardinals/1/roster) every Monday and updates a Google Sheet.

## Setup

1. Upload all files to a GitHub repository.
2. Add these repository secrets:
   - `GOOGLE_CREDENTIALS_JSON`: contents of your credentials.json file
   - `GOOGLE_SHEET_URL`: URL to your Google Sheet

## Manual Run

You can also trigger the workflow manually in the GitHub Actions tab.