from instapv.bot import Bot

bot = Bot('USERNAME', 'PASSWORD')

login_response = bot.login()
b = bot.user.get_user_following()
if login_response.two_factor_required:
    identifier = login_response.two_factor_info.two_factor_identifier
    code = input('Enter code: ')
    _ = bot.finish_two_factor_login(bot.username, bot.password, identifier, code)
    if _.status == "ok":
        print('Logged in')
    else:
        print(_.as_json)
else:
    print(login_response.as_json)