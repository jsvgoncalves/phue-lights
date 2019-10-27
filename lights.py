#!/usr/bin/env python3
import argparse
from phue import Bridge

b = Bridge('192.168.0.10')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage phue lights.')
    parser.add_argument('--off',
                        help='set it on or off',
                        action='store_true')

    parser.add_argument('--id',
                        help='id of the light to handle')
    args = parser.parse_args()

    if args.id:
        lid = int(args.id)
        b.set_light(lid, 'on', not b.get_light(lid, 'on'))
    elif args.off:
        b.set_light(1, 'on', False)
    else:
        b.set_light(1, 'on', not b.get_light(1, 'on'))
