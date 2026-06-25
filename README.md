<p align="center">
  <img src="https://raw.githubusercontent.com/Alhareth/arabic-news-scraper/main/assets/logo.png" alt="Arabic News Classifier" width="150">
</p>

<h1 align="center">🤖 Arabic News Scraper & NLP Pipeline</h1>

<p align="center">
  <strong>نظام متكامل لاستخراج وتصنيف الأخبار العربية باستخدام معالجة اللغات الطبيعية ونماذج الـ Transformers</strong>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/Alhareth/arabic-news-classifier">
    <img src="https://img.shields.io/badge/%F0%9F%9A%80%20Live%20Demo-HuggingFace%20Spaces-ff5500?style=flat-for-the-badge&logo=huggingface&logoColor=white" alt="Live Demo">
  </a>
  <a href="https://github.com/Alhareth/arabic-news-scraper/stargazers">
    <img src="https://img.shields.io/github/stars/Alhareth/arabic-news-scraper?style=flat-for-the-badge&color=yellow&logo=github" alt="Stars">
  </a>
  <a href="https://github.com/Alhareth/arabic-news-scraper/network/members">
    <img src="https://img.shields.io/github/forks/Alhareth/arabic-news-scraper?style=flat-for-the-badge&color=blue&logo=git" alt="Forks">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Transformers-%F0%9F%A4%97%20HuggingFace-yellow?style=flat" alt="Transformers">
  <img src="https://img.shields.io/badge/Concurrency-ThreadPoolExecutor-orange?style=flat&logo=cpu" alt="Concurrency">
  <img src="https://img.shields.io/badge/UI-Gradio%20v6-ff5500?style=flat&logo=gradio&logoColor=white" alt="Gradio">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License">
</p>

---

## ⚡ لمحة سريعة | Overview

| الميزة | التفاصيل التقنية |
| :--- | :--- |
| **النموذج اللغوي (Model)** | `CAMeLBERT` (Fine-tuned for multi-class Arabic text classification)[span_0](start_span)[span_0](end_span) |
| **الأداء (Performance)** | دقة **82.33%** (F1-Macro: **81.56%**)[span_1](start_span)[span_1](end_span) |
| **حجم البيانات (Dataset)** | **41,435** مقالة إخبارية عربية مستخرجة آلياً وبشكل منقح[span_2](start_span)[span_2](end_span) |
| **البيئة والتشغيل (Infrastructure)** | معالجة متزامنة متطورة لجمع البيانات + واجهة حيّة تفاعلية عبر `Gradio` |
| **الترخيص (License)** | MIT مفتوح المصدر بالكامل[span_3](start_span)[span_3](end_span) |

> **🎯 الهدف الاستراتيجي (Core Objective):** بناء خط إنتاج بيانات (Data Pipeline) آمن وقابل للتوسع[span_4](start_span)[span_4](end_span)، يدمج بين تقنيات كشط البيانات عالي الأداء وممارسات معالجة النصوص العربية (Arabic NLP) لخدمة تطبيقات الذكاء الاصطناعي محلياً وعالمياً[span_5](start_span)[span_5](end_span).

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
=======
# arabic-news-classifier
Arabic news classification using CAMeLBERT transformer. Fine-tuned for multi-class text classification of Arabic news article
>>>>>>> c0654cd36b23176980c789077f49346637bb00f4
