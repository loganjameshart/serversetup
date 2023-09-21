# Quick Debian Server Setup Script

## Description

This Python script is designed to simplify the process of setting up a Debian server by automating various tasks. It updates package sources, installs essential programs, configures the Nano text editor, and sets up a basic firewall.

## Author

- Author: Logan Hart

## Usage

1. **Requirements**: Ensure you have Python 3 installed on your Debian system (although it's usually installed by default).

2. **Configuration**:
   - Modify the `PROGRAMS` list to include the programs you want to install.
   - Customize the `NANO_CONFIG` list to adjust Nano editor settings if needed
       - Here I set tabs to equal 4 spaces and make Nano recognize them as such
   - Review and customize the `APT_CONFIG` list to specify your desired APT package sources.

3. **Running the Script**:
   - Run the script with administrator privileges using the following command:
     ```python
     sudo python3 debiansetup.py
     ```

4. **Script Actions**:
   - The script performs the following actions:
     - Updates package sources to specified APT sources.
     - Upgrades installed packages.
     - Installs a list of specified programs.
     - Configures the Nano text editor.
     - Sets up a basic firewall with SSH access allowed.

5. **Note**: Review and understand the actions performed by the script before running it on a production server. Ensure that you have proper backups and security measures in place.

## Important Notes

- The script assumes that it's being run on a Debian-based system.
- Passwords and sensitive information should not be hardcoded in scripts for security reasons.
