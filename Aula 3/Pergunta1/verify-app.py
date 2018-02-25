# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# verifySignature-app.py
#
# Cripto-7.4.1 - Commmad line app to exemplify the usage of verifySignature
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
Command line app that receives signer's public key from file and Data, Signature, Blind Components and
prComponents from STDIN and writes a message to STDOUT indicating if the signature is valid..
"""

import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils

def parseArgs():
    if (len(sys.argv) != 10):
        print("Error usage")
    else:

         if(sys.argv[1] == '-cert' and sys.argv[3] == '-msg'
         and sys.argv[5] == '-sDash' and sys.argv[7] == '-f'): 
                data = open(sys.argv[4],"r")
                signature = open(sys.argv[6],"r")
                bcomponents = open(sys.argv[8],"r")
                pRcomponents =  open(sys.argv[9],"r")
                eccPublicKeyPath = sys.argv[2]
                main(eccPublicKeyPath,data,signature,bcomponents,pRcomponents)

def showResults(errorCode, validSignature):
    print("Output")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPublicKeyPath,data,signature,bcomponents,pRcomponents):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    print("Input")
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature.read(), bcomponents.read(), pRcomponents.read(), data.read())
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
