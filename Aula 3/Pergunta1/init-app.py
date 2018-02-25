# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# initSigner-app.py 
#
# Cripto-7.0.2 - Commmad line app to exemplify the usage of initSigner
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that writes initComponents and pRDashComponents to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind

def pRDashComponent():
    _,pRDashComponents = eccblind.initSigner()
    print("pRDashComponents: %s" % pRDashComponents)

def parseArgs():

    if len(sys.argv) == 1:
        pRDashComponent()
    
    if len(sys.argv) == 2 and sys.argv[1] == '-init':
        main()
 
def main():
    initComponents, pRDashComponents = eccblind.initSigner()

    msg = raw_input("Mensagem a assinar: ")
    print("Init components: %s" % initComponents)
    print("pRDashComponents: %s" % pRDashComponents)
    with open("init.txt", "w") as text_file1:
        text_file1.write(initComponents)
    with open("pRDash.txt", "w") as text_file2:
        text_file2.write(pRDashComponents)
    with open("msg.txt", "w") as text_file3:
        text_file3.write(msg)
        

if __name__ == "__main__":
    parseArgs()
