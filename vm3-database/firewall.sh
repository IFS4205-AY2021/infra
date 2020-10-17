#!/bin/bash

# Execute as root
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i lo -m comment --comment "Allow loopback connections" -j ACCEPT
iptables -A INPUT -p icmp -m comment --comment "Allow ping traffic" -j ACCEPT
iptables -A INPUT -s ifs4205-ay2020-1-i.comp.nus.edu.sg  -j ACCEPT
iptables -A INPUT -s ifs4205-ay2020-2-i.comp.nus.edu.sg -j ACCEPT
iptables -P INPUT DROP
iptables -P FORWARD DROP
