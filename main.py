import os
import sys
import string
import colorama
from colorama import Fore

class marseille:

    def marseille1337():
        try:
            json = {
                 "clientkey": "capmonster api"
            }
            r = session.post('https://api.capmonster.cloud/getBalance', json=json).result()
            if r.json()['errorId'] == 1:
                return 'error, information about it is in the errorCode property'
            if r.json()['errorId'] == 0:
                return r.json()['balance']
        except:
            pass

    print(f"[\x1b[38;5;199m$\x1b[0m] Current Balance: {marseille()}")
