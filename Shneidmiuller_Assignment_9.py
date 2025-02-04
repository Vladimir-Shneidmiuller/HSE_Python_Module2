from scapy.all import *
from scapy.layers.http import HTTPRequest, HTTPResponse

def packet_callback(packet):
    if packet.haslayer(HTTPRequest):
        http_layer = packet[HTTPRequest]
        print("\n===== HTTP REQUEST =====")
        print(f"Method: {http_layer.Method.decode()} ")
        print(f"Host: {http_layer.Host.decode()} ")
        print(f"Path: {http_layer.Path.decode()} ")
        if packet.haslayer(Raw):
            print("Data:", packet[Raw].load.decode(errors='ignore'))

    elif packet.haslayer(HTTPResponse):
        print("\n===== HTTP RESPONSE =====")
        if packet.haslayer(Raw):
            print("Response Data:", packet[Raw].load.decode(errors='ignore'))

print("[*] Sniffing HTTP traffic ... Press Ctrl+C to stop.")
sniff(filter="tcp port 80", prn=packet_callback, store=False)
