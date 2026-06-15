"""
core/time_estimator.py
Tính toán thời gian dự kiến đến nơi (ETA) dựa trên thời gian xuất phát và quãng đường.
"""
import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def predict_eta(departure_str: str, distance_km: float, speed: float = 60) -> datetime.datetime:
    """
    Tính ETA (Estimated Time of Arrival) của chuyến xe.

    Args:
        departure_str: Thời gian xuất phát dạng chuỗi "YYYY-MM-DD HH:MM:SS".
        distance_km:   Quãng đường cần di chuyển (km).
        speed:         Vận tốc trung bình (km/h), mặc định 60 km/h.

    Returns:
        Đối tượng datetime biểu diễn thời điểm dự kiến đến nơi.

    Raises:
        ValueError: Nếu departure_str không đúng định dạng.
    """
    dep_time = datetime.datetime.strptime(departure_str, DATETIME_FORMAT)
    hours_needed = distance_km / speed
    eta = dep_time + datetime.timedelta(hours=hours_needed)
    return eta