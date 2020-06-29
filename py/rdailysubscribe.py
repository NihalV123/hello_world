# allarr = {}
# remarr={}
# reverse_d={}
# val  = 'hi'
# for tr100 in open("redditurl.txt", "r"):  #trending 1000 reddits
#     tr100 = tr100.replace(',', '')
#     tr100 = tr100.replace('https://wwww.reddit.com/r/', '')
#     key = str(tr100)
#     key = key.replace('\n', '')
#     allarr[key] = val
# print(allarr)
# print(len(allarr))

# for currsub in open("currentsub.txt", "r"):
#     currsub = currsub.replace('Subreddit(display_name=', '') #current subscribbed reddits
#     currsub = currsub.replace('\'', '').replace(')', '').replace(')]', '').replace('[(', '').replace(']', '').replace('[', '')
#     key = str(currsub)
#     key = key.replace(' \n', '')
#     key = key.replace(' ', '')
#     remarr[key] = val
# print(remarr)
# print(len(remarr))

# for vals in allarr:
#     key = str(vals)
#     reverse_d[key] = val
# print(len(reverse_d))

# for vals in remarr:
#     element = reverse_d.pop(vals,'apple')
# print(reverse_d)

# for vals in reverse_d:
#     key = str(vals)
#     f= open("newreddit.txt","a+")
#     f.write(vals+"\n")
#     f.close() 
# print("done")
 




# import random
# import webbrowser
# import praw
# import time
# from prawcore.exceptions import Forbidden     #new sub
# i = 0
# reddit = praw.Reddit(client_id="f4QT47zgSpuueA",
#                      client_secret="Cr_qLwp-0OHDBdSxnilAdO_hChA",
#                      password="QwErTyUi12345!!",
#                      user_agent="Nihalv123",
#                      username="Nihalv123")

# for each_line in open("newreddit.txt", "r"):
#     subreddit = reddit.subreddit(each_line)
#     try:
#         subreddit.subscribe()
#         print(subreddit)
#     except Forbidden:
#         print('waiting 5 sec ....')
#         time.sleep(5)

# with open('newreddit.txt', 'r') as fin:
#     data = fin.read().splitlines(True)
# with open('newreddit.txt', 'w') as fout:
#     fout.writelines(data[66:])





import random
import webbrowser
import praw
import time
from prawcore.exceptions import Forbidden     #daily sub
i = 0
reddit = praw.Reddit(client_id="f4QT47zgSpuueA",
                     client_secret="Cr_qLwp-0OHDBdSxnilAdO_hChA",
                     password="QwErTyUi12345!!",
                     user_agent="Nihalv123",
                     username="Nihalv123")
for submission in reddit.subreddit('trendingsubreddits').hot(limit=1):
    sreddits = submission.title.split(' ',4)[4]
    sredditraw = sreddits.split(' ',4)
    for sredditnames in sredditraw:
        subreddit = reddit.subreddit(sredditnames)
        subreddit.subscribe()


