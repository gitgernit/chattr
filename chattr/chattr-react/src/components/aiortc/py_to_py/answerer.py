import aiohttp.web
import aiohttp_cors
import json
import aiortc


async def offer_handler(request):
    peer_connection = aiortc.RTCPeerConnection(
    )
    peer_connection.on('iceconnectionstatechange', lambda: print(peer_connection.iceConnectionState))

    data = await request.post()
    data = dict(data)
    offer = aiortc.RTCSessionDescription(**data)

    await peer_connection.setRemoteDescription(offer)
    answer = await peer_connection.createAnswer()
    await peer_connection.setLocalDescription(answer)

    return aiohttp.web.json_response({'sdp': answer.sdp, 'type': answer.type})


app = aiohttp.web.Application()
app.router.add_post('/offer/', offer_handler)
ice_server = aiortc.RTCIceServer(urls='stun:stun.l.google.com:19302')

cors = aiohttp_cors.setup(
    app,
    defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    },
)

for route in list(app.router.routes()):
    cors.add(route)

if __name__ == '__main__':
    port = int(input('Enter port: '))
    aiohttp.web.run_app(app, host='localhost', port=port)
