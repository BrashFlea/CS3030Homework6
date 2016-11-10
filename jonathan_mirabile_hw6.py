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
from collections import Counter
"""
Apache Server Error Log Report Tool
Args:
    URL of an Apache server error log file
Returns:
    Print report of top 25 errors in log file to screen
"""
#TODO Remove before submisson
url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"

def fetch_url(url):
    """
    Fetch list of errors from URL
    Args:
        url: The URL of an Apache error log file
    Returns:
        A list of errors from the given document
    """
    resource = urllib.request.urlopen(url)
    content = resource.read().decode()
    #Regex checks for 4 groups:
    #1: []
    #2: []
    #3: []
    #4: Rest of string
    #Then ignores groups 1-3 and leaves group 4 (the verbose error) 
    dlist = re.findall(r'(?:\[.*?\]) (?:\[.*?\]) (?:\[.*?\]) (.*)', content)
    #Sort list and print out the nth most common
    slist = Counter(dlist).most_common(5)
    print(slist)
    return
    

    


# Main function
def main():
    fetch_url(url)
    return


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)

