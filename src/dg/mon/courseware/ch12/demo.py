#!\urs\bin\env python
#encoding:utf-8

import web
        
urls = (
    '/(.*)', 'hello'
)


app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
			web.input() #get
			web.data()  ##post
        return '<html><head><title>demo</title><style>h1{color:#0f0}</style></head><body><h1 style="font-size:100px;">Hello, ' + name + '!</h1></body></html>'


if __name__ == "__main__":
    app.run()

