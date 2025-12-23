import time
import math
from pymavlink import mavutil

# UDP로 송신 (포트 14550)
mav = mavutil.mavlink_connection(
    'udpout:127.0.0.1:14550',
    source_system=1,
    source_component=1
)

time.sleep(1)

print("📤 Sender started")

# ✅ 프로그램 시작 시점을 boot time으로 사용
boot_time = time.time()

while True:
    # 가상의 attitude 데이터
    roll  = math.radians(10.0)
    pitch = math.radians(-5.0)
    yaw   = math.radians(30.0)

    rollspeed  = 0.1
    pitchspeed = 0.2
    yawspeed   = 0.3

    # ✅ 부팅 이후 경과 시간 (ms)
    time_boot_ms = int((time.time() - boot_time) * 1000)

    mav.mav.attitude_send(
        time_boot_ms,
        roll,
        pitch,
        yaw,
        rollspeed,
        pitchspeed,
        yawspeed
    )

    print(
        f"📤 Sent ATTITUDE | "
        f"time_boot_ms={time_boot_ms} | "
        f"roll={roll:.3f}, pitch={pitch:.3f}, yaw={yaw:.3f}"
    )

    time.sleep(1)