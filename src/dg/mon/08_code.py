#!/usr/bin/python
'''file description ...'''

import redis

r = redis.Redis(host='localhost',port=6379,db=0)
r.set('guo','shuai')
print r.get('guo')

p = r.pipeline()
p.set('hello','redis').sadd('faz','baz').incr('num').execute()

r.set("visit:1237:totals",34634)
r.incr("visit:1237:totals")
r.get("visit:1237:totals")
	
r.hset('users:jdoe',  'name', "John Doe")
r.hset('users:jdoe', 'email', 'John@test.com')
r.hset('users:jdoe',  'phone', '1555313940')
r.hincrby('users:jdoe', 'visits', 1)
r.hgetall('users:jdoe')
r.hkeys('users:jdoe')

	