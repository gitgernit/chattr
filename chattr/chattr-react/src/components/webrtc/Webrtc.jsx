// COMPLETE SHIT! DONT PUSH TO DEV

import './Webrtc.css'

let localStream;
let remoteStream;
let peerConnection;
let dataChannel;

let stun = {
  iceServers: [
    {
      urls: [
        'stun:stun.l.google.com:19302'
      ]
    }
  ]
}

let init = async () => {
  localStream = await navigator.mediaDevices.getUserMedia(
    {
      video: true,
      audio: false,
    }
  )
  document.getElementById('user-1').srcObject = localStream
}

const activateChat = () => {
  document.querySelector('.offers').style.display = 'none';
  document.querySelector('.chat').style.display = 'flex';
}

const sendMessage = async () => {
  const msg = document.querySelector('#message-area').value
  dataChannel.send(msg)
  document.getElementById('chat-area').value += '\nYou: ' + msg
}

const setUpConnection = async () => {
  remoteStream = new MediaStream()
  document.getElementById('user-2').srcObject = remoteStream

  peerConnection = new RTCPeerConnection(stun)

  localStream.getTracks().forEach((track) => {
    peerConnection.addTrack(track, localStream)
  })
  peerConnection.ondatachannel = async (event) => {
    dataChannel = event.channel
    dataChannel.onmessage = async (event) => {
      document.getElementById('chat-area').value += '\nPeer 2: ' + event.data
    }
    activateChat()
  }
  peerConnection.ontrack = async (event) => {
    event.streams[0].getTracks().forEach((track) => {
      remoteStream.addTrack(track)
    })
  }
  peerConnection.onicecandidate = async (event) => {
    if (event.candidate) {
      document.getElementById('sdp-area').value = JSON.stringify(peerConnection.localDescription);
    }
  };
}

const generateOffer = async () => {
  await setUpConnection()
  dataChannel = peerConnection.createDataChannel('room-1')
  dataChannel.onopen = async () => {
    activateChat()
  }
  dataChannel.onmessage = async (event) => {
    document.getElementById('chat-area').value += '\nPeer 2: ' + event.data
  }
  let sdp_offer = await peerConnection.createOffer(
    {
      offerToReceiveVideo: true,
    }
  )
  await peerConnection.setLocalDescription(sdp_offer)

  document.getElementById('sdp-area').value = JSON.stringify(peerConnection.localDescription)
}

const acceptOffer = async () => {
  let sdp = JSON.parse(document.getElementById('sdp-area').value)

  if (sdp['type'] === 'offer') {
    await setUpConnection()
    await peerConnection.setRemoteDescription(sdp)
    peerConnection.createAnswer()
      .then((answer) => peerConnection.setLocalDescription(answer))
  } else {
    await acceptAnswer()
  }
}

const acceptAnswer = async () => {
  let answer = JSON.parse(document.getElementById('sdp-area').value)
  await peerConnection.setRemoteDescription(answer)
}

function Webrtc() {
  init()

  return (
    <div className="webrtc">
      <div className="videos">
        <video className="video-stream" id="user-1"
               autoPlay playsInline/>
        <video className="video-stream" id="user-2"
               autoPlay playsInline/>
      </div>
      <div className="offers">
        <textarea id="sdp-area" placeholder="SDP (offer \ answer)"></textarea>
        <div className="sdp-buttons">
          <button onClick={generateOffer}>Create offer</button>
          <button onClick={acceptOffer}>Answer offer</button>
        </div>
      </div>
      <div className="chat">
        <textarea id="chat-area" placeholder="Messages will be here" readOnly />
        <input type="text" id="message-area" placeholder="Type your message" />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  )
}

export default Webrtc
