#!/usr/bin/python
#encoding:utf-8
'''file description ...'''

import re
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.VERBOSE)
b = re.compile(r"\d+\.(\d*)")
c = re.compile(r"(?P<first_name>\w+) (?P<last_name>\w+)", )

s = 'Malcolm Reynolds 12312.324324'
print a.search(s).group()
print b.search(s).groups()
print c.search(s).groupdict()
print c.search(s).lastindex
print c.search(s).lastgroup

# s="abcdefghijklmnopqrstuvwxyz python"
# pattern=r'(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w) (?P<name>\w+)'
# m=re.search(pattern,s)
# print m.expand(r'\1'), m.expand(r'\10'), m.expand(r'\g<10>'), m.expand(r'hello \g<name>')




	
	