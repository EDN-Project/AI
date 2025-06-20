# استخدم نسخة Python الرسمية الكاملة
FROM python:3.12

# تعيين مجلد العمل داخل الحاوية
WORKDIR /detector

# نسخ ملفات المشروع إلى الحاوية
COPY . /detector

# تثبيت المتطلبات
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# إفشاء البورت المستخدم بواسطة Flask
EXPOSE 5000

# أمر التشغيل
CMD ["python", "detector.py"]