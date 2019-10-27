#!/usr/bin/env python3
import argparse
from phue import Bridge

b = Bridge('192.168.0.10')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage phue lights.')
    parser.add_argument('--off',
                        help='set it on or off',
                        action='store_true')
    args = parser.parse_args()
    b.set_light(1, 'on', not args.off)
