import logging
import os
from pathlib import Path

BASE_LOG_DIR = Path(__file__).resolve().parents[2]/'logs'
BASE_LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(BASE_LOG_DIR/'pipeline.log',mode='a'),
        logging.StreamHandler()
    ]
)
