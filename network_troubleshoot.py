import os
import socket
import requests
import subprocess

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        print("✅ Internet is working.")
    except:
        print("❌ No internet connection.")

def check_dns():
    try:
        socket.gethostbyname("google.com")
        print("✅ DNS is working.")
    except:
        print("❌ DNS resolution failed.")

def get_ip_config():
    print("\n📡 IP Configuration:")
    os.system("ipconfig")

def ping_router():
    print("\n📶 Pinging Default Gateway:")
    os.system("ping 192.168.1.1 -n 4")

def public_ip():
    ip = requests.get("https://api.ipify.org").text
    print("\n🌐 Public IP Address:", ip)

# Make sure to **call** the functions below!
check_internet()
check_dns()
get_ip_config()
ping_router()
public_ip()

