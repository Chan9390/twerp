########################################################
# TWERP.PY
#
# osint tool to replicate a twitter user's timeline and see what they see
# by Aaron DeVera @aaronsdevera
#
# Usage:
# twerp.py <your username> <target username>
# eg. $ python twerp.py aaronsdevera kennydurp_in
########################################################

# command line usage
import sys
self_user = sys.argv[1]
target_user = sys.argv[2]

# init twitter reqs
import twitter

# init twitter auth from keyfile
keys=[]
f = open('keys')
for each in f:
    if each[-1:] == '\n':
        keys.append(each[:-1])
    else:
        keys.append(each)

# activate api usage with keys
api = twitter.Api(consumer_key=keys[0],consumer_secret=keys[1],access_token_key=keys[2],access_token_secret=keys[3])

# create private list for timeline replication
api.CreateList(target_user+'-timeline','private')
print '[+] List created: %s-timeline' % target_user

# get a list of everyone a user follows
users_target_follows = api.GetFriendIDs(screen_name=target_user)
queued_users = users_target_follows
acquired_users = []

# create list on your account
api.CreateListsMember(slug=target_user+'-timeline',user_id=queued_users[0],owner_screen_name=self_user)

# enumerate the people a target user follows into private list
count = 1
while queued_users:
    for target_follower in queued_users:
        # add user attempt
        try:
            print '[+] [%s] Adding uid %s to private list %s' % (count,target_follower,target_user+'-timeline')
            api.CreateListsMember(slug=target_user+'-timeline',user_id=target_follower,owner_screen_name=self_user)
            acquired_users.append(target_follower)

        # exception handling for private users   
        except twitter.error.TwitterError:
            print '[-] [%s] Error adding uid %s to private list %s' % (count,target_follower,target_user+'-timeline')
        
        queued_users = queued_users[1:]
        count += 1