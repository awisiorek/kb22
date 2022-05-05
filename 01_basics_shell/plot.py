#!/usr/bin/env python3
import argparse
import sys
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='write a plot to an image file')
parser.add_argument(
    '-l', '--logarithmic', help='use logarithmic scale', action='store_true')
parser.add_argument(
    '-o', '--out', help='set output file name', type=str, default='out.png')
args = parser.parse_args()

nums = [int(num) for num in sys.stdin.readlines()]
if args.logarithmic:
    plt.xscale("log")
    plt.yscale("log")
plt.plot(nums)
# Alternativ: plt.plot
plt.savefig(args.out)
