# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# unblindSignature-app.py
#
# Cripto-7.3.1 - Commmad line app to exemplify the usage of unblindSignature
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
Command line app that receives Blind signature, Blind components and prDashComponents
from STDIN and writes the unblinded signature to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind

def parseArgs():
    if (len(sys.argv) != 5):
        print("Error usage")
    else:
        if(sys.argv[1] == '-s' and sys.argv[3] == '-RDash'): 
              pRDashComponents = open(sys.argv[4],"r")
              blindSignature = open(sys.argv[2],"r")
              blindComponents = open("bcomponents.txt","r")
              main(pRDashComponents,blindSignature,blindComponents)

def showResults(errorCode, signature):
    print("Output")
    if (errorCode is None):
        print("Signature: %s" % signature)
        with open("signature.txt", "w") as text_file:
                text_file.write(signature)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")
    elif (errorCode == 2):
        print("Error: blind components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind signature format")

def main(pRDashComponents,blindSignature,blindComponents):
    print("Input")
    errorCode, signature = eccblind.unblindSignature(blindSignature.read(), pRDashComponents.read(), blindComponents.read())
    showResults(errorCode, signature)

if __name__ == "__main__":
    parseArgs()
