#!/usr/bin/env python

import tweepy
import argparse
import json

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


def get_args(argv=None):
    parser = argparse.ArgumentParser(description='''
                    Queries the Twitter API for a Twitter list 
                    or file of lists given at the command line 
                    and returns a list of usernames.''')

    input = parser.add_mutually_exclusive_group(required=True)
    input.add_argument("-u", "--url", nargs=1, type=str, help="url of single list")
    input.add_argument("-f", "--file", nargs=1, type=str, help="file of list URLs")
    
    parser.add_argument("-o", "--output", nargs=1, type=str, help='output file.')
    
    return parser.parse_args(argv)
    
    
def do_auth(token_dict):
    auth = tweepy.OAuthHandler(token_dict["consumer_key"], token_dict["consumer_secret"])
    auth.set_access_token(token_dict["access_token"], token_dict["access_token_secret"])
    return tweepy.API(auth)
    
    
def gather_members(l):
    l_id = l.split("/")[5]
    try:
        for user in tweepy.Cursor(api.list_members, list_id=l_id).items():
            write_screen_name(user.screen_name)	
    except Exception as e:
        print("failed to collect %s error %s" % (l_id,e))
    
    
def write_screen_name(name):
    if args.output:
         outfile.write("%s\n" % name)
    else:
        print(name)
        
        
## SET-UP ##
token_json = get_file_contents("api_key.json")
token_dict = json.loads(token_json)
api = do_auth(token_dict)

## MAIN ##
args = get_args()

if args.file:
    f = open(args.file[0])
    lists = [url.rstrip('\n') for url in f]
    f.close
elif args.url:
    lists = args.url
    
if args.output:
    print("writing to %s" % args.output[0])
    outfile = open(args.output[0], 'w')
    
for l in lists:
    print("#### %s" % l)
    gather_members(l)

