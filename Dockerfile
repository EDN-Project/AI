# استخدم نسخة Python الرسمية الكاملة
FROM python:3.12

# تعيين مجلد العمل داخل الحاوية
WORKDIR /detector

# نسخ ملف المتطلبات أولًا (للاستفادة من الكاش في Docker)
COPY requirements.txt .

# تثبيت المتطلبات
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# أمر التشغيل
CMD ["python", "detector.py"]
