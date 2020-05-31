from instapv.bot import Bot

bot = Bot('USERNAME', 'PASSWORD')

bot.login() # Very important to login and activate other functions

if bot.is_logged_in:
    acc = bot.account.get_current_user()
    text = 'Logged in as {}'.format(bot.username)
    text += '\nName: {}'.format(acc.full_name)
    text += '\nID: {}'.format(acc.pk)
    print(text)
else:
    print('Invalid User/Password')
