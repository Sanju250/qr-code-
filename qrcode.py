import time
from pync import Notifier

# Get inputs
title = input("\nTitle of reminder: ")
msg = input("Message: ")
minutes = float(input("How many minutes? "))

# Convert minutes to seconds
seconds = minutes * 60

# Notify user that the reminder is set
print("\nReminder set successfully!\n")

# Wait for the specified time
time.sleep(seconds)

# Display the notification using pync
Notifier.notify(
    message=msg,   # Message body of the notification
    title=title    # Title of the notification
)
