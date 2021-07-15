from tornado import ioloop, httpclient

i = 0

def handle_request(response):
    print(response.code)
    global i
    i -= 1
    if i == 0:
        ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()
for url in open('urls.txt'):
    i += 1
    http_client.fetch(url.strip(), handle_request, proxie_host=proxy[0], proxie_port=proxy[1], method='HEAD')
ioloop.IOLoop.instance().start()