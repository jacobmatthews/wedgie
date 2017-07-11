"""
This program compliments getWedge.py by being able to plot the npz files generated from getWedge.py.

Author: Austin Fox Fortino ,fortino@sas.upenn.edu
"""

import argparse, wedge_utils, os, pprint

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filenames', help='Input a list of filenames to be analyzed.', nargs='*', required=True)
parser.add_argument('-p', '--path', help='Path to save destination for png files.', default='./')
parser.add_argument('-s', '--single_plot', help='Plot a single plot from supplied npz files.', action='store_true')
parser.add_argument('-m', '--multi_plot', help='Plot 4 plots at once from supplied npz files.', action='store_true')
args = parser.parse_args()

if args.plot:
    for filename in args.filenames:
        if filename.split('.')[-2] == 'timeavg':
            wedge_utils.plot_timeavg(filename, args.save_path)
        elif filename.split('.')[-2] == 'blavg':
            wedge_utils.plot_blavg(filename, args.save_path)

elif args.multi_plot:
    wedge_utils.plot_multi_timeavg(args.filenames, args.save_path)