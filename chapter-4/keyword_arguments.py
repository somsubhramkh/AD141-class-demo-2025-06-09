#!/usr/bin/env python3

def show_config(device_name,**config):
    print("Device Name:",device_name)
    for key,val in config.items():
        print(key,":",val);


show_config("Mac Mini",RAM="16Gi",Storage = "512Gi")
show_config("Macbook Pro",RAM="32Gi",Storage = "1Ti",Screen_Size="14 in")