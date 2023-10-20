#!/usr/bin/env python3
"""
About: Quick Debian server setup. Run with sudo privileges.
Author: Logan Hart
"""

import os
import subprocess
import shutil
from pathlib import Path

USER = os.getlogin()
APT_SOURCES = "/etc/apt/sources.list"
PROGRAMS = [
    "black",
    "ufw",
#    "vbetool",
    "network-manager",
    "htop",
#    "fail2ban",
    "tmux",
    "aptitude",
    "python3-pip",
    "gcc",
    "build-essential",
    "firmware-b43-installer",
    "w3m",
    "tty-clock",
    "neofetch"
]

NANO_CONFIG = ["set tabsize 4\n", "set tabstospaces"]

# I never compile from source, so I remove those source links
APT_CONFIG = [
    "deb http://deb.debian.org/debian/ bookworm main non-free-firmware non-free\n",
    "deb http://security.debian.org/debian-security bookworm-security main non-free-firmware\n",
    "deb http://deb.debian.org/debian/ bookworm-updates main non-free-firmware\n"
]


def backup_file(file_path: str) -> None:
    """Backs up a file to the home directory."""

    file_name = Path(file_path).name
    print(f"\n>>> Backing up {file_path}...\n")
    shutil.copy2(file_path, f"/home/{USER}/{file_name}.bak")


def update_packages() -> None:
    """Updates package sources and initiates upgrade."""

    print("\n>>> Updating and upgrading packages...\n")
    backup_file(APT_SOURCES)
    with open(APT_SOURCES, "w") as apt_config_file:
        apt_config_file.writelines(APT_CONFIG)

    subprocess.run(["sudo", "apt", "-y", "update"])
    subprocess.run(["sudo", "apt", "-y", "upgrade"])


def install_programs(desired_programs: list) -> None:
    """Install requested packages using apt."""

    print("\n>>> Installing programs...")
    for program in desired_programs:
        print(f"\n>>> Installing {program}...\n")
        subprocess.run(["sudo", "apt", "-y", "install", program])


def setup_firewall() -> None:
    """Creates firewall rules for necessary program sockets."""

    print("\n>>> Updating firewall...\n")
    subprocess.run(["sudo", "ufw", "allow", "ssh"])
    subprocess.run(["sudo", "ufw", "enable"])
    subprocess.run(["sudo", "ufw", "reload"])


def nano_config() -> None:
    """Edit Nano editor config file to use tab as four spaces."""

    print("\n>>> Updating Nano config file...\n")
    with open(f"/home/{USER}/.nanorc", "w") as config_file:
        config_file.writelines(NANO_CONFIG)


if __name__ == "__main__":
    update_packages()
    install_programs(PROGRAMS)
    subprocess.run(["sudo", "apt", "autoremove"])
    nano_config()
    setup_firewall()  # firewall reloads last in case of SSH disruption
