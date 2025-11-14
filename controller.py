import subprocess
import argparse
import sys

def run_command(cmd):
    try:
        subprocess.run(cmd, check=True)
        print("[+] Command executed:", " ".join(cmd))
    except subprocess.CalledProcessError as e:
        print("[-] Error:", e)

def set_limit(interface, rate):
    # Remove existing qdisc first
    subprocess.run(
        ["sudo", "tc", "qdisc", "del", "dev", interface, "root"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"[*] Limiting bandwidth on {interface} to {rate}")
    run_command([
        "sudo", "tc", "qdisc", "add", "dev", interface, "root",
        "tbf", "rate", rate, "burst", "32kbit", "latency", "400ms"
    ])

def remove_limit(interface):
    print(f"[*] Removing bandwidth limit on {interface}")
    run_command(["sudo", "tc", "qdisc", "del", "dev", interface, "root"])

def check_status(interface):
    print(f"[*] Checking current limit on {interface}")
    run_command(["tc", "qdisc", "show", "dev", interface])

def main():
    parser = argparse.ArgumentParser(description="Network Traffic Controller - Bandwidth Limiter")

    parser.add_argument("interface", help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("--limit", help="Bandwidth rate (e.g., 1mbit, 500kbit)")
    parser.add_argument("--remove", action="store_true", help="Remove bandwidth limit")
    parser.add_argument("--status", action="store_true", help="Check current qdisc settings")

    args = parser.parse_args()

    if args.limit:
        set_limit(args.interface, args.limit)
    elif args.remove:
        remove_limit(args.interface)
    elif args.status:
        check_status(args.interface)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()

