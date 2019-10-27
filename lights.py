#!/usr/bin/env python3
import argparse
import configparser
from phue import Bridge

cfg = configparser.ConfigParser()
cfg.read('config.cfg')
ip = cfg['Bridge']['ip']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage phue lights.')
    parser.add_argument('--off',
                        help='set it on or off',
                        action='store_true')

    parser.add_argument('--id',
                        help='id of the light to handle')

    parser.add_argument('--ip',
                        help='IP of the bridge',
                        default=ip)
    args = parser.parse_args()

    b = Bridge(args.ip)
    if args.id:
        lid = int(args.id)
        b.set_light(lid, 'on', not b.get_light(lid, 'on'))
    elif args.off:
        b.set_light(1, 'on', False)
    else:
        b.set_light(1, 'on', not b.get_light(1, 'on'))
