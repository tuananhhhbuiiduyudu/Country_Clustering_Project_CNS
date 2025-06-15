import pandas as pd 
import config 

def load_data(filepath = config.SET_PATH_DATA) -> pd.DataFrame : 
    try : 
        df = pd.read_csv(filepath)
        print(f"Dữ liệu đã tài thành công từ {filepath}")
        return df
    except FileNotFoundError : 
        
        print(f"Lỗi không tìm thấy file từ thư mục data")
        print(f"Vui lòng tải file Country-data.csv vào data")
        return None
    
    except Exception as e : 
        print(f"Lỗi không xác định")
        return None

## test hàm data_loader.py 
if __name__ == '__main__':
    data = load_data()
    if data is not None:
        print(f"Xem 5 dòng đầu tiên của dữ liệu")
        print(data.head())
        print(f"Xem các cột dữ liệu có")
        print(len(data.columns))