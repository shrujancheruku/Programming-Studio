import os
"""
Simple script to run the terminal commands to update the list and log
"""


def update():
    os.system('svn list --xml --recursive https://subversion.ews.illinois.edu/svn/sp17-cs242/scheruk2 '
              '> Parser/data/svn_list.xml')
    os.system('svn log --verbose --xml https://subversion.ews.illinois.edu/svn/sp17-cs242/scheruk2 '
              '> Parser/data/svn_log.xml')

update()