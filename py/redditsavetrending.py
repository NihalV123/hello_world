import praw
srno = 1;
reddit = praw.Reddit(client_id="F8Dhs9oLR3vhvw",client_secret="5znmTZsqKv7s5wQodVYH33FUxn4", user_agent="My_Agent")
for submission in reddit.subreddit('trendingsubreddits').hot(limit=2104):
    sreddits = submission.title.split(' ',4)[4]
    rtitle = submission.title.split(' ',4)[3]
    #print(rtitle)
    sredditraw = sreddits.split(' ',4)
    print(sredditraw)
    for sredditnames in sredditraw:
        f= open("url.txt","a+")
        formatted = "https://wwww.reddit.com"+sredditnames+"\n"
        f.write(formatted)
        print(formatted)
        f.close() 
    #print("-------")
    lines_seen = set() # holds lines already seen
with open("redditurl.txt", "w") as output_file:
	for each_line in open("url.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)