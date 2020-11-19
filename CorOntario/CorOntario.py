from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# This prevents a window opening on the workspace
#headless_options = Options()
#headless_options.add_argument('--headless')

# Opens Firefox
# driver = Firefox(options=headless_options)
driver = Firefox()

# Keeps Firefox minimized
driver.minimize_window()

# Waits 10 seconds
driver.set_page_load_timeout(10)

# Loads google.com
driver.get("https://covid-19.ontario.ca/data")

# Finds DIV Class for all cases and Change
# DIV class for all cases and data: ontario-column ontario-small-12 ontario-medium-6  ontario-margin-top-24-!
cases = driver.find_element_by_class_name("cviz-label-value").text

# Closes the browser once finished script
driver.quit()

# The following code is to handle taking the data and sending it as an SMS message to your phone
# You can use https://freesmsgateway.info/ to get the proper gateway information of your device

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( '<from email>', '<password>' )

# Send text message through SMS gateway of destination number
server.sendmail( '<from email>', '<carrier gateway>', cases)

# Prints case count once browser closes and data is found
print(cases)
