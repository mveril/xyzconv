#!/usr/bin/env python3
import enum
import argparse
import sys
class Units(enum.IntEnum):
  angstrom=enum.auto()
  bohr=enum.auto()
  au=int(bohr)
def convert(value,_from,to):
  # 1 Bohr = 0.529177208 Angstrom source http://greif.geo.berkeley.edu/~driver/conversions.html
  factor=0.529177208
  if _from==to:
    return value
  elif _from==Units.bohr and to==Units.angstrom:
    return value*factor
  elif _from==Units.angstrom and to==Units.bohr:
    return value/factor
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--from', type=str, dest='_from', choices=[t.name for t in list(Units)],default=Units.angstrom.name)
parser.add_argument('--to',type=str, choices=[t.name for t in list(Units)],default=Units.angstrom.name)
args = parser.parse_args()
args.to=Units[args.to]
args._from=Units[args._from]
infile=sys.stdin
outfile=sys.stdout
inlines=infile.readlines()
outlines=inlines[:1]
for line in inlines[2:]:
  sp=line.split(" ")
  for i in range(1,4):
    sp[i]=convert(float(sp[i]),args._from,args.to)
  outlines.append(f'{sp[0]:<3} {sp[1]:10.8f} {sp[2]:10.8f} {sp[3]:10.8f}\n')
outfile.writelines(outlines)