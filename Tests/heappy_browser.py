#!/usr/bin/python
# Copyright (C) 2012 Allis Tauri <allista@gmail.com>
# 
# degen_primer is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# degen_primer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
Created on Feb 21, 2014

@author: Allis Tauri <allista@gmail.com>
'''

import sys, os
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser('Launche heappy profile browser with given profile.')
    parser.add_argument('profile', type=str, nargs='?', metavar='file.hpy', default=None)
    args = parser.parse_args()
    profile = args.profile
    if profile is not None:
        if not os.path.isfile(profile):
            print 'No such file: %s' % profile
            sys.exit(1)
    #launch heappy profile browser
    from guppy import hpy
    h = hpy()
    try: h.pb(profile)
    except KeyboardInterrupt: sys.exit(0) 