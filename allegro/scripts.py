# -*- coding:UTF-8 -*-

import sys,lib,argparse

parser = argparse.ArgumentParser(description='Allegro item link and price getter.')
parser.add_argument('item_name', nargs = 1)

def parse_args():
    '''function that uses argparse to get user input
    input: ---
    output: dictionary'''
    return vars(parser.parse_args()) #make dict out of Namespace object

def main():
    '''function that claims it does the job '''
    item = parse_args()['item_name']
    try:
        url, price = lib.allegro_api(item)
        print ''.join(['Link do przedmiotu: ', url, ' Cena: ', str(price)])
        pass
    except lib.NoItemException:
        sys.exit('Wrong item name specified, can\'t get results')


main()
