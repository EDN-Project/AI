#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}🔎 Checking for model folder...${NC}"
if [ ! -d "models" ] || [ -z "$(ls -A models)" ]; then
    echo -e "${GREEN}📥 Downloading model...${NC}"
    python download_model.py
else
    echo -e "${GREEN}✅ Model already downloaded.${NC}"
fi

echo -e "${GREEN}🚀 Starting the app...${NC}"
python chat.py