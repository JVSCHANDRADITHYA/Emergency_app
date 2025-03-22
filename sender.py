import sensors
import socket
import time

sensors.init()
server_ip = "172.20.46.240"
server_port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        sensors_data = {}  # Dictionary to store sensor values
        
        for chip in sensors.iter_detected_chips():
            for feature in chip:
                sensors_data[feature.label] = feature.get_value()

        data_str = str(sensors_data)
        sock.sendto(data_str.encode(), (server_ip, server_port))
        print("Sent:", data_str)
        
        time.sleep(0.5)  # Adjust the speed
finally:
    sensors.cleanup()  # Clean up sensors after script ends
