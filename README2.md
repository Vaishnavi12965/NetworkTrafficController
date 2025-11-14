# Network Traffic Controller

A Python-based Linux network traffic controller using `tc` for bandwidth shaping and monitoring.  
This project allows users to **limit, remove, or check network bandwidth** on Linux interfaces and measure traffic using `iperf3`.

---

## Features

- Apply bandwidth limits to network interfaces
- Remove bandwidth restrictions
- Check current traffic shaping status
- Works with iperf3 for real-time throughput testing
- Command-line interface for Linux systems

---

## Requirements

- Python 3.x
- Linux system (Kali, Ubuntu, etc.)
- `tc` (Traffic Control, part of iproute2)
- `iperf3` (for network testing)
- sudo privileges

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Vaishnavi12965/network-traffic-controller.git
cd network-traffic-controller

2. Install dependencies 


pip3 install -r requirements.txt

3. Make sure iproute2 and iperf3 are installed:



sudo apt update
sudo apt install iproute2 iperf3 -y

## Usage

1 Check current status:

sudo python3 controller.py eth0 --status

2 Apply a bandwidth limit:

sudo python3 controller.py eth0 --limit 100mbit

3 Remove bandwidth limit:

sudo python3 controller.py eth0 --remove

4 Test with iperf3:

5 On Linux client:

iperf3 -c <server-ip>

6 On Windows server:

iperf3.exe -s

## How It Works

Uses Linux tc command to manage queueing disciplines (qdisc) for traffic shaping.

Python script wraps tc commands for easy CLI usage.

Works in real time without restarting network interfaces

Author
vaishnavi
yellagounivaishnavi@gmail.com


