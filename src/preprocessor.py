import re
import json
from bs4 import BeautifulSoup

def extract_from_script_tags(soup):
    """استخراج النصوص والبيانات الوصفية المضمنة داخل وسم script"""
    script_tags = soup.find_all('script', type='application/ld+json')
    for tag in script_tags:
        try:
            data = json.loads(tag.string)
            if isinstance(data, dict) and 'articleBody' in data:
                return data['articleBody']
        except (json.JSONDecodeError, TypeError):
            continue
    return ""

def clean_text(text):
    """تنظيف النص العربي من الروابط، الرموز التعبيرية، والمسافات الزائدة"""
    if not text:
        return ""
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # إزالة الروابط
    text = re.sub(r'[^\w\s\u0600-\u06FF]', '', text)     # الاحتفاظ بالحروف العربية والمسافات فقط
    text = re.sub(r'\s+', ' ', text).strip()             # إزالة المسافات المتكررة
    return text