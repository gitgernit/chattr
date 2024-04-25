// COMPLETE SHIT! DONT PUSH TO DEV

import axios from 'axios';
import './Aiortc.css';

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


function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

const connect = async () => {
  peerConnection = new RTCPeerConnection(stun)
  dataChannel = peerConnection.createDataChannel('test')

  let offer = await peerConnection.createOffer({offerToReceiveVideo: true})
  await peerConnection.setLocalDescription(offer)

  let answer = await axios.post('http://localhost:8081/connect/',
    {offer: peerConnection.localDescription})
}

const receive = async () => {
  peerConnection = new RTCPeerConnection(stun)
  peerConnection.ondatachannel = async (event) => {
    console.log('on data channel')
  }

  await peerConnection.setRemoteDescription(document.getElementById('offer-area').value)
}

const ping = () => {
  console.log(peerConnection.connectionState)
}

function Aiortc() {
  return (
    <div className="aiortc">
      <div className="connection-establisher">
        <button id="connect-button" onClick={connect}>Connect</button>
        <button onClick={ping}>Ping</button>
      </div>
      <textarea id="offer-area" />
      <button onClick={receive}>receive</button>
      <div className="chat">
        <textarea id="chat-area" placeholder="Messages will be here" readOnly/>
        <input type="text" id="message-area" placeholder="Type your message"/>
        <button onClick={null}>Send</button>
      </div>
    </div>
  )
}

export default Aiortc
