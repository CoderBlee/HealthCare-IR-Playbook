#!/bin/bash

# Script to install necessary tools for incident response

# Update package lists
sudo apt-get update

# Install example tools
sudo apt-get install -y wireshark nmap

echo "Tools installation complete."
