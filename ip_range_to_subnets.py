#!/usr/bin/env python3

"""
Summarize an IP address range.
"""

import sys
import argparse

from netaddr import IPAddress, iter_iprange, cidr_merge


def check_ip_address(ip_addr):

    """
    Check that ip_addr is a valid IP address.
    """

    try:
        IPAddress(ip_addr)
    except Exception as exception:
        return False

    return True


def ip_range_to_subnets(first, last):

    """
    Summarize the IP address range in subnets.
    """

    return cidr_merge(list(iter_iprange(first, last)))


def main(argv):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-first",
            action="store",
            dest="first",
            type=str,
            required=True,
            help="the first IP address in the range."
        )
        parser.add_argument(
            "-last",
            action="store",
            dest="last",
            type=str,
            required=True,
            help="the last IP address in the range."
        )
        if len(argv) < 3:
            parser.print_help()
            return -1
        args = parser.parse_args()

        if not check_ip_address(args.first):
            print("{} is not a valid IP address.".format(args.first), file=sys.stderr)
            return 0

        if not check_ip_address(args.last):
            print("{} is not a valid IP address.".format(args.last), file=sys.stderr)
            return 0

        subnets = ip_range_to_subnets(args.first, args.last)
        for subnet in subnets:
            print(subnet)

    except KeyboardInterrupt as keyboard_exception:
        print(keyboard_exception, file=sys.stderr)

    except Exception as exception:
        print(exception, file=sys.stderr)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))