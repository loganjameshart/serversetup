#! /usr/bin/env python3
"""
About: Quick Debian server setup.
Author: Logan Hart
"""

import os
import subprocess

USER = os.getlogin()
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


def update() -> None:
    """Updates package sources and initiates upgrade."""

    print("\n>>> Updating and upgrading packages...\n")
    subprocess.run(["sudo", "apt", "-y", "update"])
    subprocess.run(["sudo", "apt", "-y", "upgrade"])


def install(desired_programs: list) -> None:
    """Install requested packages using apt."""

    print("\n>>> Installing programs...\n")
    for program in desired_programs:
        print(f"\n>>> Installing {program}...\n")
        subprocess.run(["sudo", "apt", "-y", "install", program])


def ufw_setup() -> None:
    """Creates firewall rules for necessary program sockets."""

    print(">>> Updating firewall...\n")
    subprocess.run(["sudo", "ufw", "allow", "ssh"])
    subprocess.run(["sudo", "ufw", "enable"])
    subprocess.run(["sudo", "ufw", "reload"])


if __name__ == "__main__":
    update()
    install(PROGRAMS)
    syncthing_setup()
    subprocess.run(["sudo", "apt", "autoremove"])
    ufw_setup()  # firewall reloads last in case of SSH disruption
