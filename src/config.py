import logging

# إعدادات الـ Logging لمراقبة عملية السحب بدقة
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SITEMAP_URL = "https://sabq.org/sitemap.xml"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
DELAY = 1         # زمن التأخير بين الطلبات لتجنب الحظر
MAX_WORKERS = 10  # عدد الـ Threads المتوازية للتسريع