#!/usr/bin/env python3


##### get_configs #####

# This script will connect to the devices from devices.json using the
# credentials in secrets.json, get the running config and save it to
# a file in the configs directory.

# Written by Zach Wendell, 201902
# Last Updated: 20190212T053400Z


# IMPORT LIBRARIES
import netmiko
from datetime import datetime
import json


# GET CURRENT TIMESTAMP (UTC date/time in ISO8601 format)
now8601 = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


# DEFINE CREDENTIALS & DEVICES
with open('secrets.json', 'r') as secrets:
  creds = json.loads(secrets.read())
gcun = creds['admin_user']['username']
gcpw = creds['admin_user']['password']

with open('devices.json', 'r') as devices:
  gcdevs = json.loads(devices.read())



def get_configs():
  # ITERATE THROUGH DEVICES
  for device in gcdevs.items():
    dev_fqdn = device[1]['dev_fqdn']
    dev_type = device[1]['dev_type']

    # FOR CISCO IOS DEVICES
    if 'cisco_ios' in dev_type:
      try:
        connection = netmiko.ConnectHandler(
          ip = dev_fqdn,
          device_type = dev_type,
          username = gcun,
          password = gcpw
        )
        config = connection.send_command('show running-config')
        connection.disconnect()
        with open('configs/' + dev_fqdn + '.config', 'w') as f: 
          f.write(config)
        print('['+now8601+'] ' + dev_fqdn + ': configuration saved')
      except:
        print('['+now8601+'] ' + dev_fqdn + ': unable to connect ***')

    # FOR CISCO NX OS DEVICES
    elif 'cisco_nxos' in dev_type:
      try:
        connection = netmiko.ConnectHandler(
          ip = dev_fqdn,
          device_type = dev_type,
          username = gcun,
          password = gcpw
        )
        config = connection.send_command('show running-config')
        connection.disconnect()
        with open('configs/' + dev_fqdn + '.config', 'w') as f: 
          f.write(config)
        print('['+now8601+'] ' + dev_fqdn + ': configuration saved')
      except:
        print('['+now8601+'] ' + dev_fqdn + ': unable to connect ***')

    # FOR ARISTA EOS DEVICES
    elif 'arista_eos' in dev_type:
      try:
        connection = netmiko.ConnectHandler(
          ip = dev_fqdn,
          device_type = dev_type,
          username = gcun,
          password = gcpw
        )
        config = connection.send_command('show run')
        connection.disconnect()
        with open('configs/' + dev_fqdn + '.config', 'w') as f: 
          f.write(config)
        print('['+now8601+'] ' + dev_fqdn + ': configuration saved')
      except:
        print('['+now8601+'] ' + dev_fqdn + ': unable to connect ***')

    # FOR JUNIPER JUNOS DEVICES
    elif 'juniper_junos' in dev_type:
      try:
        connection = netmiko.ConnectHandler(
          ip = dev_fqdn,
          device_type = dev_type,
          username = gcun,
          password = gcpw
        )
        config = connection.send_command('show configuration')
        connection.disconnect()
        with open('configs/' + dev_fqdn + '.config', 'w') as f: 
          f.write(config)
        print('['+now8601+'] ' + dev_fqdn + ': configuration saved')
      except:
        print('['+now8601+'] ' + dev_fqdn + ': unable to connect ***')

    # FOR UBIQUITI EDGEOS DEVICES
    elif 'ubiquiti_edge' in dev_type:
      try:
        # dev_type 'ubiquiti_edge' not working for me with netmiko
        # currently due to weird prompt issues. Using 'vyatta_vyos'
        # explicitly instead, since they're basically the same platform
        connection = netmiko.ConnectHandler(
          ip = dev_fqdn,
          device_type = 'vyatta_vyos',
          username = gcun,
          password = gcpw
        )
        commands = [
          'run terminal length 9999',
          'run show configuration'
        ]
        config = connection.send_config_set(commands)
        connection.disconnect()
        with open('configs/' + dev_fqdn + '.config', 'w') as f: 
          f.write(config)
        print('['+now8601+'] ' + dev_fqdn + ': configuration saved')
      except:
        print('['+now8601+'] ' + dev_fqdn + ': unable to connect ***')

    # FOR VYATTA/VYOS DEVICES
    elif 'vyatta_vyos' in dev_type:
      try:
        connection = netmiko.ConnectHandler(
          ip = dev_fqdn,
          device_type = dev_type,
          username = gcun,
          password = gcpw
        )
        commands = [
          'run terminal length 9999',
          'run show configuration'
        ]
        config = connection.send_config_set(commands)
        connection.disconnect()
        with open('configs/' + dev_fqdn + '.config', 'w') as f: 
          f.write(config)
        print('['+now8601+'] ' + dev_fqdn + ': configuration saved')
      except:
        print('['+now8601+'] ' + dev_fqdn + ': unable to connect ***')

    else:
      print('['+now8601+'] ' + dev_fqdn + ': ' + dev_type  + ' is not supported')



# Run the get_configs function
get_configs()



# eof

