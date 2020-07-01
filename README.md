# Instagram Private API.
# WARRNING: Don't use it now!!!

- An unofficial instagram private api.

### API
- Media
    - Edit
    - Delete
    - Like
    - UnLike
    - Save
    - UnSave
    - getComments
    - getCommentsReplais
    - deleteComment
    - getLikers
    - enableComments
    - disableComments
- User
    - getUserFeed
    - getSelfUserFeed
    - getInfoByName
    - FollowRequestApprove
    - FollowRequestIgnore
    - Follow
    - UnFollow
    - Block
    - UnBlock
    - getUserFollowers
    - getUserFollowing
    - getPendingFollowRequests
- Live
    - Create
    - Start
    - End
    - SaveLive
    - getPostLiveLikers
    - getLikesCount
    - getComments
    - enableComments
    - disableComments
    - getLiveInfo

## Requirements
```
$ sudo apt-get install libpq-dev
$ pip3 install -U setuptools
$ pip3 install -r requirements.txt
```

## Install Using pip
```
$ pip3 install instapvapi
```

## Manual Installation
```
$ git clone https://github.com/its0x4d/instagramapi-python
$ cd instagramapi-python
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

## Usage
```python
from instapv import Instagram

bot = Bot('USERNAME', 'PASSWORD')

bot.login() # Without calling login function the script will not work!

if bot.is_logged_in:
    print('Logged in successfuly!')
    print(bot._uid)
else:
    print('Invalid username/password')
```
Version: **0.0.6 Beta**
