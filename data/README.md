# Bitcoin Data Scraper

Chương trình Python để cào dữ liệu Bitcoin từ Yahoo Finance sử dụng thư viện yfinance.

## Tính năng

- Lấy dữ liệu Bitcoin (BTC-USD) từ Yahoo Finance
- Hỗ trợ nhiều khoảng thời gian khác nhau (1 ngày đến tất cả dữ liệu có sẵn)
- Lưu dữ liệu dưới dạng CSV với các cột: Date, Open, High, Low, Close, Volume
- Giao diện tương tác để chọn khoảng thời gian
- Hiển thị thống kê cơ bản về dữ liệu

## Cài đặt

1. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

Hoặc cài đặt thủ công:
```bash
pip install yfinance pandas numpy
```

## Sử dụng

Chạy chương trình:
```bash
python bitcoin_data_scraper.py
```

Chương trình sẽ hiển thị menu để chọn khoảng thời gian dữ liệu:
- 1 ngày
- 5 ngày  
- 1 tháng
- 3 tháng
- 6 tháng
- 1 năm (mặc định)
- 2 năm
- 5 năm
- Tất cả dữ liệu có sẵn

## Kết quả

Dữ liệu sẽ được lưu trong thư mục `data/` với tên file `bitcoin_data_[khoảng_thời_gian].csv`

Ví dụ: `bitcoin_data_1y.csv` cho dữ liệu 1 năm.

## Cấu trúc dữ liệu

File CSV sẽ có các cột:
- **Date**: Ngày tháng
- **Open**: Giá mở cửa
- **High**: Giá cao nhất trong ngày
- **Low**: Giá thấp nhất trong ngày  
- **Close**: Giá đóng cửa
- **Volume**: Khối lượng giao dịch

## Lưu ý

- Cần kết nối internet để tải dữ liệu
- Dữ liệu được lấy từ Yahoo Finance, có thể có độ trễ
- Chương trình tự động tạo thư mục `data/` nếu chưa tồn tại

