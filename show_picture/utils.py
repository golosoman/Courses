import os


def get_posts_on_request(key_post, data_from_base):
    posts = list()
    for post_info in data_from_base:
        if post_info.get('content').lower().find(key_post.lower()) != -1:
            if os.path.exists(post_info.get('pic')):
                posts.append([post_info, True])
            else:
                posts.append([post_info, False])
    return posts
