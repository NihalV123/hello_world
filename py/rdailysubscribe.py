allarr = {}
remarr={}
reverse_d={}
val  = 'hi'
for tr100 in open("redditurl.txt", "r"):  #trending 1000 reddits
    tr100 = tr100.replace(',', '')
    tr100 = tr100.replace('https://wwww.reddit.com/r/', '')
    key = str(tr100)
    key = key.replace('\n', '')
    allarr[key] = val
print(allarr)
print(len(allarr))

for currsub in open("currentsub.txt", "r"):
    currsub = currsub.replace('Subreddit(display_name=', '') #current subscribbed reddits
    currsub = currsub.replace('\'', '').replace(')', '').replace(')]', '').replace('[(', '').replace(']', '').replace('[', '')
    key = str(currsub)
    key = key.replace(' \n', '')
    key = key.replace(' ', '')
    remarr[key] = val
print(remarr)
print(len(remarr))

for vals in allarr:
    key = str(vals)
    reverse_d[key] = val
print(len(reverse_d))

for vals in remarr:
    element = reverse_d.pop(vals,'apple')
print(reverse_d)

for vals in reverse_d:
    key = str(vals)
    f= open("newreddit.txt","a+")
    f.write(vals+"\n")
    f.close() 
print("done")
 

# import random
# import webbrowser
# import praw

# reddit = praw.Reddit(client_id="f4QT47zgSpuueA",
#                      client_secret="Cr_qLwp-0OHDBdSxnilAdO_hChA",
#                      password="QwErTyUi12345!!",
#                      user_agent="Nihalv123",
#                      username="Nihalv123")

# for submission in reddit.subreddit('trendingsubreddits').hot(limit=1):
#     sreddits = submission.title.split(' ',4)[4]
#     rtitle = submission.title.split(' ',4)[3]
#     sredditraw = sreddits.split(' ',4)
#     for sredditnames in sredditraw:
#         sredditnames = sredditnames.replace('/r/', '')
#         sredditnames = sredditnames.replace(',', '')
#         subreddit = reddit.subreddit(sredditnames)
#         print(subreddit)
#         subreddit.subscribe()