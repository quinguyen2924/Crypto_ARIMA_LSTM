import yfinance as yf
import pandas as pd
import os

def get_bitcoin_data():
    """
    Tải dữ liệu Bitcoin từ 2018-01-01 đến hiện tại với khoảng thời gian 1 ngày
    """
    try:
        print("Đang tải dữ liệu Bitcoin từ 2018-01-01 đến hiện tại...") 
        # Tạo ticker cho Bitcoin (BTC-USD)
        btc_ticker = yf.Ticker("BTC-USD")
        # Lấy dữ liệu lịch sử từ 2018-01-01 đến hiện tại với khoảng thời gian 1 ngày
        btc_data = btc_ticker.history(start="2020-01-01", interval="1d")
        if btc_data.empty:
            print("Không có dữ liệu được tìm thấy!")
            return None
        # Reset index để có cột Date
        btc_data = btc_data.reset_index()
        # Đảm bảo có đúng các cột yêu cầu
        required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        # Kiểm tra xem có đủ cột không
        missing_columns = [col for col in required_columns if col not in btc_data.columns]
        if missing_columns:
            print(f"Thiếu các cột: {missing_columns}")
            return None
        # Chọn chỉ các cột cần thiết
        btc_data = btc_data[required_columns]
        
        # Sắp xếp theo ngày (từ cũ đến mới)
        btc_data = btc_data.sort_values('Date')
        
        print(f"Đã tải thành công {len(btc_data)} bản ghi dữ liệu Bitcoin")
        print(f"Từ ngày: {btc_data['Date'].min()} đến {btc_data['Date'].max()}")
        
        return btc_data
        
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu: {str(e)}")
        return None

def save_to_csv(data, filename="bitcoin_data_max_1d.csv"):
    """
    Lưu dữ liệu vào file CSV
    """
    try:
        if data is not None:
            # Tạo thư mục data nếu chưa có
            os.makedirs("data", exist_ok=True)
            
            # Đường dẫn file
            filepath = os.path.join("data", filename)
            
            # Lưu vào CSV
            data.to_csv(filepath, index=False, encoding='utf-8')
            print(f"Đã lưu dữ liệu vào file: {filepath}")
            print(f"Kích thước file: {os.path.getsize(filepath)} bytes")
            
            # Hiển thị thông tin cơ bản về dữ liệu
            print("\nThông tin dữ liệu:")
            print(f"Số dòng: {len(data)}")
            print(f"Số cột: {len(data.columns)}")
            print(f"Các cột: {list(data.columns)}")
            
            # Hiển thị 5 dòng đầu
            print("\n5 dòng đầu tiên:")
            print(data.head())
            
            # Hiển thị 5 dòng cuối
            print("\n5 dòng cuối cùng:")
            print(data.tail())
            
            # Hiển thị thống kê cơ bản
            print("\nThống kê cơ bản:")
            print(data.describe())
            
        else:
            print("Không có dữ liệu để lưu!")
            
    except Exception as e:
        print(f"Lỗi khi lưu file: {str(e)}")

if __name__ == "__main__":
    print("=== TẢI DỮ LIỆU BITCOIN TỪ 2018-01-01 ĐẾN HIỆN TẠI ===")
    print("Khoảng thời gian: 1 ngày (1d), start=2018-01-01")
    print()
    
    # Tải dữ liệu
    bitcoin_data = get_bitcoin_data()
    
    if bitcoin_data is not None:
        # Lưu vào CSV
        save_to_csv(bitcoin_data)
        print("\nHoàn thành! Dữ liệu đã được lưu vào thư mục data/")
    else:
        print("Không thể lấy dữ liệu Bitcoin!")

