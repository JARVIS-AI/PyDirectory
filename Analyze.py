#!/usr/bin/python
# coding: utf-8

# def Help():
#     print()
#     print(" " + 55 * "-")
#     print("|                   Directory Worker                    |")
#     print("| Written by Jarvis Mercer                              |")
#     print("| https://github.com/JARVIS-AI                          |")
#     print("| Version = " + Version() + "                                       |")
#     print("| Choose your option                                    |")
#     print(" " + 55 * "-")
#     print()


from fnmatch import filter
import os
import os.path
import sys
import pprint
import argparse

def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Print version
    parser.add_argument("-v", "--version", action="version", version='%(prog)s - Version 2.0.3')

    # NEED HELP FPR MAKING THIS POSSIBLE 
    parser.add_argument("-nd", "--number-directory", dest='NumDirectory', action='store',  help="Number of items in Directory")

    parser.add_argument("-d", "--directory", dest='Directory', action='store',  help="List items of Directory")
    # Parse arguments
    args = parser.parse_args()

    return args


def Menu():
    print()
    print(" " + 55 * "-")
    print("|                   Directory Worker                    |")
    print("|                                                       |")
    print("| https://github.com/JARVIS-AI                          |")
    print("|                                                       |")
    print("| Choose your option                                    |")
    print(" " + 55 * "-")
    print()


def InBox():
        print("| " + str + ((42-len(str)) * " ") + "|")


def Line():
    print(" " + 45 * "-")


def Logical():
    print("Enter your directory, MUST BE STRING")
    dir = input()
    list = os.listdir(dir) # dir is your directory path
    number_files = len(list)
    print (number_files)
    return dir

if __name__ == '__main__':
    args = parseArguments()


if args.NumDirectory:
    print(len(os.listdir(args.Directory)))
    exit(0)

if args.Directory:
    pprint.pprint((os.listdir(args.Directory)))
    exit(0)

Menu()
Logical()


