# 🤖 Multi-Threaded Arabic News Scraper & NLP Feature Extractor

An optimized, production-ready Python data pipeline built to concurrently crawl Arabic news articles via XML Sitemaps, perform tailored NLP preprocessing, and compute text readability analytics. 

🌐 **Live Demo:** Access the trained AI model interface directly on [Hugging Face Spaces](https://huggingface.co/spaces/Alhareth/arabic-news-classifier)

---

## 🚀 Architectural & Engineering Highlights

- **High-Performance Concurrency:** Leveraged Python's `ThreadPoolExecutor` to orchestrate non-blocking multi-threaded web requests, maximizing data crawling throughput safely without IP bans.
- **Resilient Pipeline Design:** Built strict, decoupled error-handling mechanisms and structural logging to handle network timeouts and structural shifts in website architectures.
- **Robust Text Preprocessing:** Engineered modular regular expressions to sanitize raw Arabic text fields by eliminating URLs, invalid metadata blocks, structural markers, and junk assets inside nested `script` tags.
- **Statistical NLP Features:** Adapted text analytics frameworks to extract structural counts and compute advanced semantic scores like *Flesch Reading Ease* adapted for Arabic script complexities.

---

## 📊 Model Evolution & Metrics (Fine-Tuning)

The downstream text classification model (`CAMeLBERT`) was fine-tuned using an iterative **Self-Training** (Pseudo-Labeling) methodology:

| Model Version | Training Dataset Size | Key Improvements | Final Accuracy (F1-Macro) |
| :--- | :--- | :--- | :--- |
| **Model v1** | 3,000 "Golden" Articles | Manually annotated high-quality base data. | Base Baseline |
| **Model v2 (Current)** | **41,435** Articles | Combined golden & high-confidence "Silver" data (Threshold >= 75%). | **82.33% (81.56%)** |

---

## 📁 Repository Blueprint

```text
arabic-news-scraper/
│
├── src/                          # Core source code modules
│   ├── __init__.py               # Initializes src as a Python package
│   ├── config.py                 # Infrastructure presets & localized logging hooks
│   ├── scraper.py                # Multi-threaded crawling nodes & network routines
│   ├── preprocessor.py           # Algorithmic text cleaning & markup isolation
│   └── feature_extractor.py      # NLP feature engineering & mathematical metrics
│
├── notebooks/                    # Developmental logs & historical Colab research
│   └── exploration_and_demo.ipynb
│
├── data/                         # Local data sandbox (Protected via .gitignore)
│   └── .gitkeep
│
├── .gitignore                    # Safeguards repository from uploading huge CSV files
├── requirements.txt              # Explicit third-party system dependencies
└── README.md                     # Technical portfolio interface
🛠️ Technology Stack
Core Language: Python 3.10+

Concurrency Engine: Concurrent Futures (ThreadPoolExecutor)

Data Mining: BeautifulSoup4, Requests, XML ElementTree Parsing

NLP & Feature Engineering: NLTK, Textstat, Pandas

Deployment & UI: Hosted live via Gradio on Hugging Face Spaces

⚙️ Execution Sandbox (How to Run)
Follow these streamlined steps to clone, configure, and execute the production pipeline on your local architecture:

1. Download and Clone the Project
Clone the repository from GitHub and navigate into the root project directory:

Bash
git clone [https://github.com/Alhareth/arabic-news-scraper.git](https://github.com/Alhareth/arabic-news-scraper.git)
cd arabic-news-scraper
2. Environment Specifications Setup
Install all required third-party libraries and NLP dependencies written in the standard configuration file using pip:

Bash
pip install -r requirements.txt
3. Practical Code Execution Sample
You can now programmatically import the core pipeline engines directly into any custom script to scrape and extract features dynamically:

Python
from src.scraper import fetch_sitemap_urls, run_concurrent_pipeline
from src.feature_extractor import compute_text_features

# 1. Fetch historical article sub-sitemaps dynamically
target_urls = fetch_sitemap_urls("[https://sabq.org/sitemap.xml](https://sabq.org/sitemap.xml)")[:20]

# 2. Execute the multi-threaded production crawling run (Extracting 20 articles)
scraped_dataset = run_concurrent_pipeline(target_urls)

# 3. Compute structural NLP metrics on any extracted text sample
if scraped_dataset:
    sample_text = scraped_dataset[0]["cleaned_text"]
    analytics = compute_text_features(sample_text)
    print("Linguistic Analytics Output:", analytics)
📝 Key Engineering Takeaways
polite Scraping Boundaries: Optimized the concurrency workload (max_workers=10) combined with automated random jitter delays to prevent trigger-based firewall blockages.

Deterministic Data Integrity: Mitigated structural text variations by tracking metadata patterns inside JavaScript injection points (application/ld+json), stabilizing data acquisition success rates.

Enterprise Integration: Structured the code natively into functional packages (src/) making it production-ready and fully importable by external applications or backend APIs.

📄 License
This system architecture and code deployment pipelines are completely open-sourced under the MIT License.