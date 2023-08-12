#! /usr/bin/env python3
'''Quick Debian setup.'''

import os

USER = os.getlogin()
PROGRAMS = [
	'ufw', 'vbetool', 'network-manager', 'htop', 'fail2ban', 'syncthing', 'tmux', 'aptitude'
	]


def update():
	print('\n>>> Updating and upgrading packages...\n')
	os.system('sudo apt -y update && sudo apt -y upgrade')

def install(desired_programs: list):
	print('\n>>> Installing programs...\n')
	for program in desired_programs:
		print(f'\n>>> Installing {program}...\n')
		os.system(f"sudo -y apt install {program}")

def ufw_setup():
	os.system('sudo ufw allow ssh')
	os.system('sudo ufw allow syncthing')
	os.system('sudo ufw enable')
	os.system('sudo ufw reload')

def syncthing_setup():
	os.system(f'sudo systemctl enable syncthing@{USER}.service')

if __name__ == '__main__':
	update()
	install(PROGRAMS)
	ufw_setup()
	syncthing_setup()
