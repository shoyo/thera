import praw,random
reddit = praw.Reddit(client_id='g1urkS6sO5LI7A',
                     client_secret='RSgUhmWgDHpuF1szYuS00lpbdPI',
                     user_agent='junction_test')


#possible subreddit r/mademesmile, r/happycrowds r/selfimprovement r/GetMotivated
list_subreddit = ['mademesmile','selfimprovement','GetMotivated']
rand_subreddit = random.choice(list_subreddit)

for submission in reddit.subreddit(rand_subreddit).hot(limit=10):
    post_id = submission.id
    post_title = submission.title
    #print(post_id,post_title)
    store = []
    for chara in post_title:
        if chara == ' ' :#or ']':
            store.append('_')
        else:
            store.append(chara)
    
    post_title = ''.join(store)
    post_title = post_title.replace('[','')
    post_title = post_title.replace(']','')
    post_title = post_title.lower()
    url = 'https://reddit.com/r/' + rand_subreddit + '/comments/' + post_id + '/' + post_title
    print(url)


#for submission in subreddit.stream.submissions():
#    try:
#        print(submission.title)
#    except Exception as e:
#        pass


#posts = []
#ml_subreddit = reddit.subreddit('MachineLearning')
#for post in ml_subreddit.hot(limit=10):
#    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
#posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
#print(posts)