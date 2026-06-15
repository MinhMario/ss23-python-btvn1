"""
core/geo_calculator.py
Tính khoảng cách địa lý giữa hai điểm theo công thức Haversine.
Công thức này chính xác hơn nhiều so với cách tính sai số cao của code cũ.
"""
from math import radians, sin, cos, sqrt, atan2

EARTH_RADIUS_KM = 6371.0


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Tính khoảng cách (km) giữa hai tọa độ GPS theo công thức Haversine.

    Args:
        lat1, lon1: Vĩ độ và kinh độ điểm xuất phát (độ thập phân).
        lat2, lon2: Vĩ độ và kinh độ điểm đích (độ thập phân).

    Returns:
        Khoảng cách tính bằng km (float).

    Ví dụ:
        >>> calculate_distance(21.0285, 105.8542, 10.8231, 106.6297)
        1143.84  # Hà Nội → TP.HCM
    """
    # Chuyển độ sang radian
    rlat1 = radians(lat1)
    rlat2 = radians(lat2)
    delta_lat = radians(lat2 - lat1)
    delta_lon = radians(lon2 - lon1)

    # Công thức Haversine
    a = sin(delta_lat / 2) ** 2 + cos(rlat1) * cos(rlat2) * sin(delta_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_KM * c