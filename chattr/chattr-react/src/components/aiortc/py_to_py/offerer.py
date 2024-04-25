import aiohttp.web
import aiohttp_cors
import aiortc
import asyncio
import json


async def connect():
    peer_connection = aiortc.RTCPeerConnection()
    peer_connection.on('iceconnectionstatechange', lambda: print(peer_connection.iceConnectionState))
    peer_connection.on('icecandidate', lambda: print('ice candidate'))
    data_channel = peer_connection.createDataChannel('test')

    offer = await peer_connection.createOffer()
    await peer_connection.setLocalDescription(offer)

    async with aiohttp.ClientSession() as session:
        response = await session.post(url=f"http://localhost:{port}/offer/",
                                      data={'sdp': offer.sdp, 'type': offer.type})
        response = await response.json()

    answer = aiortc.RTCSessionDescription(**response)
    await peer_connection.setRemoteDescription(answer)
    print(peer_connection.iceGatheringState)
    print(peer_connection.connectionState)


app = aiohttp.web.Application()
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
    port = int(input('Enter answerer port: '))
    asyncio.run(connect())
    aiohttp.web.run_app(app, host='localhost', port=8081)
