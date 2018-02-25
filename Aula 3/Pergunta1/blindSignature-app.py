# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateBlindSignature-app.py
#
# Cripto-7.2.1 - Commmad line app to exemplify the usage of generateBlindSignature
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
Command line app that receives signer's private key from file and Passphrase, Blind message and
initComponents from STDIN and writes Blind signature to STDOUT.
"""

from eVotUM.Cripto import utils
import sys
from eVotUM.Cripto import eccblind


def parseArgs():
    if (len(sys.argv) != 5):
        print("Error usage")
    else:
        if(sys.argv[1] == '-key' and sys.argv[3] == '-bmsg'): 
                blindM = open(sys.argv[4],"r")
                eccPrivateKeyPath = sys.argv[2]
                main(eccPrivateKeyPath,blindM)

def showResults(errorCode, blindSignature):
    print("Output")
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
        with open("bs.txt", "w") as text_file1:
              text_file1.write(blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main(eccPrivateKeyPath,blindM):
    pemKey = utils.readFile(eccPrivateKeyPath)
    print("Input")
    passphrase = raw_input("Passphrase: ")
    initComponents = open("init.txt","r")
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM.read(), initComponents.read())
    showResults(errorCode, blindSignature)

if __name__ == "__main__":
    parseArgs()