# twerp
## osint tool to replicate another user's timeline

See what you target sees! This tool allows you to enter any non-private Twitter user as a target and replicate their timeline as your own private list. See who your target follows, visualized in a natural way where you can see the same tweets presented just as if you are were the target.

# setup
You will need to generate consumer and token keys through the [Twitter Developer Application Managerment console](https://apps.twitter.com) to gain access to the Twitter API. Once you have all of the read-write authorizations, create a file named `keys` local to `twerp.py`. In this file, enter the authorizations keys on new lines in this order, like so:

    cosumer-key
    consumer-secret
    token-key
    token-secret

You will also need to install the necessary python libraries. Do so by running `pip -r requirements.txt`.

# using
Use `twerp.py` as a command-line tool with the following syntax:

    twerp.py <your username> <target username>
    eg. $ python twerp.py aaronsdevera kennydurp_in

No '@' signs.

The twerp.py program will produce a slew of generation messages. Afterwards, a private list will appear on your twitter account named after your target, with its members comprised of everyone your target follows!

# API limits
[They're a thing](https://twittercommunity.com/t/cant-add-members-to-a-list-code-104/25824/5). Write permissions for adding members to a list are weird and aren't explicit in the documentation. There may be issues.