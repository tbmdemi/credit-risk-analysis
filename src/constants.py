from pathlib import Path

# Thu muc goc cua Project
BASE_DIR = Path(__file__).parent.parent

# Cac duong dan quan trong
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Tham so
FILE_NAME = "UCI_Credit_Card"