# Sensor Command line for S.M.A.R.T.

Get SMART `Raw Read Error Rate` value and HDD temperature as sensor in home-assistant

## Quick start

1. Install kapow! from https://github.com/BBVA/kapow

2. Copy `hdd.pow` and `hdd.py` to some folder on the machine which has access to the disks

3. Adapt routes inside `hdd.pow` to your wishes. You can add more disks or remove some from the examples.

4. Run `sudo kapow server --bind $IP:8880 hdd.pow` inside the above folder

   Replace `$IP` with the IP address which can be used to reach your kapow! server from home-assistant
   Of course can you change the port (default `8880`) as it fits your setup. 

5. Put the following inside your `configuration.yaml` in home-assistant:

          sensor:
          - platform: command_line
            name: HDD Temperature SDA
            command: "curl -s http://$IP:8880/hdd/temp/sda"
            unit_of_measurement: "°C"
            scan_interval: 600
        
   `$IP` should be the IP address where the kapow! server can be accessed
   
6. Restart home-assistant and the sensor data should appear

## Home-assistant sensor examples

### Read temperature from disk /dev/sda

      sensor:
      - platform: command_line
        name: HDD Temperature SDA
        command: "curl -s http://$IP:8880/hdd/temp/sda"
        unit_of_measurement: "°C"
        scan_interval: 600
        
### Read error rate from disk /dev/sdb
      
     sensor:
      - platform: command_line
        name: HDD SMART error rate SDB
        command: "curl -s http://$IP:8880/hdd/error/sdb"
        scan_interval: 600


