#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys
import urllib
import urllib.request
import re
from collections import Counter, OrderedDict

"""
Apache Server Error Log Report Tool
Args:
    URL of an Apache server error log file
Returns:
    Print report of top 25 errors in log file to screen
"""


def help():
    """
    Displays usage details
    """
    print("Usage is ./jonathan_mirabile_hw6.py <file Input>")


def fetch_url(url):
    """
    Fetch list of errors from URL
    Note: Best viewed in full screen as errors are verbose
    Args:
        url: The URL of an Apache error log file
    Returns:
        A report with the top 25 errors from the document
    """
    resource = urllib.request.urlopen(url)
    content = resource.read().decode()
    #Regex checks for 4 groups:
    #1: []
    #2: [error]
    #3: []
    #4: Rest of string
    #Then ignores groups 1-3 and leaves group 4 (the verbose error) 
    dlist = re.findall(r'(?:\[.*?\]) (?:\[error\]) (?:\[.*?\]) (.*)', content)
    #Take the top 25 errors and turn it into an ordered dictionary
    sdict = OrderedDict(Counter(dlist).most_common(25))
    
    print("*** Top 25 Errors***")
    for error, value in sdict.items():
        print('Count: {:<6} Error: {}'.format(value, error))

    return
    

# Main function
def main(url):
    fetch_url(url)
    return


if __name__ == "__main__":
    # Call Main
    if len(sys.argv) == 1:
        help()
        exit(1)
    else:
        print("Fetching file...")
        main(sys.argv[1])
        exit(0)

