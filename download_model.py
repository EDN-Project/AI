import os
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
MODEL_DIR = "./models"

print(f"📥 Downloading {MODEL_NAME} to {MODEL_DIR}...")
os.makedirs(MODEL_DIR, exist_ok=True)

AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=MODEL_DIR)
AutoModelForCausalLM.from_pretrained(MODEL_NAME, cache_dir=MODEL_DIR)

print(f"✅ Model downloaded successfully to {MODEL_DIR}")