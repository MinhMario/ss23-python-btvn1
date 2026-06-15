import datetime
 
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta, DATETIME_FORMAT
from utils.file_helper import create_log_dir

#Tại sao from math import * là Anti-pattern? Vấn đề nằm ở chỗ câu lệnh này đổ toàn bộ ~40 tên hàm của math (như sqrt, log, floor, ceil, pow, pi...) thẳng vào namespace hiện tại mà không có tiền tố nào
# cách import thông minh hơn : from math import sqrt, atan2, radians, sin, cos
# Câu 2 — Tệp đặc biệt để biến thư mục thành Package là gì?
# Đó là tệp __init__.py. Khi Python thấy một thư mục có tệp này, nó coi thư mục đó là một package và cho phép import từ bên trong. Tệp có thể để trống hoặc chứa code khởi tạo package (ví dụ: export các hàm public, set __all__, hay log version).
# ├── main.py
# ├── utils/
# │ ├── __init__.py
# │ └── file_helper.py
# ├── core/
# │ ├── __init__.py
# │ ├── geo_calculator.py
# │ └── time_estimator.py
# └── logs/

# Dữ liệu giả lập các chuyến xe đẩy về từ tổng đài
shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285, "from_lon": 105.8542,  
        "to_lat": 10.8231,   "to_lon": 106.6297,   
        "depart":   "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00",
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285, "from_lon": 105.8542,  
        "to_lat": 16.0544,   "to_lon": 108.2022,    
        "depart":   "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00",           
    },
]
 

create_log_dir("logs")
 
print()
print("=" * 60)
print("     HỆ THỐNG THEO DÕI VẬN TẢI — KẾT QUẢ PHÂN TÍCH")
print("=" * 60)
 
# ─── Xử lý từng chuyến xe ────────────────────────────────────────────────────
for shipment in shipments:
    # 1. Tính khoảng cách bằng Haversine (chính xác)
    distance = calculate_distance(
        shipment["from_lat"], shipment["from_lon"],
        shipment["to_lat"],   shipment["to_lon"]
    )
 
    # 2. Tính ETA
    eta = predict_eta(shipment["depart"], distance_km=distance)
 
    # 3. So sánh ETA với deadline để phát hiện nguy cơ trễ hàng
    deadline = datetime.datetime.strptime(shipment["deadline"], DATETIME_FORMAT)
    is_late = eta > deadline
 
    # 4. In kết quả
    print(f"\n  Xe       : {shipment['id']}")
    print(f"  Khoảng cách: {distance:.2f} km")
    print(f"  Xuất phát  : {shipment['depart']}")
    print(f"  ETA dự kiến: {eta.strftime(DATETIME_FORMAT)}")
    print(f"  Deadline   : {shipment['deadline']}")
 
    if is_late:
        overdue_minutes = int((eta - deadline).total_seconds() / 60)
        print(f"  [CẢNH BÁO] Xe {shipment['id']} có nguy cơ TRỄ HẸN "
              f"khoảng {overdue_minutes} phút!")
    else:
        buffer_minutes = int((deadline - eta).total_seconds() / 60)
        print(f"  [OK] Giao hàng đúng hạn. Dự phòng: {buffer_minutes} phút.")
 
print()
print("=" * 60)