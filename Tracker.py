ى الفحص بنجاح لـ {success_count} منتج.")

print("مراقبة الروابط المخصصة شغالة...")
while True:
    check_products()
    sleep_time = random.randint(1800, 3600)
    print(f"⏳ انتظار الجولة القادمة بعد {sleep_time // 60} دقيقة...")
    time.sleep(sleep_time)
    
