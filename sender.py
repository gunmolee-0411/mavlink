import time
from pymavlink import mavutil
import mavlink   # mavgen으로 생성된 파일

# UDP로 보내기
master = mavutil.mavlink_connection(
    "udpout:127.0.0.1:14550",
    source_system=1
)

# ⭐️ 커스텀 MAVLink 파서 연결 (while 밖!)
master.mav = mavlink.MAVLink(master)

print("SENDER: sending custom message...")

while True:
    now_ms = int(time.time() * 1000) % (2**32)

    msg = mavlink.MAVLink_custom_attitude_message(
        now_ms,
        1.1,   # roll
        2.2,   # pitch
        3.3    # yaw
    )

    master.mav.send(msg)
    print("SENT:", now_ms)
    time.sleep(1)