import time
import random
import html
import ssl
import json
import os
import re
import requests
import cloudscraper
from bs4 import BeautifulSoup

# ⚠️ التوكن ومعرف الشات الخاص بك
TOKEN = "8996279782:AAEJ-n3vP4K9bts15GC0_htKMceRC4yHj8E"
CHAT = "5124680786"

DB_FILE = "custom_products_prices.json"

# قائمة الروابط المحددة
TARGET_URLS = [
    "https://www.amazon.eg/dp/B09WKV3CTR",
    "https://www.amazon.eg/dp/B09LTK7V6T",
    "https://www.amazon.eg/dp/B0CGM871S9",
    "https://www.amazon.eg/dp/B0D4MCPHMQ",
    "https://www.amazon.eg/dp/B0D2PG2NT6",
    "https://www.amazon.eg/dp/B0H966K97T",
    "https://www.amazon.eg/dp/B0D5P9VWDP",
    "https://www.amazon.eg/dp/B0GCGRX6WW",
    "https://www.amazon.eg/dp/B0G2SSJFXF",
    "https://www.amazon.eg/dp/B0B3DQK14Z",
    "https://www.amazon.eg/dp/B0H5CT6SY3",
    "https://www.amazon.eg/dp/B0FQCQCXNB",
    "https://www.amazon.eg/dp/B0CYXLYW4Y",
    "https://www.amazon.eg/dp/B08WJMQDVZ",
    "https://www.amazon.eg/dp/B01J5KTUJW",
    "https://www.amazon.eg/dp/B0CK1GFDS2",
    "https://www.amazon.eg/dp/B0D9W9T3WW",
    "https://www.amazon.eg/dp/B0CLVJBJZ5",
    "https://www.amazon.eg/dp/B0H1K88MHN",
    "https://www.amazon.eg/dp/B0G4XJGW77",
    "https://www.amazon.eg/dp/B0D83Q4927",
    "https://www.amazon.eg/dp/B0F7FT56BZ",
    "https://www.amazon.eg/dp/B0FPMJHCJ9",
    "https://www.amazon.eg/dp/B0DJFX1VJH",
    "https://www.amazon.eg/dp/B0FD8VGW4V",
    "https://www.amazon.eg/dp/B0DW6KJG8P",
    "https://www.amazon.eg/dp/B0HBX7ZN7Z",
    "https://www.amazon.eg/dp/B0FYGNR4RJ",
    "https://www.amazon.eg/dp/B0FLD7MTKS",
    "https://www.amazon.eg/dp/B096R1QJZ7",
    "https://www.amazon.eg/dp/B0DDL5H4KB",
    "https://www.amazon.eg/dp/B0HN2F9R4C",
    "https://www.amazon.eg/dp/B0FSXYHSJW",
    "https://www.amazon.eg/dp/B07CMC349B",
    "https://www.amazon.eg/dp/B0CLDT2JZ8",
    "https://www.amazon.eg/dp/B0BVBWS548",
    "https://www.amazon.eg/dp/B0H4P1KK2H",
    "https://www.amazon.eg/dp/B0D6YYQYTH",
    "https://www.amazon.eg/dp/B08SQWNRN6",
    "https://www.amazon.eg/dp/B0H9619RJY",
    "https://www.amazon.eg/dp/B0D2B7MX4L",
    "https://www.amazon.eg/dp/B0BZZWF4MY",
    "https://www.amazon.eg/dp/B09BDMWZY3",
    "https://www.amazon.eg/dp/B09GFDT5HB",
    "https://www.amazon.eg/dp/B08WJS7RHC",
    "https://www.amazon.eg/dp/B0CZZ31VSQ",
    "https://www.amazon.eg/dp/B0GFXJLSZ8",
    "https://www.amazon.eg/dp/B0BDX5KB2X",
    "https://www.amazon.eg/dp/B0FFGZC76X",
    "https://www.amazon.eg/dp/B0DKFJHPK7",
    "https://www.amazon.eg/dp/B0B3DVZDMP",
    "https://www.amazon.eg/dp/B01KXFKS6M",
    "https://www.amazon.eg/dp/B0FMQ9X62M",
    "https://www.amazon.eg/dp/B0957LVN5D",
    "https://www.amazon.eg/dp/B0FMP7ZD2N",
    "https://www.amazon.eg/dp/B091J84LT2",
    "https://www.amazon.eg/dp/B0FXGGBYZY",
    "https://www.amazon.eg/dp/B0CZMWGXW3",
    "https://www.amazon.eg/dp/B0FQKVKVV9",
    "https://www.amazon.eg/dp/B0DZX6H6BM",
    "https://www.amazon.eg/dp/B0C3JYVPDJ",
    "https://www.amazon.eg/dp/B0BRGJ3PGF",
    "https://www.amazon.eg/dp/B096MSRDMR",
    "https://www.amazon.eg/dp/B0FQKJN6LC",
    "https://www.amazon.eg/dp/B0C58PCMN3",
    "https://www.amazon.eg/dp/B00821QXR8",
    "https://www.amazon.eg/dp/B0H4LQRRBH",
    "https://www.amazon.eg/dp/B0DS1JLSMV",
    "https://www.amazon.eg/dp/B096L6G3VQ",
    "https://www.amazon.eg/dp/B0HC82BGFV",
    "https://www.amazon.eg/dp/B0DH4SB3XX",
    "https://www.amazon.eg/dp/B098S2WYY2",
    "https://www.amazon.eg/dp/B0F6D39FFS",
    "https://www.amazon.eg/dp/B0FM89RFC1",
    "https://www.amazon.eg/dp/B0DPDMCMY7",
    "https://www.amazon.eg/dp/B0G5BHJFHN",
    "https://www.amazon.eg/dp/B0FQ66V61K",
    "https://www.amazon.eg/dp/B0G7221W2X",
    "https://www.amazon.eg/dp/B0FSX5QTZT",
    "https://www.amazon.eg/dp/B0CJGMSPHG",
    "https://www.amazon.eg/dp/B0DQ6DPZBJ",
    "https://www.amazon.eg/dp/B0DKCFKPPH",
    "https://www.amazon.eg/dp/B0D8PR9QJH",
    "https://www.amazon.eg/dp/B0FQCJLTHC",
    "https://www.amazon.eg/dp/B0CHN1W1YP",
    "https://www.amazon.eg/dp/B0FSWWNB6N",
    "https://www.amazon.eg/dp/B0FSXJ3GF4",
    "https://www.amazon.eg/dp/B0H9JGPSXK",
    "https://www.amazon.eg/dp/B0C5KKCCR9",
    "https://www.amazon.eg/dp/B0CJYG4SX7",
    "https://www.amazon.eg/dp/B08WJPYF9M",
    "https://www.amazon.eg/dp/B09BG43W14",
    "https://www.amazon.eg/dp/B0CRQCWY94",
    "https://www.amazon.eg/dp/B0FD8L33BB",
    "https://www.amazon.eg/dp/B0GD8F8VMP",
    "https://www.amazon.eg/dp/B08Y97V1RK",
    "https://www.amazon.eg/dp/B0DP3N8GPL",
    "https://www.amazon.eg/dp/B0DXBZ434R",
    "https://www.amazon.eg/dp/B0HJZR3V5T",
    "https://www.amazon.eg/dp/B01KXFGXU2"
]

H = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive"
}

AR = str.maketrans("٠١٢٣٤٥٦٧٨٩٫٬", "0123456789.,")

# استرجاع قاعدة البيانات المخزنة مسبقاً
if os.path.exists(DB_FILE):
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            last_prices = json.load(f)
        print(f"📂 تم استرجاع {len(last_prices)} منتج محفوظ من قبل.")
    except Exception:
        last_prices = {}
else:
    last_prices = {}

def save_prices():
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(last_prices, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("خطأ في حفظ الملف:", e)

def create_scraper():
    ctx = ssl.create_default_context()
    ctx.set_ciphers("DEFAULT@SECLEVEL=1")
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "desktop": True},
        ssl_context=ctx
    )
    scraper.headers.update(H)
    return scraper

scraper = create_scraper()

def send(msg):
    u = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        res = requests.post(
            u, 
            json={"chat_id": CHAT, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": False}, 
            timeout=15
        )
        if res.status_code != 200:
            print("مشكلة من تيليجرام:", res.text)
        time.sleep(1.5)
    except Exception as e:
        print("خطأ في إرسال تيليجرام:", e)

def clean(text):
    x = text.translate(AR).replace(",", "")
    m = re.search(r"\d+(?:\.\d+)?", x)
    return float(m.group(0)) if m else None

def extract_product_name(s, asin):
    title_tag = s.select_one("#productTitle")
    if title_tag:
        return title_tag.get_text(strip=True)
    return f"منتج أمازون ({asin})"

def extract_price(s):
    selectors = [
        ".a-price .a-offscreen", 
        "#priceblock_ourprice", 
        "#priceblock_dealprice", 
        ".a-price-whole", 
        ".a-color-price"
    ]
    for selector in selectors:
        tag = s.select_one(selector)
        if tag:
            p = clean(tag.get_text())
            if p is not None and p > 0:
                return p
    return None

def check_products():
    global scraper
    print(f"\n[{time.strftime('%H:%M:%S')}] جاري فحص الروابط المحددة ({len(TARGET_URLS)} رابط)...")
    
    if not scraper.cookies:
        try:
            scraper.get("https://www.amazon.eg/", timeout=20)
            time.sleep(random.uniform(2, 4))
        except:
            pass

    success_count = 0
    for url in TARGET_URLS:
        match = re.search(r"/dp/([A-Z0-9]{10})", url)
        if not match:
            continue
        asin = match.group(1)
        
        try:
            r = scraper.get(url, timeout=25)
            if r.status_code != 200:
                print(f"⚠️ تحذير: الـ ASIN {asin} رد بالكود {r.status_code}")
                time.sleep(random.uniform(2, 4))
                continue
                
            if "api-services-support@amazon.com" in r.text or "Enter the characters you see below" in r.text:
                print("⚠️ أمازون طلبت كابتشا. جاري تجديد الجلسة...")
                scraper = create_scraper()
                time.sleep(5)
                continue

            s = BeautifulSoup(r.text, "html.parser")
            price = extract_price(s)
            if price is None:
                print(f"⚠️ فشل في استخراج السعر لـ {asin}")
                time.sleep(random.uniform(1, 3))
                continue

            raw_name = extract_product_name(s, asin)
            safe_name = html.escape(raw_name)
            old_price = last_prices.get(asin)

            if old_price is None:
                last_prices[asin] = price
                print(f"✨ رُصد لأول مرة: {raw_name[:30]}... | السعر: {price} ج.م")
                msg = (
                    f"📦 <b>متابعة منتج جديد!</b>\n\n"
                    f"🛒 <a href='{url}'>{safe_name}</a>\n"
                    f"💰 السعر: <b>{price} ج.م</b>"
                )
                send(msg)
                
            elif price != old_price:
                diff = price - old_price
                ar_trend = "📉 نزل" if diff < 0 else "📈 زاد"
                print(f"🔥 تغير سعر: {raw_name[:30]}... من {old_price} إلى {price} ج.م")
                msg = (
                    f"🚨 <b>تغيير في السعر!</b>\n\n"
                    f"🛒 <a href='{url}'>{safe_name}</a>\n"
                    f"الحالة: {ar_trend}\n"
                    f"من: <s>{old_price}</s> ج.م\n"
                    f"إلى: <b>{price} ج.م</b>"
                )
                send(msg)
                last_prices[asin] = price
            else:
                print(f"✔️ مستقر: {raw_name[:30]}... | السعر: {price} ج.م")

            success_count += 1
            time.sleep(random.uniform(3, 6))
            
        except Exception as e:
            print(f"خطأ أثناء فحص الرابط {url}: {e}")
            time.sleep(5)

    if success_count > 0:
        save_prices()
    
    print(f"✅ انتهى الفحص بنجاح لـ {success_count} منتج.")

print("مراقبة الروابط المخصصة شغالة...")
while True:
    check_products()
    sleep_time = random.randint(1800, 3600)
    print(f"⏳ انتظار الجولة القادمة بعد {sleep_time // 60} دقيقة...")
    time.sleep(sleep_time)
    
