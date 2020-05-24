################################################################################
#
# Author: francescodilillo
# Purpose: Create web requests handler
# Last Edit Date: 24-05-2020
#
#
################################################################################

import tornado.web                  # it contains the handlers
import tornado.ioloop               # it contains the thread that will wait for results
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())     # python-3.8.0a4 / Windows


class basicRequestHandler(tornado.web.RequestHandler):
    LOOPER = 0

    def get(self):
        self.LOOPER += 1
        message = "Hello visitor #" + str(self.LOOPER) + " this is a python command executed by the backend"
        self.write(message)

class listRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animal", listRequestHandler)
    ])

port = 8882
app.listen(port)
print("Application is listening on port", port)
tornado.ioloop.IOLoop.current().start()
