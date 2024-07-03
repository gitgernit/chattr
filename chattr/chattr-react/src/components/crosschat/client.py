__all__ = []

import asyncio
import logging
import pathlib

import aiortc

logging.basicConfig(level=logging.INFO)

stun_servers = [
    aiortc.RTCIceServer('stun:' + url)
    for url in [
        'stun1.l.google.com:19302',
        'stun2.l.google.com:19302',
    ]
]

OFFER_DESTINATION = 'offer.txt'
ANSWER_DESTINATION = 'answer.txt'


def connected_handler(dc):
    logging.info('Datachannel open! (connected)')
    dc.send('Hello, world!')
    logging.debug('Sent initial message to datachannel')


def message_handler(dc, message):
    logging.info(f'Received: {message}')
    dc.send(message)
    logging.debug(f'Echoed {message} to datachannel')


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

    with pathlib.Path(OFFER_DESTINATION).open('w') as offer_file:
        for line in pc.localDescription.sdp.split('\n'):
            offer_file.write(line)

    logging.info(f'Offer written to {OFFER_DESTINATION}')
    await asyncio.sleep(0.1)  # to prevent logging.info to be outputted after input
    input(f'Press enter when answer is in {ANSWER_DESTINATION}')

    with pathlib.Path(ANSWER_DESTINATION).open('r') as answer_file:
        sdp = answer_file.read()
        await accept_answer(pc, sdp)

    logging.debug('Answer read')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.create_task(main())
    loop.run_forever()
