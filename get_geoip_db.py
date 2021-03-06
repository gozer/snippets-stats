#!/usr/bin/env python3

import time
import sys,os,errno,re,argparse
from datetime import datetime
from subprocess import call
from config import config

proxies = config['proxies']

def print_debug(level, message):
  if debug >= level:
    print("[%s] %s" % (datetime.now(),message))

def get_geoip_db():

  # TODO

if __name__ == "__main__":
 
  parser = argparse.ArgumentParser(description="Get latest GeoIP DB from MaxMind")
  parser.add_argument('-d', '--debug', action='store', help='debug level', type=int, default=3)
  #parser.add_argument('-f', '--force', action='store_true', help='force changes even if there are a lot')
  args = parser.parse_args()

  debug = args.debug

  print_debug(1, "Starting...")

  get_geoip_db()
