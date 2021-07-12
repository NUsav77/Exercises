'''
Get the domain from an email address
'''

import re

email = str(input())

re.findall(r'^@/w*^[.com]', email)