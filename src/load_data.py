import pandas as pd
from pathlib import Path
import logging
import time
from ydata_profiling import profile_report

import src.constants as c

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def load_csv() -> pd.DataFrame:
    """
    Mac dinh la se load file UCI_Credit_Card.csv
    """

    path = c.RAW_DATA_DIR

    return pd.read_csv(path / f"{c.FILE_NAME}.csv")

def save_parquet(df: pd.DataFrame, file = c.FILE_NAME):
    """
    Mac dinh la se load luu file UCI_Credit_Card.csv ve dang .parquet
    Args:
        df (pd.DataFrame): Dataframe can luu thanh file .parquet
        file (str): Ten file de luu cho DataFrame

    Returns:
    
    """
    c.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    target_file = c.PROCESSED_DATA_DIR / f"{file}.parquet"
    logging.info(f"Saving output data: {target_file}")

    df.to_parquet(target_file, index= False, engine= 'pyarrow')

def load_parquet(path = c.PROCESSED_DATA_DIR, file = c.FILE_NAME, columns = None) -> pd.DataFrame:
    """
    Su dung de load file .parquet
    
    Args:
        path (Path): Duong dan toi thu muc chua file can doc
        file (str): Ten file can doc

    Returns:
        pd.DataFrame: DataFrame doc tu file .parquet
    """

    start = time.time()
    df = pd.read_parquet(path / f"{file}.parquet", columns= columns)
    end = time.time()

    logging.info(f"Execution time: {end-start:.4f}")

    return df

def make_report(df: pd.DataFrame, name= "Báo cáo Dữ liệu Tài chính"):
    """
    Tao report tuong ung cho DataFrame duoi dang html
    
    Args:
        df (pd.DataFrame): DataFrame can tao report
        name (str): Ten file dat cho report
    Returns:
    
    """
    profile = df.profile_report(title= name)

    output_path = c.BASE_DIR / "data" / "reports" / "data_profile.html"
    output_path.parent.mkdir(parents=True, exist_ok=True) # Tạo thư mục nếu chưa có
    
    profile.to_file(output_path)
    logging.info(f"Báo cáo đã được lưu tại: {output_path}")

def main():
    df = load_csv()
    print(df.info())

    save_parquet(df)

    df_1 = load_parquet()
    print(df_1.info())

    make_report(df_1)

if __name__ == "__main__":
    start = time.time()
    main()

    end = time.time()

    print(f"Execution time total: {end - start}")