from __future__ import print_function
import argparse
import os

default_path = os.path.join("data")
default_news_path = os.path.join(default_path, 'rating.csv')

parser = argparse.ArgumentParser(description='cmdArgs')
parser.add_argument('--output', type=str, default='news_ouput.csv',
                help='filename to write analysis output in CSV format')
parser.add_argument('--path', required=False, type=str, default=default_news_path, help='directory where news data reside')
parser.add_argument('--channel', type=str, default='', help='which channel we parsing')
parser.add_argument('--userfile', type=str, default='users.json', help='users profile information')

cfg = parser.parse_args()
# print(cfg)



# Print the values of the arguments
print(f'Output File: {cfg.output}')
print(f'Path: {cfg.path}')
print(f'Channel: {cfg.channel}')
print(f'Userfile: {cfg.userfile}')