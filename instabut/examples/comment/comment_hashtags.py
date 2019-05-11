"""
    instabot example

    Dependencies:
        You must have a file with comments to post.
        The file should have one comment per line.

    Notes:
        You can change file and add there your comments.
"""

import sys
import os
import argparse

sys.path.append(os.path.join(sys.path[0], '../../'))
from instabot import Bot
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('filepath', type=str, help='filepath')
parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
#parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()


comments_file_name = args.filepath

hashtags =  args.hashtags

if not os.path.exists(comments_file_name):
    print("Can't find '%s' file." % comments_file_name)
    exit()

bot = Bot(comments_file=comments_file_name)
bot.login(username=args.u, password=args.p)

for hashtag in args.hashtags:
    bot.comment_hashtag(hashtag)
bot.logout()
