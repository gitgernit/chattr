import {activateChat} from './miscallenous.js'

const stunServers = [
  'stun1.l.google.com:19302',
  'stun2.l.google.com:19302',
]

async function createOffer(pc, room) {
  let dc = pc.createDataChannel(room, {negotiated: true, id: 0})
  let offer = await pc.createOffer()
  await pc.setLocalDescription(offer)

  dc.onopen = activateChat
  dc.onmessage = getMessage

  return dc
}

async function createAnswer(pc, room, sdp) {
  if (pc.localDescription) {
    await pc.setRemoteDescription({type: 'answer', sdp: sdp})
  } else {
    let dc = pc.createDataChannel(room, {negotiated: true, id: 0})
    await pc.setRemoteDescription({type: 'offer', sdp: sdp})
    let answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    dc.onopen = activateChat
    dc.onmessage = getMessage

    return dc
  }
}

function sendMessage(event, dc) {
  let messageInput = document.getElementById('message-input')
  let chatArea = document.getElementById('chat-area')

  if (event.key === 'Enter') {
    dc.send(messageInput.value)

    chatArea.value += 'you: ' + messageInput.value + '\n'
    messageInput.value = ''
  }
}

function getMessage(event) {
  let chatArea = document.getElementById('chat-area')
  chatArea.value += 'remote peer: ' + event.data + '\n'
}


export { stunServers, createOffer, createAnswer, sendMessage }
