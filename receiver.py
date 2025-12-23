from pymavlink import mavutil
import mavlink

# UDP 수신
master = mavutil.mavlink_connection(
    "udpin:0.0.0.0:14550",
    source_system=255
)

# ⭐️ 커스텀 MAVLink 파서
mav = mavlink.MAVLink(master)

print("RECEIVER: waiting...")

while True:
    # raw bytes 읽기
    data = master.recv(1024)
    if not data:
        continue

    # byte 단위 파싱
    for b in data:
        msg = mav.parse_char(bytes([b]))
        if msg is None:
            continue

        print("DEBUG:", msg.get_type())

        if msg.get_type() == "CUSTOM_ATTITUDE":
            print(
                "RECEIVED:",
                msg.time_boot_ms,
                msg.roll,
                msg.pitch,
                msg.yaw
            )