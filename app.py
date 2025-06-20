from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
from ultralytics import YOLO

# إعداد التطبيق
app = Flask(__name__)
CORS(app)

# تحميل الموديل
model = YOLO("strawberry_detector.pt")
print("Classes:", model.names)

# متوسط وزن الفراولة الواحدة (جرام)
AVERAGE_STRAWBERRY_WEIGHT = 20