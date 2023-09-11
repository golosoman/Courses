import pytest
from main import app
from app.work_with_posts.dao.posts_dao import PostsDAO
from app.work_with_posts.dao.comments_dao import CommentsDAO

@pytest.fixture()
def get_posts():
    posts = PostsDAO(app.config.get("POSTS_DATA_PATH"))
    return posts

@pytest.fixture()
def get_comments():
    comments = CommentsDAO(app.config.get("COMMENTS_DATA_PATH"))
    return comments

