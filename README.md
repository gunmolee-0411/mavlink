MAVLink Custom Message (UDP) 
--------------------------------------------------------------------------------------------------------------------
example of sending and receiving MAVLink messages over UDP using pymavlink, including a user-defined custom message.

--------------------------------------------------------------------------------------------------------------------
Messages

- Standard MAVLink
	•	Uses common dialect
	•	Parsed with recv_match()

- Custom MAVLink: CUSTOM_ATTITUDE
	•	uint32 time_boot_ms
	•	float  roll
  •	float  pitch
	•	float  yaw

  --------------------------------------------------------------------------------------------------------------------
  Key Point
	•	recv_match() works only for standard messages
	•	Custom messages require raw-byte parsing using parse_char()
