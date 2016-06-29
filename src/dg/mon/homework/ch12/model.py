#!\urs\bin\env python
#encoding:utf-8

import web
import datetime
#数据库连接
db = web.database(dbn = 'mysql', db = 'test', user = 'root', pw = 'changeit!')
#获取所有文章
def get_posts():
    return db.select('blog', order = 'id DESC')

#获取文章内容
def get_post(id):
    try:
        return db.select('blog', where = 'id=$id', vars = locals())[0]
    except IndexError:
        return None
#新建文章
def new_post(title, text):
    db.insert('blog',
        title = title,
        content = text,
        posted_on = datetime.datetime.utcnow())
#删除文章
def del_post(id):
    db.delete('blog', where = 'id = $id', vars = locals())

#修改文章
def update_post(id, title, text):
    db.update('blog',
        where = 'id = $id',
        vars = locals(),
        title = title,
        content = text)

# 取得文章的评论
def get_comments_by_blog(blog_id):
    return db.select('comment', where = 'blog_id=$blog_id', vars = locals(), order = 'id DESC')

# 新加入评论
def new_comment(title, text, blog_id):
    db.insert('comment',
        blog_id = blog_id,
        title = title,
        content = text,
        posted_on = datetime.datetime.utcnow())
