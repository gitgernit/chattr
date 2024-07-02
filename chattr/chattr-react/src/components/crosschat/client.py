__all__ = []

import asyncio

import aiortc

stun_servers = list(
    map(
        lambda x: aiortc.RTCIceServer('stun:' + x),
        [
            'stun1.l.google.com:19302',
            'stun2.l.google.com:19302',
        ],
    ),
)


def connected_handler(dc):
    print('Datachannel open! (connected)')
    dc.send('Hello, world!')


def message_handler(dc, message):
    print(f'Received: {message}')
    dc.send(message)


async def create_offer(pc: aiortc.RTCPeerConnection, room):
    dc = pc.createDataChannel(room, negotiated=True, id=0)
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)

    dc.on('open', lambda: connected_handler(dc))
    dc.on('message', lambda message: message_handler(dc, message))


async def accept_answer(pc: aiortc.RTCPeerConnection, sdp):
    await pc.setRemoteDescription(
        aiortc.RTCSessionDescription(type='answer', sdp=sdp),
    )


async def main():
    pc = aiortc.RTCPeerConnection(
        configuration=aiortc.RTCConfiguration(
            iceServers=stun_servers,
        ),
    )
    await create_offer(pc, 'ham')
    await asyncio.sleep(1)

    with open('offer.txt', 'w') as offer_txt:
        for line in pc.localDescription.sdp.split('\n'):
            offer_txt.write(line)

    print('offer written')

    await asyncio.sleep(20)

    with open('answer.txt', 'r') as answer_txt:
        sdp = ''.join(answer_txt.readlines())
        await accept_answer(pc, sdp)

    print('answer read')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.create_task(main())
    loop.run_forever()
