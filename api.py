import falcon.asgi

api = falcon.asgi.App(cors_enable=True)

class Server:
    async def on_get(self, request, response):
        responseText = "Hello World!"
        response.media = {"response": f'The Server says:{responseText}'}

api.add_route('/v1/server', Server())