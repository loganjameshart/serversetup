#! /usr/bin/env python3
"""
About: Quick Debian server setup.
Author: Logan Hart
"""

import subprocess

PROGRAMS = [
    "black",
    "ufw",
    "vbetool",
    "network-manager",
    "htop",
    "fail2ban",
    "tmux",
    "aptitude",
    "python3-pip",
]


def update_packages() -> None:
    """Updates package sources and initiates upgrade."""

    print("\n>>> Updating and upgrading packages...\n")
    subprocess.run(["sudo", "apt", "-y", "update"])
    subprocess.run(["sudo", "apt", "-y", "upgrade"])


def install_programs(desired_programs: list) -> None:
    """Install requested packages using apt."""

    print("\n>>> Installing programs...\n")
    for program in desired_programs:
        print(f"\n>>> Installing {program}...\n")
        subprocess.run(["sudo", "apt", "-y", "install", program])


def setup_firewall() -> None:
    """Creates firewall rules for necessary program sockets."""

    print(">>> Updating firewall...\n")
    subprocess.run(["sudo", "ufw", "allow", "ssh"])
    subprocess.run(["sudo", "ufw", "enable"])
    subprocess.run(["sudo", "ufw", "reload"])


if __name__ == "__main__":
    update_packages()
    install_programs(PROGRAMS)
    subprocess.run(["sudo", "apt", "autoremove"])
    firewall_setup()  # firewall reloads last in case of SSH disruption
