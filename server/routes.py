# -*- coding: utf-8 -*-
import MySQLdb
from app import *
from helpers import *
import model

@app.errorhandler(400)
def bad_request(error):
    return result_invalid(error.description)

@app.errorhandler(404)
def not_found(error):
    return result_not_found(error.response)

### Common
@app.route('/db/api/status/', methods=['GET'])
def status():
    response = model.status()
    return result(response)

@app.route('/db/api/clear/', methods=['POST'])
def clear():
    res = model.clear()

    if res:
        return result("OK")
    else:
        return result_unknown("Couldn't clear data")


### User
@app.route('/db/api/user/create/', methods=['POST'])
def user_create():
    udata = get_request_json()

    res = model.user_create(udata)

    if res:
        udata = model.user_data_short(udata.get('email'))
        return result(udata)
    else:
        return result_user_exists("User %s already exists" % udata.get('email'))

@app.route('/db/api/user/details/', methods=['GET'])
def user_details():
    email = get_request_arg('user')

    res = model.user_data(email)
    if res is None:
        return result_not_found("User %s doesn't exist" % email)

    return result(res)

@app.route('/db/api/user/follow/', methods=['POST'])
def user_follow():
    data = get_request_json()

    follower = data.get('follower')
    followee = data.get('followee')

    if not model.user_exists(follower):
        return result_not_found("User %s doesn't exist" % follower)

    if follower == followee:
        return result_invalid_semantic("User %s cannot follow himself" % follower)

    if not model.user_exists(followee):
        return result_not_found("User %s doesn't exist" % followee)

    if not model.user_follows(follower, followee):
        res = model.user_follow(follower, followee)

        if res:
            udata = model.user_data(follower)
            return result(udata)
        else:
            return result_unknown("Couldn't follow %s by %s" % (followee, follower))
    else:
        return result_unknown("User %s already follows %s" % (follower, followee))

@app.route('/db/api/user/listFollowers/', methods=['GET'])
def user_list_followers():
    email = get_request_arg('user')
    limit = get_request_arg('limit', 0)
    since_id = get_request_arg('since_id')
    order = get_request_arg('order', 'desc')

    if not model.user_exists(email):
        return result_not_found("User %s doesn't exist" % email)

    uemails = model.user_followers(email, limit=limit, order=order, since_id=since_id)

    res = []
    if len(uemails) > 0:
        res = model.users_data(uemails)

    return result(res)

@app.route('/db/api/user/listFollowing/', methods=['GET'])
def user_list_following():
    email = get_request_arg('user')
    limit = get_request_arg('limit', 0)
    since_id = get_request_arg('since_id')
    order = get_request_arg('order', 'desc')

    if not model.user_exists(email):
        return result_not_found("User %s doesn't exist" % email)

    uemails = model.user_following(email, limit=limit, order=order, since_id=since_id)

    res = []
    if len(uemails) > 0:
        res = model.users_data(uemails)

    return result(res)

@app.route('/db/api/user/listPosts/', methods=['GET'])
def user_list_posts():
    # TODO:
    return result({})

@app.route('/db/api/user/unfollow/', methods=['POST'])
def user_unfollow():
    data = get_request_json()

    follower = data.get('follower')
    followee = data.get('followee')

    if not model.user_exists(follower):
        return result_not_found("User %s doesn't exist" % follower)

    if not model.user_exists(followee):
        return result_not_found("User %s doesn't exist" % followee)

    if model.user_follows(follower, followee):
        res = model.user_unfollow(follower, followee)

        if res:
            udata = model.user_data(follower)
            return result(udata)
        else:
            return result_unknown("Couldn't unfollow %s by %s" % (followee, follower))
    else:
        return result_unknown("User %s doesn't follow %s" % (follower, followee))

@app.route('/db/api/user/updateProfile/', methods=['POST'])
def user_update_profile():
    # TODO:
    return result({})



### Forum
@app.route('/db/api/forum/create/', methods=['POST'])
def forum_create():
    # TODO:
    return result({})

@app.route('/db/api/forum/details/', methods=['GET'])
def forum_details():
    # TODO:
    return result({})

@app.route('/db/api/forum/listPosts/', methods=['GET'])
def forum_list_posts():
    # TODO:
    return result({})

@app.route('/db/api/forum/listThreads/', methods=['GET'])
def forum_list_threads():
    # TODO:
    return result({})

@app.route('/db/api/forum/listUsers/', methods=['GET'])
def forum_list_users():
    # TODO:
    return result({})



### Thread
@app.route('/db/api/thread/close/', methods=['POST'])
def thread_close():
    # TODO:
    return result({})

@app.route('/db/api/thread/create/', methods=['POST'])
def thread_create():
    # TODO:
    return result({})

@app.route('/db/api/thread/details/', methods=['GET'])
def thread_details():
    # TODO:
    return result({})

@app.route('/db/api/thread/list/', methods=['GET'])
def thread_list():
    # TODO:
    return result({})

@app.route('/db/api/thread/listPosts/', methods=['GET'])
def thread_list_posts():
    # TODO:
    return result({})

@app.route('/db/api/thread/open/', methods=['POST'])
def thread_open():
    # TODO:
    return result({})

@app.route('/db/api/thread/remove/', methods=['POST'])
def thread_remove():
    # TODO:
    return result({})

@app.route('/db/api/thread/restore/', methods=['POST'])
def thread_restore():
    # TODO:
    return result({})

@app.route('/db/api/thread/subscribe/', methods=['POST'])
def thread_subscribe():
    # TODO:
    return result({})

@app.route('/db/api/thread/unsubscribe/', methods=['POST'])
def thread_unsubscribe():
    # TODO:
    return result({})

@app.route('/db/api/thread/update/', methods=['POST'])
def thread_update():
    # TODO:
    return result({})

@app.route('/db/api/thread/vote/', methods=['POST'])
def thread_vote():
    # TODO:
    return result({})



### Post
@app.route('/db/api/post/create/', methods=['POST'])
def post_create():
    # TODO:
    return result({})

@app.route('/db/api/post/details/', methods=['GET'])
def post_details():
    # TODO:
    return result({})

@app.route('/db/api/post/list/', methods=['GET'])
def post_list():
    # TODO:
    return result({})

@app.route('/db/api/post/remove/', methods=['POST'])
def post_remove():
    # TODO:
    return result({})

@app.route('/db/api/post/restore/', methods=['POST'])
def post_restore():
    # TODO:
    return result({})

@app.route('/db/api/post/update/', methods=['POST'])
def post_update():
    # TODO:
    return result({})

@app.route('/db/api/post/vote/', methods=['POST'])
def post_vote():
    # TODO:
    return result({})
