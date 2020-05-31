# Instagram Private API.

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
$ pip3 install colorama
$ pip3 install requests
$ pip3 install packaging
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

Version: **0.0.6 Beta**
