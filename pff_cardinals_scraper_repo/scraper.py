import asyncio
from playwright.async_api import async_playwright

async def scrape_pff_roster():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.pff.com/nfl/teams/arizona-cardinals/1/roster")

        await page.wait_for_selector("table")
        table = await page.query_selector("table")
        html = await table.inner_html()

        import pandas as pd
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        headers = [th.get_text(strip=True) for th in soup.find_all("th")]
        rows = []
        for tr in soup.find_all("tr")[1:]:
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            if cells:
                rows.append(cells)

        df = pd.DataFrame(rows, columns=headers)
        await browser.close()
        return df

if __name__ == "__main__":
    df = asyncio.run(scrape_pff_roster())
    df.to_csv("pff_roster.csv", index=False)