import load_data as ld
import constants as c
import logging
import time
from ydata_profiling import profile_report
import pandas as pd

def make_report(df: pd.DataFrame):
    profile = df.profile_report(title= "Báo cáo Dữ liệu Tài chính")

    output_path = c.BASE_DIR / "data" / "reports" / "data_profile.html"
    output_path.parent.mkdir(parents=True, exist_ok=True) # Tạo thư mục nếu chưa có
    
    profile.to_file(output_path)
    logging.info(f"Báo cáo đã được lưu tại: {output_path}")

def main():
    start = time.time()
    df = ld.load_parquet() # Đảm bảo trò đã import hàm này
    
    make_report(df)
    
    end = time.time()

    logging.info(f"Execution time: {end - start:.4f}")

if __name__ == "__main__":
    main()