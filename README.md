# 🕷️ Web Scraping Masterclass: Complete Course Repository

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.11+-darkgreen?logo=scrapy&logoColor=white)](https://scrapy.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-bs4-orange)](https://www.crummy.com/software/BeautifulSoup/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![Pandas](https://img.shields.io/badge/Pandas-ETL%20%26%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Comprehensive codebase, automated scripts, hands-on tutorials, and end-to-end industrial web scraping projects developed during the **"Ultimate Web Scraping Course" by CampusX**.

> **Special Acknowledgments:**  
> A heartfelt thank you to **Nitish Sir** and **Misbah Sir** for curating an incredible, practical curriculum covering everything from raw HTTP requests to production-grade distributed crawling, anti-bot bypasses, and automated CAPTCHA solving.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Projects Showcase](#-projects-showcase)
  - [1. 99acres Real Estate Scraper & ETL](#1-99acres-real-estate-scraper--etl-pipeline)
  - [2. Yahoo Finance Stock Market Scraper](#2-yahoo-finance-stock-market-scraper)
  - [3. BBC Sport Premier League Top Scorers](#3-bbc-sport-premier-league-top-scorers)
  - [4. Automated CAPTCHA Solver with Computer Vision](#4-automated-captcha-solver-with-computer-vision--ocr)
- [Core Modules & Learning Paths](#-core-modules--learning-paths)
  - [HTTP & Requests](#1-http--requests-library)
  - [BeautifulSoup4](#2-beautifulsoup4-dom-parsing)
  - [Selenium WebDriver](#3-selenium-webdriver-dynamic-web-automation)
  - [Scrapy Framework](#4-scrapy-framework-enterprise-crawling)
  - [Anti-Bot Countermeasures & CAPTCHA Bypass](#5-anti-bot-countermeasures--captcha-bypass)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuring Tesseract OCR](#configuring-tesseract-ocr-optional)
- [How to Run](#-how-to-run)
- [Key Engineering Practices](#-key-engineering-practices)
- [Contributing & Feedback](#-contributing--feedback)
- [License](#-license)

---

## 📖 Overview

Modern web scraping demands far more than fetching static HTML. Websites today rely on single-page applications (SPAs), dynamic DOM updates, infinite scroll mechanisms, authentication barriers, and sophisticated bot countermeasures.

This repository covers the complete spectrum of web data extraction:
- **Low-level HTTP Protocols**: Custom headers, session management, payload inspection, REST API reverse engineering.
- **Static Parsing**: Navigating DOM trees, robust CSS selectors, and data extraction with BeautifulSoup4.
- **Browser Automation**: End-to-end automation of dynamic websites using Selenium WebDriver, including `ActionChains`, waiting strategies, iframe context-switching, and alerts.
- **High-Throughput Crawling**: Enterprise-grade Scrapy spiders featuring asynchronous architectures, custom item pipelines, downloader middlewares, user-agent pools, and proxy rotation.
- **Anti-Bot & CAPTCHA Engineering**: Combining PIL, OpenCV image pre-processing, and Tesseract OCR to automatically solve image CAPTCHAs and bypass bot verification.
- **ETL Data Pipelines**: Transforming raw, messy scraped data into clean, typed, analysis-ready tabular datasets (Excel / JSON) using Pandas method-chaining.

---

## 📂 Repository Structure

```plaintext
Web_Scraping_Course_by_CampusX/
│
├── 📁 99 acres project/                 # End-to-end Real Estate Scraper (Chennai)
│   ├── 01. properties-scraper.py        # Functional Selenium scraper with multi-filters & pagination
│   ├── 02. restructured-properties-scraper.py # Modular Object-Oriented (OOP) implementation
│   └── chennai-properties-99acres.xlsx  # Extracted and cleaned properties dataset
│
├── 📁 Yahoo finance project/            # Financial Market Scraping
│   ├── stock_scraper.py                 # OOP StocksScraper class with hover menus & pagination
│   ├── stock_scraper.ipynb              # Interactive exploratory analysis & scraping notebook
│   └── yahoo-stocks-data.xlsx           # Cleaned stock market dataset (Price, Vol, Cap, PE)
│
├── 📁 Requests/                         # HTTP Protocol & REST API Fundamentals
│   ├── requests-tutorial.ipynb          # Interactive requests tutorial notebook
│   └── requests_tutorial.py             # Script covering GET/POST/PUT/DELETE, auth & error handling
│
├── 📁 Beautiful_soup/                   # Static HTML Parsing & Extraction
│   ├── Beautiful Soup Tutorial.ipynb    # Comprehensive guide to BeautifulSoup4 & DOM navigation
│   ├── html-doc.html                    # Reference HTML document for DOM traversal
│   └── EPL Top Scorers.xlsx             # BBC Sport Premier League top scorers dataset
│
├── 📁 selenium/                         # Browser Automation & Dynamic SPAs
│   ├── 📁 scripts/                      # 14 standalone, modular automation scripts:
│   │   ├── 01. getting-started.py               # Chrome driver setup & initialization
│   │   ├── 02. basic-interaction-with-elements.py # Finding elements, click, typing
│   │   ├── 03. submitting-forms.py              # Form filling & keyboard shortcuts
│   │   ├── 04. dropdowns.py                     # Single-selection select elements
│   │   ├── 05. multiselect.py                   # Multi-select options handling
│   │   ├── 06. basic-scrolling.py               # Coordinate-based scroll execution
│   │   ├── 07. infinite-scrolling.py            # Dynamic DOM infinite scroll loop
│   │   ├── 08. explicit-wait.py                 # WebDriverWait & expected_conditions
│   │   ├── 09. implicit-wait.py                 # Implicit timeout strategies
│   │   ├── 10. iframes.py                       # Switching between frame contexts
│   │   ├── 11. javascript-alert.py              # JS standard alert handling
│   │   ├── 12. confirmation-alert.py            # Confirmation popups (accept/dismiss)
│   │   ├── 13. prompt-alert.py                  # Prompt popups with text input
│   │   └── 14. page-object-model.py             # Page Object Model (POM) architecture
│   ├── Scrolling.ipynb                  # Interactive scroll demonstration
│   ├── basic interaction with elements.ipynb
│   ├── explicit and implicit waits.ipynb
│   ├── handling alerts.ipynb
│   ├── iframes.ipynb
│   └── page object model.ipynb
│
├── 📁 scrapy/                            # Production Distributed Scraping Framework
│   ├── 📁 custom_spider/                 # Spider-level custom_settings & JSON feeds
│   ├── 📁 data_pipelines/                # Item pipelines for cleaning & transformation
│   ├── 📁 demo_project/                  # Basic Scrapy architecture & spider setup
│   ├── 📁 handling_apis/                 # Scraping REST API endpoints directly via Scrapy
│   ├── 📁 login_page/                    # FormRequest authentication & session handling
│   ├── 📁 middleware/                    # Custom Downloader Middlewares (User-Agent rotation)
│   ├── 📁 middleware_demo/               # Proxy rotation & custom spider middlewares
│   ├── 📁 mini_project/                  # Books catalog scraper with custom items
│   └── 📁 quotes_scrapper/               # Multi-page pagination traversal with response.follow
│
├── 📁 working with captchas/            # Anti-Bot & CAPTCHA Engineering
│   ├── preventing-captchas.ipynb        # Human-in-the-loop & automated OCR bypass
│   ├── captcha.png                      # Raw cropped CAPTCHA screenshot
│   ├── captcha-processed.png            # OpenCV filtered & thresholded image
│   └── webpage.png                      # Full-page screenshot for element localization
│
├── LICENSE                              # MIT License
└── README.md                            # Repository Documentation
```

---

## 🚀 Projects Showcase

### 1. 99acres Real Estate Scraper & ETL Pipeline
*Directory:* [`99 acres project/`](99%20acres%20project/)

A robust, production-ready real estate property scraper targeting `99acres.com` for Chennai listings.

- **Dynamic Element Interaction**: Uses Selenium `ActionChains` to drag and release price budget sliders.
- **Dynamic Filter Automation**: Interacts with multi-state filter toggles ("Verified Listings", "Ready To Move", and expands hidden menus to enable "With Photos" and "With Videos").
- **Pagination & JS Execution**: Automatically locates the `Next Page >` control, scrolls it into the viewport via JavaScript (`window.scrollBy`), and iteratively pages through all listings.
- **Object-Oriented Design**: Encapsulated into the `PropertyScraper` class (`02. restructured-properties-scraper.py`) for reusability, maintainability, and clean error handling.
- **Pandas ETL Pipeline**:
  - Eliminates duplicates and strips whitespace.
  - Normalizes property prices: converts Crore (`cr`) and Lakh (`lac`) strings into uniform numeric values in Lakhs.
  - Cleans location strings by removing city suffixes and formatting sub-localities.
  - Converts square feet (`area_sqft`) and bedroom counts (`bhk`) into clean numeric types.
  - Exports clean dataset to [`chennai-properties-99acres.xlsx`](99%20acres%20project/chennai-properties-99acres.xlsx).

---

### 2. Yahoo Finance Stock Market Scraper
*Directory:* [`Yahoo finance project/`](Yahoo%20finance%20project/)

An automated financial market scraper extracting the "Most Active" equities from Yahoo Finance.

- **Interactive Navigation**: Simulates user hover interactions using Selenium `ActionChains` over the top navigation menus ("Markets" -> "Trending Tickers" -> "Most Active").
- **Table Data Extraction**: Iterates across table rows, extracting Symbol, Name, Price, Change, Volume, Market Cap, and PE Ratio.
- **Automated Multi-Page Traversal**: Handles paginated tables dynamically until the "Next" button is no longer clickable.
- **Data Standardization**:
  - Handles multiplier units: parses Billions (`B`) and Trillions (`T`) into standard numerical metrics.
  - Converts volume indicators (`M` to numeric).
  - Cleans non-reporting entries (`-` to `NaN`) and reformats numeric PE ratios.
  - Exports results directly to [`yahoo-stocks-data.xlsx`](Yahoo%20finance%20project/yahoo-stocks-data.xlsx).

---

### 3. BBC Sport Premier League Top Scorers
*Directory:* [`Beautiful_soup/`](Beautiful_soup/)

A lightweight, high-performance scraper parsing BBC Sport football player statistics.

- Uses `requests` with custom headers to fetch live sports data.
- Employs `BeautifulSoup` to navigate nested HTML tables and extract player name, club, goals scored, assists, and minutes per goal.
- Assembles tabular records into a structured Pandas DataFrame and outputs to [`EPL Top Scorers.xlsx`](Beautiful_soup/EPL%20Top%20Scorers.xlsx).

---

### 4. Automated CAPTCHA Solver with Computer Vision & OCR
*Directory:* [`working with captchas/`](working%20with%20captchas/)

A solution for handling challenge-response authentication (CAPTCHA) on protected login endpoints.

```
[Full Page Screenshot]
        │
        ▼ (Device Pixel Ratio Normalization)
[Cropped CAPTCHA (PIL)]
        │
        ▼ (OpenCV Pre-Processing: Grayscale + Median Blur + Otsu Threshold + Dilation)
[Binary Clean Image]
        │
        ▼ (Tesseract OCR Engine: --psm 8)
[Extracted Text String]
        │
        ▼
[Automated Form Submission & Bypass]
```

- **Device Pixel Ratio (DPR) Scaling**: Calculates browser `window.devicePixelRatio` to ensure pixel-perfect cropping on high-DPI displays (Retina/4K).
- **Computer Vision Filtering (OpenCV)**:
  - Color conversion from RGB to BGR and Grayscale.
  - Noise reduction via `cv2.medianBlur`.
  - Adaptive binarization using Otsu's thresholding (`cv2.threshold` with `THRESH_BINARY + THRESH_OTSU`).
  - Morphological dilation (`cv2.dilate`) with a $(2 \times 2)$ kernel to bridge broken character contours.
- **OCR Character Recognition**: Uses `pytesseract` with Page Segmentation Mode `--psm 8` (treating the image as a single word) to extract text and re-inject it into the login form automatically.
- **Human-in-the-Loop Fallback**: Demonstrates manual terminal halt using `input()` for complex/adversarial CAPTCHAs.

---

## 🛠️ Core Modules & Learning Paths

### 1. HTTP & Requests Library
*Location:* [`Requests/`](Requests/)
- **Methods & Verbs**: Thorough implementation of `GET`, `POST` (form data vs. JSON body), `PUT`, and `DELETE`.
- **Query Parameters**: Passing structured dictionaries to query strings (`?q=requests+language:python`).
- **Headers & Identity**: Injecting custom `User-Agent`, `Authorization` Bearer tokens, and content negotiations.
- **Error Handling**: Defensively catching network exceptions using `response.raise_for_status()` and `requests.exceptions.RequestException`.

### 2. BeautifulSoup4 (DOM Parsing)
*Location:* [`Beautiful_soup/`](Beautiful_soup/)
- **Tree Traversal**: Exploring `.parent`, `.children`, `.descendants`, and sibling elements.
- **Search Queries**: Leveraging `find()`, `find_all()`, attribute dictionaries, and regex matchers.
- **CSS Selectors**: Querying complex elements using `.select()` and `.select_one()`.
- **Content Extraction**: Clean extraction using `.get_text(strip=True)` and `.get('attr')`.

### 3. Selenium WebDriver (Dynamic Web Automation)
*Location:* [`selenium/`](selenium/) & [`selenium/scripts/`](selenium/scripts/)
- **Element Discovery**: Locating elements using XPATH, CSS Selectors, Class Names, and IDs.
- **Interactive Controls**: Handling standard inputs, dropdown select boxes (`Select`), and multi-select elements.
- **Synchronization**: Mastered Explicit Waits (`WebDriverWait` + `expected_conditions`) over flaky implicit sleeps.
- **Scroll Engineering**: Basic JavaScript scrolling and dynamic **Infinite Scrolling** based on dynamic `scrollHeight` tracking.
- **Context Switching**: Switching to and from `iframe` frames and managing multi-window browser sessions.
- **Alert Handling**: Accepting, dismissing, and sending text to native browser JS alerts (`alert`, `confirm`, `prompt`).
- **Architecture**: Implementation of the **Page Object Model (POM)** pattern for clean, maintainable automation code.

### 4. Scrapy Framework (Enterprise Crawling)
*Location:* [`scrapy/`](scrapy/)
Nine focused projects demonstrating Scrapy's capabilities:

| Subproject | Focus Area | Key Features Demonstrated |
| :--- | :--- | :--- |
| **`demo_project`** | Scrapy Basics | Standard project scaffold, CSS selectors, JSON exports |
| **`quotes_scrapper`** | Crawling & Pagination | Traversal across pages via `response.follow` |
| **`custom_spider`** | Custom Settings | Per-spider settings (`DOWNLOAD_DELAY`, concurrency, custom feeds) |
| **`data_pipelines`** | Item Pipelines | Item cleaning, string sanitization, and pipeline validation |
| **`mini_project`** | Data Modeling | Scraping books catalog into strongly-typed `Item` classes |
| **`handling_apis`** | API Scraping | Using Scrapy to directly crawl REST APIs returning JSON |
| **`login_page`** | Form Authentication | `FormRequest.from_response`, cookie management, authenticated crawls |
| **`middleware`** | Downloader Middlewares | Rotating random User-Agents across requests |
| **`middleware_demo`** | Proxy Rotation | Proxy middleware implementation to distribute network origin |

### 5. Anti-Bot Countermeasures & CAPTCHA Bypass
*Location:* [`working with captchas/`](working%20with%20captchas/)
- Overcoming anti-scraping flags: `--disable-blink-features=AutomationControlled`, custom user agents, incognito profiles.
- Automated optical character recognition on distorted text CAPTCHAs using image morphology.

---

## 💻 Tech Stack

| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core language for all scripts, spiders, and pipelines |
| **HTTP Client** | `requests` | Static resource retrieval & REST API interaction |
| **HTML Parsing** | `beautifulsoup4`, `lxml` | Fast DOM parsing and tag tree traversal |
| **Browser Automation** | `selenium` | Dynamic DOM interaction, JavaScript execution, SPAs |
| **Crawling Framework**| `scrapy` | Asynchronous, high-scale web crawling & pipelines |
| **Data Manipulation** | `pandas`, `numpy` | Data cleaning, type conversion, and restructuring |
| **Computer Vision** | `opencv-python`, `pillow` | Image preprocessing (filtering, thresholding, dilation) |
| **OCR Engine** | `pytesseract` (Tesseract-OCR) | Text extraction from processed CAPTCHA images |
| **Data Export** | `openpyxl` | Writing cleaned data to Excel spreadsheets |

---

## ⚡ Getting Started

### Prerequisites
- Python 3.10 or higher installed.
- Google Chrome browser installed (compatible with modern Selenium Manager).
- *(Optional, for CAPTCHA module)* Tesseract-OCR binary installed.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Yugalpoudel07/Web_Scraping_Course_by_CampusX.git
   cd Web_Scraping_Course_by_CampusX
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4 selenium scrapy pandas numpy opencv-python pillow pytesseract openpyxl jupyter
   ```

### Configuring Tesseract OCR (Optional)
If running [`working with captchas/preventing-captchas.ipynb`](working%20with%20captchas/preventing-captchas.ipynb):
1. Download and install Tesseract from the [UB-Mannheim Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki).
2. Ensure the binary path is correctly configured in your code:
   ```python
   import pytesseract
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

---

## 🏃 How to Run

### Running Selenium Projects
Execute any of the modular scripts directly:
```bash
# Run 99acres real estate scraper
python "99 acres project/02. restructured-properties-scraper.py"

# Run Yahoo Finance scraper
python "Yahoo finance project/stock_scraper.py"

# Run individual Selenium automation scripts
python "selenium/scripts/07. infinite-scrolling.py"
python "selenium/scripts/14. page-object-model.py"
```

### Running Scrapy Spiders
Navigate to any Scrapy project directory and launch the spider via the CLI:
```bash
# Example: Running the books scraper
cd scrapy/mini_project
scrapy crawl books_scraper -o output.json

# Example: Running the quotes scraper with custom settings
cd ../custom_spider
scrapy crawl quotes_scrapper

# Example: Running the authenticated scraper
cd ../login_page
scrapy crawl quotes_scraper
```

### Running Jupyter Notebooks
Launch Jupyter Notebook to explore interactive tutorials and visual experiments:
```bash
jupyter notebook
```
Open any of the `.ipynb` files to follow along step-by-step.

---

## 💡 Key Engineering Practices

- **Resilient Waiting**: Replaced brittle hardcoded sleeps (`time.sleep`) with event-driven synchronization (`WebDriverWait` with `expected_conditions`).
- **Object-Oriented Design**: Scrapers are structured as modular classes (`PropertyScraper`, `StocksScraper`, `LoginPage`) separating navigation, extraction, and cleaning.
- **Anti-Fingerprinting**: Disabled automated flags (`--disable-blink-features=AutomationControlled`), added realistic user headers, and rotated proxies.
- **Robust ETL Pipelines**: Integrated Pandas method chaining (`.assign()`, `.pipe()`, `.apply()`) for readable, reproducible data transformations.
- **Rate-Limiting & Politeness**: Configured download delays and concurrency caps in Scrapy to respect target servers.

---

## 🤝 Contributing & Feedback

Contributions, suggestions, and feature requests are always welcome!
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Crafted with ❤️ by <a href="https://github.com/Yugalpoudel07">Yugal Poudel</a><br>
  <i>Happy Scraping! 🕸️</i>
</p>
