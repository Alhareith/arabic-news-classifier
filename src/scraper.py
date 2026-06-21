import requests
import time
import random
import logging
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.config import HEADERS, DELAY, MAX_WORKERS
from src.preprocessor import clean_text, extract_from_script_tags

def fetch_sitemap_urls(sitemap_url):
    """جلب قائمة الروابط الفرعية من الـ Sitemap الرئيسي"""
    try:
        response = requests.get(sitemap_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        return urls
    except Exception as e:
        logging.error(f"Error fetching sitemap {sitemap_url}: {e}")
        return []

def scrape_article(url):
    """سحب مقال واحد وتنظيفه بالكامل مع إدارة الأخطاء لضمان استقرار الـ Pipeline"""
    try:
        time.sleep(random.uniform(0.5, DELAY))  # تأخير مهذب لتفادي الحظر
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # محاولة استخراج النص من الـ Script tags أولاً ثم من الـ HTML التقليدي
        body_text = extract_from_script_tags(soup)
        if not body_text:
            paragraphs = soup.find_all('p')
            body_text = " ".join([p.get_text() for p in paragraphs])
            
        cleaned_body = clean_text(body_text)
        
        return {
            "url": url,
            "raw_text": body_text,
            "cleaned_text": cleaned_body
        }
    except Exception as e:
        logging.error(f"Error scraping article {url}: {e}")
        return None

def run_concurrent_pipeline(urls):
    """تشغيل خط الإنتاج المتزامن لجمع البيانات بسرعة قصوى وكفاءة عالية"""
    articles = []
    logging.info(f"Starting pipeline for {len(urls)} URLs using {MAX_WORKERS} workers...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(scrape_article, url): url for url in urls}
        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                articles.append(result)
                
    logging.info(f"Pipeline finished! Successfully scraped {len(articles)} articles.")
    return articles