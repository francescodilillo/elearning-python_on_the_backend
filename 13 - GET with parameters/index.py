################################################################################
#
# Author: francescodilillo
# Purpose: Create web requests handler
# Last Edit Date: 26-05-2020
#
#
################################################################################

import tornado.web                  # it contains the handlers
import tornado.ioloop               # it contains the thread that will wait for results
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())     # python-3.8.0a4 / Windows

class queryRequestHandler(tornado.web.RequestHandler):

    def get(self):
        num = self.get_argument("n")
        if num.isdigit():
            r = "odd" if int(num)%2 else "even"
            self.write(f"{num} is {r}")
        else:
            self.write(f"{num} is not a valid integer")

class resourceRequestHandler(tornado.web.RequestHandler):

    def get(self, sname, cid):
        self.write(f"Welcome {sname} to course {cid}")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/isEven", queryRequestHandler),                   # example: localhost:8882/isEven?n=2
         (r"/students/([a-z]+)/([0-9]+)", resourceRequestHandler)   #example: localhost:8882/students/francesco/77
    ])

port = 8882
app.listen(port)
print("Application is listening on port", port)
tornado.ioloop.IOLoop.current().start()
