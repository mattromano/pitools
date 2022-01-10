# Raspberry Pi + Sense Hat ETH Price Alert
A tool to let you know how stressed you should be, every 15 minutes 

## Set-Up
### Pre-requisits:
#### Hardware:
- Raspberry Pi
- SenseHat (https://www.raspberrypi.com/products/sense-hat/)
#### Once cloned into the repo, enter in terminal:
- You will need to install requests to interact with Coingecko API: `pip install requests`
- Installing Sense Hat on the Pi: `sudo apt-get install sense-hat`
- Make the python file and executable: `sudo chmod +x PiETHAlert.py`
- Set up the automation in Crontab: `crontab -e`
  - In crontab enter the timing of the proccess automation, mine currently is set to every 15 minutes from 6AM to 8PM, every day of the week. Copy the below if you want the same: 
     - `0,15,30,45 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 * * /usr/bin/python2.7 /home/pi/eth_alert_sensehat/eth_alertv2.py`
     - To set up a custom timing refer to crontab documentation here: https://www.adminschoice.com/crontab-quick-reference

Once you've done all that you should be now recieving alerts on your Sense Hat's LED matrix every 15 minutes. You can also update the message of the update in the main python script.
