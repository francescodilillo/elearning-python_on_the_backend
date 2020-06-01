################################################################################
#
# Author: francescodilillo
# Purpose: Create web requests handler for get and post
# Last Edit Date: 31-05-2020
#
#
################################################################################

import tornado.web                  # it contains the handlers
import tornado.ioloop               # it contains the thread that will wait for results
import asyncio
import json
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())     # python-3.8.0a4 / Windows

class mainRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

class queryRequestHandler(tornado.web.RequestHandler):

    def get(self):
        fh = open("numbers.txt")
        numbers = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(numbers))

    def post(self):
        num = self.get_argument('num')
        fh = open("numbers.txt", "a")
        fh.write(f'{num}\n')
        fh.close()
        self.write(json.dumps({"message": "Number added successfully."}))



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", mainRequestHandler),
        (r"/list", queryRequestHandler)
    ])

port = 8882
app.listen(port)
print("Application is listening on port", port)
tornado.ioloop.IOLoop.current().start()
