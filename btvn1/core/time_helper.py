from datetime import datetime, timedelta

def calculate_eta(flights):
    print('----- TINH TOAN THOI GIAN HA CANH (ETA) -----')
    flight_id = input('Nhap ma chuyen bay can tinh: ').strip().upper()

    for f in flights:
        if f['flight_id'] == flight_id:
            depart = datetime.strptime(f['depart_time'], '%Y-%m-%d %H:%M:%S')
            eta = depart + timedelta(minutes=f['duration_min'])
            print(f"-> Chuyen bay {flight_id} cat canh luc: {depart}")
            print(f"-> Thoi gian ha canh du kien (ETA): {eta}")
            return

    print(f'Khong tim thay chuyen bay co ma: {flight_id}')