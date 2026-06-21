import nltk
from textstat import flesch_reading_ease

# تحميل الحزم الأساسية لـ NLTK عند استدعاء الملف
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def compute_text_features(text):
    """حساب عدد الكلمات، الجمل، ومتوسط الطول، ومقياس سهولة القراءة الفليشية"""
    if not text or len(text.strip()) == 0:
        return {"word_count": 0, "sentence_count": 0, "avg_sentence_length": 0, "flesch_score": 0}
        
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    
    word_count = len(words)
    sentence_count = len(sentences) if len(sentences) > 0 else 1
    avg_sentence_length = word_count / sentence_count
    
    # حساب مقياس Flesch Reading Ease
    flesch_score = flesch_reading_ease(text)
    
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_sentence_length": round(avg_sentence_length, 2),
        "flesch_score": flesch_score
    }