################################################################################
#
# Author: francescodilillo
# Purpose: Backend code for image upload service
# Last Edit Date: 01-06-2020
#
#
################################################################################

import tornado.web                  # it contains the handlers
import tornado.ioloop               # it contains the thread that will wait for results
import asyncio
import json
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())     # python-3.8.0a4 / Windows

class uploadRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
            self.write(f"http://localhost:8080/img/{f.filename}")

if (__name__ == '__main__'):
    app = tornado.web.Application([

        (r'/', uploadRequestHandler),
        (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': "img"})


    ])

    app.listen(8080)
    print("App listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()