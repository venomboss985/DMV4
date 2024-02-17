# SETUP STEPS

1. Clone repo
2. Create a python venv environment with `python -m venv env`
3. Activate the venv with `. env/bin/activate`
4. Install dependencies by running `pip install -r requirements.txt`
5. Test the installation by running `./getCamera.py`
6. Test the script works by running `./dmv4.py`
7. If the script does not run from the previous command, run `chmod +x dmv4.py` and rerun the script
8. Run `sudo crontab -e` and add the line `@reboot /home/$USER/DMV4/dmv4.py`
9. Save and reboot the Pi (recorded footage will be output to the `outputs/` folder)

# DISABLING START ON BOOT

1. Run `sudo crontab -e` and remove or comment out the previously added line
2. Save and reboot
