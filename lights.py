#!/usr/bin/env python3
import argparse
import configparser
from phue import Bridge

def set_light(id, state):
    b.set_light(id, 'on', state)

def main(args):
    global b
    b = Bridge(args.ip)
    if args.id:
        lid = int(args.id)
        if args.off:
            set_light(lid, False)
        else:
            set_light(lid, not b.get_light(lid, 'on'))

    elif args.off:
        set_light(1, False)
    else:
        set_light(1, not b.get_light(1, 'on'))


if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    cfg.read('config.cfg')
    ip = cfg['Bridge']['ip']

    parser = argparse.ArgumentParser(description='Manage phue lights.')
    parser.add_argument('--off',
                        help='set it on or off',
                        action='store_true')
    parser.add_argument('--id',
                        help='id of the light to handle')
    parser.add_argument('--ip',
                        help='IP of the bridge',
                        default=ip)
    main(parser.parse_args())

