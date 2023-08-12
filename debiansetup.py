#! /usr/bin/env python3
'''Quick Debian setup.'''

import os

USER = os.getlogin()

PROGRAMS = [
	'ufw', 'vbetool', 'network-manager', 'htop', 'fail2ban', 'syncthing', 'tmux'
	]


def install(desired_programs: list):
	for program in desired_programs:
		os.system(f"sudo apt install {program}")

def ufw_setup():
	os.system('sudo ufw allow ssh')
	os.system('sudo ufw allow syncthing')
	os.system('sudo ufw reload')

def syncthing_setup():
	os.system('syncthing')
	os.system(f'sudo systemctl enable syncthing@{USER}.service')

if __name__ == '__main__':
	install(PROGRAMS)
	ufw_setup()
	syncthing_setup()
