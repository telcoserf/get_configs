# get_configs

## Basics
* Containerized Python/Netmiko replacement for RANCID/Oxidized for backing up network device configurations
* Currently supported device types:
    - Arista EOS
    - Cisco IOS
    - Cisco NX OS
    - Juniper JunOS
    - Ubiquiti EdgeOS
    - Vyatta/VyOS
* To use other device types, see the Netmiko documentation and adapt the code accordingly

## Setup
* Change the device names, IPs/FQDNs, and types in the devices.json.example file and save it as 'devices.json'
* Change the credentials for 'admin_user' in the secrets.json.example file and save it as 'secrets.json'
* Change the DNS server in the docker-compose.yml file to either a public DNS server or your local name server

## Usage
* This tool can either be run as a stand-alone Python script, or as a containerized microservice via Docker
    - Python 3:
        - ```python3 get_configs.py```
    - Docker:
        - ```docker-compose up```

