<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/thiagobucca/bucalarm-iot">
    <img src="images/mqay.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MQay</h3>

  <p align="center">
    Systemd > MQTT Bridge
    <br />
  </p>
</p>

# MQay

MQay is a Python script that monitors the memory usage and uptime of one or more systemd services, and publishes this information to an MQTT broker. The script can be used to keep track of important system processes and receive notifications when they go down.

## Dependencies

MQay requires the following Python packages to be installed:

- `psutil`
- `paho-mqtt`

## Configuration

Before running MQay, you need to set the following variables in the script:

- `service_names`: A list of the systemd services you want to monitor.
- `broker_address`: The hostname or IP address of the MQTT broker.
- `broker_port`: The port number of the MQTT broker (usually 1883).
- `broker_username`: The username to use for authenticating with the MQTT broker.
- `broker_password`: The password to use for authenticating with the MQTT broker.

You can also adjust the time interval between checks by changing the value of the `time.sleep` function.

## Usage

To run MQay, simply execute the script using Python:

`python mqay.py`

The script will start monitoring the specified systemd services and publishing their memory usage and uptime information to the MQTT broker. When a service goes down, the script will publish the following information:

- `memory`: 0
- `cpu_time`: "Off"

## License

MQay is released under the [MIT License](LICENSE).
