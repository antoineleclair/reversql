#!/usr/bin/env python2
import sys, os, re

def print_reverse(filename):
    with open(filename) as f:
        for create in reversed(list(creates(f))):
            print 'DROP %s %s;' % create

def creates(f):
    regex = re.compile(r'CREATE'
                       r'\s+'
                       r'(?P<table_or_sequence>TABLE|SEQUENCE)'
                       r'\s+'
                       r'(?P<name>\w+)'
                       r'\s*\(?', flags=re.IGNORECASE)
    for line in f:
        match = regex.match(line)
        if match is not None:
            yield match.group('table_or_sequence').upper(), match.group('name')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s filename' % sys.argv[0])
    filename = sys.argv[1]
    try:
        with open(filename) as f: pass
    except IOError as e:
        sys.exit('File %s does not exist.' % sys.argv[0])
    print_reverse(filename)
