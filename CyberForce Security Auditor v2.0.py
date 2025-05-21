import os
import platform
import subprocess
import argparse
import socket
import psutil

def check_firewall():
    """Check if firewall is active."""
    os_type = platform.system()
    if os_type == "Windows":
        print("\n[+] Checking Windows Firewall:")
        os.system("netsh advfirewall show allprofiles")
    elif os_type == "Linux":
        print("\n[+] Checking Linux Firewall (UFW):")
        os.system("sudo ufw status")
    elif os_type == "Darwin":  # macOS
        print("\n[+] Checking macOS Firewall:")
        os.system("sudo pfctl -s info")

def scan_network_ports():
    """Check open ports (no hacking)."""
    print("\n[+] Open Network Ports:")
    for conn in psutil.net_connections():
        if conn.status == "LISTEN":
            print(f"Port {conn.laddr.port} is open")

def check_admin():
    """Check if running as admin/root."""
    try:
        if platform.system() == "Windows":
            print("\n[+] Admin Check:")
            os.system("net session >nul 2>&1 && echo 'You are ADMIN' || echo 'NOT ADMIN'")
        else:
            print("\n[+] Root Check:")
            os.system("sudo -n true 2>/dev/null && echo 'You are ROOT' || echo 'NOT ROOT'")
    except:
        pass

def main():
    print("\n=== 🔒 CyberForce Security Scanner ===")
    check_firewall()
    scan_network_ports()
    check_admin()

if __name__ == "__main__":
    main()
