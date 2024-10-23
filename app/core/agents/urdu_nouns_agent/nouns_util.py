import re
import pendulum
import logging
from app.utils.models import Nouns
from app.utils.settings import DEBUG
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Urdu_stop_words = [
    "آئے", "آتا", "آتی", "آتے", "آدھا", "آدھی", "آدھے", "آپ", "آپس", "آگیا", "آگئی", "آگئے", "آگے", "اگر", "آخر", "آخرکار", "اکثر", "اکیلے",
    "اٹھ", "اٹھا", "اٹھاو", "اٹھایا", "اٹھائے", "اٹھتی", "اٹھتے", "اٹھنا", "اٹھنے", "اٹھو", "اٹھکر", "اڈا", "ادھر", "ارے", "اس", "اسکا", "اسکی",
    "اسکے", "اسلیے", "اسمیں", "اسے", "اسی", "اصل", "اصل", "اصول", "افسوس", "الگ", "اللہ", "ان", "اندر", "انہیں", "انہوں", "انہی", "انی", "انکا",
    "انکی", "انکے", "انھیں", "انھو", "انھی", "انکا", "انکی", "انکے", "اپ", "اپنا", "اپنے", "اپنی", "اب", "ادھر", "ارد", "اوپر", "اور", "ابھی", 
     "ایسی", "ایسے", "ایسا", "ایسی", "ایک", "اچھی", "اچھا", "اچھے", "بد", "برے", "بڑی", "بڑا", "بڑے", "بس", "بعض", "بغیر", "بعد", "بعدازاں",
    "بغیر", "براہ", "بہت", "بہت", "بہتر", "بی", "بے", "تحت", "تھ", "تھا", "تھی", "تھے", "تمام", "تمہیں", "تمھارا", "تمھاری", "تمھارے", "تو",
    "تین", "جا", "جاتی", "جاتے", "جانے", "جائے", "جاؤ", "جائے", "جتنے", "جتنا", "جسے", "حالانکہ", "حال", "حاصل", "حالت", "خود", "خصوصا",
    "در", "دراز", "درست", "دور", "دو", "دوپہر", "دوران", "دوسرا", "دوسری", "دوسرے", "دیر", "دے", "دی", "دیا", "دیگر", "دیتا", "دیتی", "دیتے", 
    "دینا", "دینی", "دینے", "ذریعے", "ذرا", "راضی", "رہا", "رہتا", "رہتی", "رہتے", "رہنا", "رہنے", "رہیں", "رہی", "رہے", "رو", "روز", "زیادہ",
    "سات", "ساتھ", "سخت", "سکتا", "سکتی", "سکتے", "صرف", "صبح", "سے", "سو", "سورج", "سکیں", "شاید", "شام", "صبح", "صحیح", "طرح", "طور", "طرف", 
    "طریقہ", "طور", "علاوہ", "عنقریب", "فوری", "فی", "لئے", "لئے", "لہذا", "لیکن", "متعدد", "مجھے", "محسوس", "مجبور", "مجھے", "مزید", "مستقبل", 
    "مسائل", "مقام", "مل", "ملتا", "ملتی", "ملتے", "ملنا", "ملنے", "ملی", "ملے", "ممکن", "مندرجہ", "مندرجہ", "مندرجہ", "مندرجہ", "منزل", "میری",
    "میاں", "میں", "ن", "نا", "نہیں", "نہ", "نہایت", "نتیجہ", "نظر", "نظر", "نظر", "کا", "بھی", "نظام", "نقش", "نوعیت", "نہ", "نہایت", "نہ", "ہاں",
    "ہوں", "ہی", "ہو", "ہوئے", "ہوتا", "ہوتی", "ہوتے", "ہونا", "ہونگے", "ہوں", "ہوگی", "ہوں", "ہیں", "ہے", "وہ", "وغیرہ", "وگرنہ", "والا", "والی", 
    "والے", "وسیع", "وسط", "کو", "کر", "کرتا", "کرتی", "کرتے", "کرنا", "کرنے", "کریں", "کریگا", "کر", "کسی", "کچھ", "کبھی", "کہ", "کہا", "کہتے",
    "کہنا", "کہنے", "کی", "کے", "کیلئے", "کیلیے", "کیوں", "کیا", "کیسے", "کس", "کیسے", "کی", "کوئی", "کہیں", "گا", "گئی", "گئے", "گی", "گیا", "گے"
]

class NounsOutputParser():
    def __init__(self, original_text: str) -> None:
        self.original_text = original_text
        self.processed_text = self.remove_stop_words()
        
    def remove_stop_words(self):
        pattern = r'\b(?:' + '|'.join(map(re.escape, Urdu_stop_words)) + r')\b'
        processed_text = re.sub(pattern, '', self.original_text)
        processed_text = re.sub(r'\s+', ' ', processed_text).strip()
        return processed_text
    
    def find_stop_words(self, nouns_list: list):
        found_words = list(set(Urdu_stop_words) & set(nouns_list))
        pkt_time = pendulum.now('Asia/Karachi')
        formatted_time = pkt_time.format('YYYY-MM-DD HH:mm:ss')        
        logger.info("Stop words found in Nouns:")
        for word in found_words:
            logger.info(word)
            print(word)
        if found_words and DEBUG:
            logger.info("Saving Stop words")
            save_str = f"Time of hullcination:{formatted_time}\n" + ",".join(found_words) + "\n\n"
            with open("stopword_detections.txt", "a") as file:
                file.write(save_str)
        final_list = [noun for noun in nouns_list if noun not in found_words]
        return final_list

    
    def parse(self, text: str) -> str:
        possible_matches = [
            r'\[Response Format Start\]\nNouns:(.*?)\[Response Format End\]',
            r'Nouns:(.*?)\[Response Format End\]',
            r'Nouns:(.*)'
        ]
        
        match = None
        for pattern in possible_matches:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                break
        
        if not match:
            nouns = Nouns(nouns=[], text=self.original_text)
            return nouns
            
        content = match.group(1).strip()
        if "none" in content.lower() or not content:
            nouns = Nouns(nouns=[], text=self.original_text)
            return nouns
        
        content = re.sub(r'\[Response Format End\]$', '', content).strip()
        preprocessed_nouns = [noun.strip() for noun in content.split('\n')]
        postprocesses_nouns =  self.find_stop_words(nouns_list=preprocessed_nouns)
        nouns = Nouns(nouns=postprocesses_nouns, text=self.original_text)
        return nouns 
