MAVLink Custom Message (UDP)

Minimal example of sending and receiving MAVLink messages over UDP using pymavlink, including a user-defined custom message.

Messages

Standard MAVLink Message
	•	Uses the MAVLink common dialect
	•	Parsed using mavutil.recv_match()

Custom MAVLink Message: CUSTOM_ATTITUDE
	uint32 time_boot_ms
	float  roll
	float  pitch
	float  yaw
	•	Defined in custom_attitude.xml
	•	Python bindings generated using mavgen

Key Point
	•	recv_match() works only for standard MAVLink messages
	•	Custom messages must be parsed using raw-byte parsing with parse_char()
