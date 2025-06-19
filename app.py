import os
import pickle
import numpy as np
import faiss
import re

from flask import Flask, jsonify, request
from flask_cors import CORS

from transformers import pipeline
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = "chunks.pkl"
INDEX_PATH = "faiss_index.index"
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
MODEL_DIR = "./models"

print("📥 Loading components...")
chunks = pickle.load(open(CHUNKS_PATH, "rb"))
index = faiss.read_index(INDEX_PATH)
embedder = SentenceTransformer("all-MiniLM-L6-v2")
llm = pipeline(
    "text-generation",
    model=MODEL_NAME,
    cache_dir=MODEL_DIR,
    trust_remote_code=True,
    device_map="auto"
)
print("✅ Components loaded.")

app = Flask(__name__)
CORS(app)
