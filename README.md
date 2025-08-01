# ✈️ Flight Reservation System

واجهة رسومية بسيطة لحجز الرحلات باستخدام Python و Tkinter و SQLite.  
تم تصميم التطبيق ليكون عصريًا، بسيطًا، وسهل الاستخدام.

---

## 🖥️ الميزات

- حجز رحلات جديدة عبر واجهة بسيطة.
- عرض جميع الحجوزات في جدول تفاعلي.
- تعديل أو حذف الحجز مباشرة من الجدول.
- واجهة رسومية متجاوبة مع دعم ملء الشاشة.
- تخزين البيانات باستخدام SQLite دون الحاجة لقاعدة بيانات خارجية.

---

## 📷 شكل البرنامج

> 💡 نسخة محسّنة مستوحاة من:  
> [Flighty Reserve](https://flighty-reserve-mate.lovable.app/)

---

## 📁 هيكل المشروع

flight_reservation_app/ │ ├── main.py                # نقطة التشغيل الرئيسية ├── home.py                # الصفحة الرئيسية ├── booking.py             # حجز رحلة ├── reservations.py        # عرض الحجوزات ├── edit_reservation.py    # تعديل حجز ├── database.py            # التعامل مع SQLite ├── flights.db             # قاعدة البيانات ├── requirements.txt       # مكتبات المشروع └── README.md              # هذا الملف

---

## 🚀 تشغيل المشروع

1. تأكد من وجود Python 3.8 أو أعلى
2. فعّل البيئة الافتراضية (اختياري):
   `bash
   python -m venv venv
   source venv/bin/activate  # على ويندوز: venv\Scripts\activate

3. ثبّت المتطلبات:

pip install -r requirements.txt


4. شغّل البرنامج:

python main.py


---

✅ المتطلبات

tkinter (يأتي مع Python)

Pillow (لعرض الخلفيات أو الصور، إن وُجدت)

---

🛠️ مستقبلًا

دعم واجهة عربية/إنجليزية.

تصدير بيانات الحجز إلى PDF.

إضافة نظام تسجيل دخول للمستخدمين.

---
📄 الترخيص

مشروع مفتوح المصدر لأغراض تعليمية فقط
🔗 GitHub Repository: https://github.com/MohamedAshraf2710/flightbooking