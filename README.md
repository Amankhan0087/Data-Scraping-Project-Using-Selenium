# Data Scraping Project Using Selenium

A simple Python script that uses Selenium to scrape product listings from Daraz.pk search results.

## What it does

`project.py` opens a Chrome browser via Selenium, searches Daraz.pk for a given query (currently hardcoded to `laptop`), waits for the results to render, and prints the matching product elements found on the page.

## Requirements

- Python 3
- Google Chrome
- [Selenium](https://pypi.org/project/selenium/) (`pip install selenium`)

## Usage

```bash
python project.py
```

To search for a different product, edit the `query` variable in `project.py`.

## Notes

- Selenium's Chrome driver is used directly, so a compatible ChromeDriver/Chrome installation is required.
- The script relies on Daraz's current page structure (`[data-qa-locator="product-item"]`); if the site changes, the selector may need updating.
