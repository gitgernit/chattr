const stunServers = [
  'stun1.l.google.com:19302',
  'stun2.l.google.com:19302',
]

async function createOffer(pc, room) {
  let dc = pc.createDataChannel(room)
  let offer = await pc.createOffer()
  await pc.setLocalDescription(offer)

  return dc
}

async function createAnswer(pc, room, sdp) {
  if (pc.localDescription) {
    await pc.setRemoteDescription({type: 'answer', sdp: sdp})
  } else {
    let dc = pc.createDataChannel(room)
    await pc.setRemoteDescription({type: 'offer', sdp: sdp})
    let answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return dc
  }
}


export { stunServers, createOffer, createAnswer }
