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
    "syncthing",
    "tmux",
    "aptitude",
    "python3-pip",
]


def update() -> None:
    """Updates package sources and initiates upgrade."""

    print("\n>>> Updating and upgrading packages...\n")
    subprocess.run("sudo apt -y update", shell=True)
    subprocess.run("sudo apt -y upgrade", shell=True)


def install(desired_programs: list) -> None:
    """Install requested packages using apt."""

    print("\n>>> Installing programs...\n")
    for program in desired_programs:
        print(f"\n>>> Installing {program}...\n")
        subprocess.run(f"sudo apt -y install {program}", shell=True)


def ufw_setup() -> None:
    """Creates firewall rules for necessary program sockets."""

    subprocess.run("sudo ufw allow ssh", shell=True)
    subprocess.run("sudo ufw allow syncthing", shell=True)
    subprocess.run("sudo ufw enable", shell=True)
    subprocess.run("sudo ufw reload", shell=True)


def syncthing_setup():
    """Enables Syncthing."""

    subprocess.run(f"sudo systemctl enable syncthing@{USER}.service", shell=True)


if __name__ == "__main__":
    update()
    install(PROGRAMS)
    syncthing_setup()
    subprocess.run("sudo apt autoremove", shell=True)
    ufw_setup()  # firewall reloads last in case of SSH disruption
