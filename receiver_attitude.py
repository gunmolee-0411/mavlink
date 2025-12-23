from pymavlink import mavutil

# UDP로 수신
mav = mavutil.mavlink_connection(
    'udpin:0.0.0.0:14550'
)

print("📥 Receiver waiting...")

while True:
    msg = mav.recv_match(type='ATTITUDE', blocking=True)
    if not msg:
        continue

    print("📥 Received ATTITUDE")
    print(f"  roll       = {msg.roll:.6f}")
    print(f"  pitch      = {msg.pitch:.6f}")
    print(f"  yaw        = {msg.yaw:.6f}")
    print(f"  rollspeed  = {msg.rollspeed:.6f}")
    print(f"  pitchspeed = {msg.pitchspeed:.6f}")
    print(f"  yawspeed   = {msg.yawspeed:.6f}")
    print("-" * 40)