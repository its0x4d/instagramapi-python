from instapv.bot import Bot

bot = Bot('USERNAME', 'PASSWORD')
bot.login()

followers = []
next_max_id = None # next_max_id for pagination
user_id = bot.account_id # self user id

while 1:
    _response = bot.user.get_user_followers(user_id, next_max_id)
    for item in _response.users:
        followers.append(item)
    if not _response.big_list:
        break
    next_max_id = _response.next_max_id

print(followers)