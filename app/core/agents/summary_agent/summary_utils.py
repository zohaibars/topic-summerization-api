import re
import logging
from app.utils.models import Topics

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

class TopicsOutputParser():
    def __init__(self, text: str) -> None:
        self.text = text
        
    def parse(self, topics: str) -> str:
        possible_matches = [
            r'\[Response Format START\](.*?)\[Response Format END\]',
            r'These are the topics:(.*?)\[Response Format END\]',
            r'These are the topics:(.*)'
        ]
        logger.info("Parsing summaries")
        try:
            match = None
            for pattern in possible_matches:
                match = re.search(pattern, topics, re.DOTALL)
                if match:
                    break
            
            if not match:
                topics = Topics(topic_summaries=[{}])
                return topics
            content = match.group(1).strip()

            topic_summarize = []
            topics = re.split(r'\*\*(.*?)\*\*', content)

            for i in range(1, len(topics), 2):
                topic = topics[i].strip()
                summary = topics[i + 1].strip()
                topic_summarize.append({"topic": topic, "summary": summary})
            topics  = Topics(topic_summaries=topic_summarize)
            logger.info("Parsed Successfully")
            return topics
        except Exception as ex:
            logger.error(f"While parsing summaries: {ex}")
            return Topics(topic_summaries=[{}])

urdu_proper_nouns = [
    "پاکستان",    # Pakistan
    "اسلام آباد",  # Islamabad
    "لاہور",       # Lahore
    "کراچی",       # Karachi
    "پشاور",       # Peshawar
    "کوئٹہ",       # Quetta
    "فیصل آباد",   # Faisalabad
    "ملتان",       # Multan
    "راولپنڈی",    # Rawalpindi
    "سوات",        # Swat
    "گلگت",        # Gilgit
    "بنی گالا",    # Bani Gala
    "گوجرانوالہ",  # Gujranwala
    "شیخوپورہ",    # Sheikhupura
    "سیالکوٹ",     # Sialkot
    "چکوال",       # Chakwal
    "بھاولپور",    # Bahawalpur
    "ہنزہ",        # Hunza
    "مری",         # Murree
    "نیلم",        # Neelum
    "کشمیر",       # Kashmir
    "عمران خان",   # Imran Khan
    "قائد اعظم",    # Quaid-e-Azam (Muhammad Ali Jinnah)
    "علامہ اقبال",  # Allama Iqbal
    "شاہ رخ خان",  # Shahrukh Khan
    "ماہرہ خان",   # Mahira Khan
    "بینظیر بھٹو", # Benazir Bhutto
    "بلال عباس",   # Bilal Abbas
    "نوید انجم",   # Naveed Anjum
    "فیروز خان",   # Feroze Khan
    "منیب بٹ",     # Muneeb Butt
    "ہمایوں سعید", # Humayun Saeed
    "نوشین شاہ",   # Nousheen Shah
    "نیلم منیر",   # Neelam Muneer
    "ہانیہ عامر",  # Hania Amir
    "عائشہ خان"    # Ayesha Khan
]

urdu_adjectives = [
    "خوبصورت",    # Beautiful
    "بہادر",      # Brave
    "تیز",        # Fast
    "ہوشیار",     # Clever
    "محنتی",      # Hardworking
    "مہربان",     # Kind
    "دلچسپ",      # Interesting
    "پیارا",      # Lovely
    "ذہین",       # Intelligent
    "صابر",       # Patient
    "خوش",        # Happy
    "اداس",       # Sad
    "طاقتور",     # Strong
    "کمزور",      # Weak
    "چالاک",      # Cunning
    "نیک",        # Good
    "برا",        # Bad
    "غصہ",        # Angry
    "پریشان",     # Worried
    "خوفناک",     # Terrifying
    "مزیدار",     # Delicious
    "خوشبو",      # Fragrant
    "مددگار",     # Helpful
    "مفید",       # Useful
    "معقول",      # Reasonable
    "بیمار",      # Sick
    "صحتمند",     # Healthy
    "امیر",       # Rich
    "غریب",       # Poor
    "معصوم",      # Innocent
    "بڑا",        # Big
    "چھوٹا",      # Small
    "لمبا",       # Tall/Long
    "چھوٹا",      # Short
    "گہرا",       # Deep
    "چوڑا",       # Wide
    "تنگ",        # Narrow
    "گرم",        # Hot
    "ٹھنڈا",      # Cold
    "سرد",        # Chilly
    "ہلکا",       # Light
    "بھاری",      # Heavy
    "مہنگا",      # Expensive
    "سستا",       # Cheap
    "مضبوط",      # Strong
    "کمزور",      # Weak
    "بےحد",       # Infinite
    "نیا",        # New
    "پرانا",      # Old
    "خوبرو",      # Handsome
    "دلیر",       # Gallant
    "پرسکون",     # Calm
    "شاندار",     # Magnificent
    "خوبصورت",    # Beautiful
    "روشن",       # Bright
    "اندھیرا",    # Dark
    "اچھا",       # Good
    "برابر",      # Equal
    "غیر مساوی",  # Unequal
    "فطری",       # Natural
    "مصنوعی",     # Artificial
    "بنیادی",     # Basic
    "مشکل",       # Difficult
    "آسان",       # Easy
    "دلکش",       # Charming
    "سچے",        # True
    "جھوٹا",      # False
    "بے غرض",     # Selfless
    "خود غرض",    # Selfish
    "مخلص",       # Sincere
    "غیر مخلص"    # Insincere
]

