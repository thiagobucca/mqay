import psutil
import time
import subprocess
import datetime
import paho.mqtt.client as mqtt

service_names = ["service1", "service2", "service3"]

broker_address = "yourbroker"
broker_port = 1883
broker_username = "youruser"
broker_password = "yourpassword"

client = mqtt.Client()

client.username_pw_set(broker_username, broker_password)
client.connect(broker_address, broker_port)

while True:
    for service_name in service_names:
        try:
            status_output = subprocess.check_output(["systemctl", "is-active", service_name])
            is_active = status_output.decode().strip() == "active"
        except Exception as e:
            print(f"Error checking status for {service_name}: {e}")
            continue

        if is_active:
            try:
                status_output = subprocess.check_output(["systemctl", "status", service_name])
                status_lines = status_output.decode().split("\n")
                pid_line = next((line for line in status_lines if "Main PID" in line), None)
                if not pid_line:
                    raise Exception("Main PID not found in service status")
                pid = int(pid_line.split()[2])
            except Exception as e:
                print(f"Error retrieving process ID for {service_name}: {e}")
                continue

            process = psutil.Process(pid)
            memory_info = process.memory_info()
            memory_usage = memory_info.rss / 1024 / 1024

            uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(process.create_time())
            uptime_str = ""
            if uptime.days > 0:
                uptime_str = f"{uptime.days} days"
            elif uptime.seconds >= 3600:
                hours = uptime.seconds // 3600
                uptime_str = f"{hours} hours"
            elif uptime.seconds >= 60:
                minutes = uptime.seconds // 60
                uptime_str = f"{minutes} minutes"

            client.publish(
                f"systemd-service/{service_name}/memory", f"{memory_usage:.2f}")
            client.publish(
                f"systemd-service/{service_name}/cpu_time", f"Up {uptime_str}")
        else:
            client.publish(
                f"systemd-service/{service_name}/memory", "0")
            client.publish(
                f"systemd-service/{service_name}/cpu_time", "Desligado")

    time.sleep(60)
