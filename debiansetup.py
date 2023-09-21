#!/usr/bin/env python3
"""
About: Quick Debian server setup.
Author: Logan Hart
"""

import os
import subprocess
from pathlib import Path

USER = os.getlogin()
APT_SOURCES = "/etc/apt/sources.list"
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

NANO_CONFIG = ["set tabsize 4\n", "set tabstospaces"]

APT_CONFIG = [
    "deb http://deb.debian.org/debian/ bookworm main non-free-firmware non-free\n",
    "deb-src http://deb.debian.org/debian/ bookworm main non-free-firmware non-free\n",
    "\n",
    "deb http://security.debian.org/debian-security bookworm-security main non-free-firmware\n",
    "deb-src http://security.debian.org/debian-security bookworm-security main non-free-firmware\n",
    "\n",
    "# bookworm-updates, to get updates before a point release is made;\n",
    "# see https://www.debian.org/doc/manuals/debian-reference/ch02.en.html_updates_and_backports\n",
    "deb http://deb.debian.org/debian/ bookworm-updates main non-free-firmware\n",
    "deb-src http://deb.debian.org/debian/ bookworm-updates main non-free-firmware\n",
    "\n",
    "# This system was installed using small removable media\n",
    "# (e.g. netinst, live or single CD). The matching 'deb cdrom'\n",
    "# entries were disabled at the end of the installation process.\n",
    "# For information about how to configure apt package sources,\n",
    "# see the sources.list(5) manual.\n",
]


def backup_file(file_path: str) -> None:
    """Backs up a file to the home directory."""

    file_name = Path(file_path).name
    with open(file_path) as original_file:
        backup_data = original_file.read()
    with open(f"/home/{USER}/{file_name}.bak", "w") as backup_file:
        backup_file.write(backup_data)


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

    print(">>> Updating firewall...\n")
    subprocess.run(["sudo", "ufw", "allow", "ssh"])
    subprocess.run(["sudo", "ufw", "enable"])
    subprocess.run(["sudo", "ufw", "reload"])


def nano_config() -> None:
    print("\n>>> Updating Nano config file...\n")
    with open(f"/home/{USER}/.nanorc", "w") as config_file:
        config_file.writelines(NANO_CONFIG)


if __name__ == "__main__":
    update_packages()
    install_programs(PROGRAMS)
    subprocess.run(["sudo", "apt", "autoremove"])
    nano_config()
    setup_firewall()  # firewall reloads last in case of SSH disruption
