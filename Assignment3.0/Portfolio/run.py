import os
"""
Simple script to update the list and log and then run the app
Run this to use the website
"""

print("Updating SVN records.....")
os.system("python3 updateSVN.py")
print("SVN records updated!")
print("Starting app.....")
os.system("python3 Portfolio.py")
