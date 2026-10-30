import requests
from bs4 import BeautifulSoup
import time
import re
import random
import json
import os

# ⚠️ التوكن ومعرف الشات الخاص بك
TOKEN = "8996279782:AAEJ-n3vP4K9bts15GC0_htKMceRC4yHj8E"
CHAT = "5124680786"

DB_FILE = "prices_database.json"

LINKS = [
    "https://www.amazon.eg/dp/B0H17ZVHBY",
    "https://www.amazon.eg/dp/B0H17VFW5L",
    "https://www.amazon.eg/dp/B0HFN2GVGX",
    "https://www.amazon.eg/dp/B09G3CNVWV",
    "https://www.amazon.eg/dp/B0HFN5DCYW",
    "https://www.amazon.eg/dp/B0FTMJJQB8",
    "https://www.amazon.eg/dp/B0HBG81LXL",
    "https://www.amazon.eg/dp/B0HFN4VB5D",
    "https://www.amazon.eg/dp/B0B1B793GY",
    "https://www.amazon.eg/dp/B08X63FTM3",
    "https://www.amazon.eg/dp/B0FBKB2BY6",
    "https://www.amazon.eg/dp/B0DBR2DRXP",
    "https://www.amazon.eg/dp/B0H17SP4XR",
    "https://www.amazon.eg/dp/B0H1872WDR",
    "https://www.amazon.eg/dp/B08Z49DXMD",
    "https://www.amazon.eg/dp/B09G3DNHQZ",
    "https://www.amazon.eg/dp/B0F4D6HCBQ",
    "https://www.amazon.eg/dp/B098MM2D6K",
    "https://www.amazon.eg/dp/B0GWQCX4BF",
    "https://www.amazon.eg/dp/B0C797ZKHW",
    "https://www.amazon.eg/dp/B0BXPKSVFQ",
    "https://www.amazon.eg/dp/B0BC6XC8HF",
    "https://www.amazon.eg/dp/B0F26MT6HH",
    "https://www.amazon.eg/dp/B0H185KP31",
    "https://www.amazon.eg/dp/B0FTMHZYTN",
    "https://www.amazon.eg/dp/B08Y8YTQGP",
    "https://www.amazon.eg/dp/B0BXPPM3HR",
    "https://www.amazon.eg/dp/B0DBR36RM9",
    "https://www.amazon.eg/dp/B0H4H4P2RR",
    "https://www.amazon.eg/dp/B0GZQYBX2D",
    "https://www.amazon.eg/dp/B094HJ4JSH",
    "https://www.amazon.eg/dp/B0GFFCKN9X",
    "https://www.amazon.eg/dp/B08Z485HYS",
    "https://www.amazon.eg/dp/B0GHNVXZ7C",
    "https://www.amazon.eg/dp/B0FTMJ3145",
    "https://www.amazon.eg/dp/B0CK64CHJY",
    "https://www.amazon.eg/dp/B0HKJRHGHG",
    "https://www.amazon.eg/dp/B0CBVPX5CZ",
    "https://www.amazon.eg/dp/B0CVQBBPSK",
    "https://www.amazon.eg/dp/B091J53S75",
    "https://www.amazon.eg/dp/B0GSYK242Y",
    "https://www.amazon.eg/dp/B0FTMK4J7S",
    "https://www.amazon.eg/dp/B0FTMKXC6P",
    "https://www.amazon.eg/dp/B08YY12TFY",
    "https://www.amazon.eg/dp/B0GYJF5Z7F",
    "https://www.amazon.eg/dp/B0BXPMRTM5",
    "https://www.amazon.eg/dp/B0CB8C4MZX",
    "https://www.amazon.eg/dp/B0HKS1DYWF",
    "https://www.amazon.eg/dp/B07MVWDB2R",
    "https://www.amazon.eg/dp/B0H6CMT2YF",
    "https://www.amazon.eg/dp/B0H6BVPPSD",
    "https://www.amazon.eg/dp/B0DQ18YMVK",
    "https://www.amazon.eg/dp/B0CX4KQF17",
    "https://www.amazon.eg/dp/B0BRY69ZNT",
    "https://www.amazon.eg/dp/B0CWFGMN4B",
    "https://www.amazon.eg/dp/B0HKFW34GX",
    "https://www.amazon.eg/dp/B0C7N3XQPN",
    "https://www.amazon.eg/dp/B0H17YLM6F",
    "https://www.amazon.eg/dp/B092TZPJ4Q",
    "https://www.amazon.eg/dp/B0C6HX6KCJ",
    "https://www.amazon.eg/dp/B0CW1NYQ7N",
    "https://www.amazon.eg/dp/B0BNZBHQLH",
    "https://www.amazon.eg/dp/B0F92WDNNN",
    "https://www.amazon.eg/dp/B0BYTJV3PV",
    "https://www.amazon.eg/dp/B0H184SH8L",
    "https://www.amazon.eg/dp/B0B1YRH6G5",
    "https://www.amazon.eg/dp/B0FV8HB9CB",
    "https://www.amazon.eg/dp/B0H187XMWN",
    "https://www.amazon.eg/dp/B0H88B7LXT",
    "https://www.amazon.eg/dp/B08YY228BC",
    "https://www.amazon.eg/dp/B0D4734GYT",
    "https://www.amazon.eg/dp/B0C6RB94VW",
    "https://www.amazon.eg/dp/B0DGY1HD3B",
    "https://www.amazon.eg/dp/B0H184YYDP",
    "https://www.amazon.eg/dp/B0CK72V25C",
    "https://www.amazon.eg/dp/B0F92XRBYV",
    "https://www.amazon.eg/dp/B09NW9R7L4",
    "https://www.amazon.eg/dp/B0H7N8511J",
    "https://www.amazon.eg/dp/B0H17ZFJBW",
    "https://www.amazon.eg/dp/B0FRMS67DC",
    "https://www.amazon.eg/dp/B0F5B7PLMF",
    "https://www.amazon.eg/dp/B0H4GVVQYP",
    "https://www.amazon.eg/dp/B0HKSGZ8ZR",
    "https://www.amazon.eg/dp/B0CN9Q3MY3",
    "https://www.amazon.eg/dp/B09Z4LPZDQ",
    "https://www.amazon.eg/dp/B0BYXHJXZL",
    "https://www.amazon.eg/dp/B0H95FWM7M",
    "https://www.amazon.eg/dp/B0GY922Z1X",
    "https://www.amazon.eg/dp/B0CSX89CM1",
    "https://www.amazon.eg/dp/B0BQCDNMNQ",
    "https://www.amazon.eg/dp/B091JBDYT9",
    "https://www.amazon.eg/dp/B0BC6V1MX5",
    "https://www.amazon.eg/dp/B0H17VMNFK",
    "https://www.amazon.eg/dp/B0FTMKB2B3",
    "https://www.amazon.eg/dp/B09NW9HX9S",
    "https://www.amazon.eg/dp/B08YNPDYCZ",
    "https://www.amazon.eg/dp/B0BZ5KY8YZ",
    "https://www.amazon.eg/dp/B0F14271PD",
    "https://www.amazon.eg/dp/B0FN9SM1LK",
    "https://www.amazon.eg/dp/B098TTX8ST",
    "https://www.amazon.eg/dp/B0971DYZND",
    "https://www.amazon.eg/dp/B0CPVQ6YJ4",
    "https://www.amazon.eg/dp/B09NW9SYXN",
    "https://www.amazon.eg/dp/B0D4727X69",
    "https://www.amazon.eg/dp/B0GN54LVLD",
    "https://www.amazon.eg/dp/B0F4HZ424M",
    "https://www.amazon.eg/dp/B0BTGQ5JF4"
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive"
    }

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    try:
        requests.post(url, data=payload, timeout=15)
    except Exception as e:
        print(f"⚠️ خطأ في إرسال التنبيه: {e}")

def load_database():
    """تحميل الأسعار المسجلة مسبقاً"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def save_database(db):
    """حفظ الأسعار في الملف"""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

def get_current_price(url):
    """جلب السعر الحالي للمنتج فقط"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            headers = get_random_headers()
            response = requests.get(url, headers=headers, timeout=25)
            
            if "captcha" in response.text.lower() or response.status_code == 503:
                time.sleep(random.randint(15, 25))
                continue
                
            if response.status_code != 200:
                return None
                
            soup = BeautifulSoup(response.text, "html.parser")
            
            title_element = soup.find(id="productTitle")
            title = title_element.get_text().strip() if title_element else "منتج بدون عنوان"
            
            price = None
            price_whole = soup.find("span", class_="a-price-whole")
            price_fraction = soup.find("span", class_="a-price-fraction")
            
            if price_whole:
                p_text = price_whole.get_text().replace(",", "").strip()
                if price_fraction:
                    p_text += "." + price_fraction.get_text().strip()
                price = float(re.findall(r"[\d\.]+", p_text)[0])
                
            return {"title": title, "price": price}
        except:
            time.sleep(5)
    return None

def smart_monitor():
    database = load_database()
    print(f"🚀 بدء التشغيل الذكي لمراقبة {len(LINKS)} منتج...")
    send_telegram_message(f"🤖 <b>تم بدء تشغيل بوت مراقبة الأسعار الذكي!</b>\n📊 يتم فحص الأسعار ومقارنتها بقاعدة البيانات.")

    while True:
        for index, link in enumerate(LINKS, 1):
            product_data = get_current_price(link)
            
            if product_data and product_data["price"]:
                current_price = product_data["price"]
                product_title = product_data["title"]
                
                # لو المنتج مش متسجل قبل كده، نسجل سعره الحالي كمرجع أساسي في الصمت
                if link not in database:
                    database[link] = {
                        "title": product_title,
                        "base_price": current_price
                    }
                    save_database(database)
                    print(f"📥 [تسجيل أولي]: تم حفظ سعر المنتج ({index}/{len(LINKS)}) بسعر: {current_price} ج.م")
                else:
                    # لو متسجل، نقارن السعر الحالي بالسعر الأساسي المسجل
                    base_price = database[link]["base_price"]
                    
                    if base_price > current_price:
                        drop_percentage = ((base_price - current_price) / base_price) * 100
                        print(f"📉 فحص ({index}/{len(LINKS)}): السعر القديم {base_price} -> الحالي {current_price} (خصم: {drop_percentage:.1f}%)")
                        
                        # لو الخصم 20% أو أكثر مقارنة بالسعر المسجل
                        if drop_percentage >= 20:
                            msg = (
                                f"🔥 <b>لقطة! انخفض السعر بنسبة 20% أو أكثر!</b> 🔥\n\n"
                                f"📌 <b>المنتج:</b> {product_title}\n"
                                f"💰 <b>السعر الجديد:</b> {current_price} ج.م\n"
                                f"🏷️ <b>السعر المسجل سابقاً:</b> {base_price} ج.م\n"
                                f"📉 <b>نسبة الانخفاض:</b> <code>{drop_percentage:.1f}%</code>\n\n"
                                f"🔗 <a href='{link}'>اضغط هنا لفتح المنتج والشراء</a>"
                            )
                            send_telegram_message(msg)
                    else:
                        pass
            
            # فاصل زمني آمن بين كل منتج والتاني
            time.sleep(random.randint(12, 20))
            
        print("\n🔄 انتهت دورة الفحص كاملة في صمت. استراحة لمدة 5 دقائق ثم الدورة التالية...")
        time.sleep(300)

if __name__ == "__main__":
    smart_monitor()
