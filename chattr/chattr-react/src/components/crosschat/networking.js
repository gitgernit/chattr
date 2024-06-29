const stunServers = [
  'stun.l.google.com:19302',
  'stun1.l.google.com:19302',
  'stun2.l.google.com:19302',
  'stun3.l.google.com:19302',
  'stun4.l.google.com:19302',
]

async function createOffer(pc, room) {
  let offer = await pc.createOffer()
  let dc = pc.createDataChannel(room)

  await pc.setLocalDescription(offer)

  return [offer, dc]
}

export { stunServers, createOffer }
