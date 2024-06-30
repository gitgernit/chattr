import './Crosschat.css'
import {stunServers, createOffer, createAnswer} from './networking.js'

const rtcConfiguration = {
  iceServers: stunServers.map(server => ({urls: `stun:${server}`})),
};

let pc = new RTCPeerConnection(rtcConfiguration)
let dc

async function offerButton() {
  let sdpArea = document.getElementById('sdp-area')
  dc = await createOffer(pc, 'ham')

  pc.onicecandidate = (candidate) => {
    sdpArea.value = pc.localDescription.sdp
  }
}

async function answerButton() {
  let sdpArea = document.getElementById('sdp-area')
  dc = await createAnswer(pc, 'ham', sdpArea.value)

  pc.onicecandidate = (candidate) => {
    sdpArea.value = pc.localDescription.sdp
  }
}

function Crosschat() {
  return (
    <div className="crosschat">
      <div className="controls">
        <textarea className="sdp-area" id="sdp-area"
                  placeholder="Paste \ copy SDP"/>
        <div className="sdp-buttons">
          <button id="offer-button"
                  onClick={offerButton}>Offer
          </button>
          <button id="answer-button"
                  onClick={answerButton}>Answer</button>
        </div>
      </div>
      <div className="chat">
        <textarea className="chat-area" readOnly
                  placeholder="Messages will appear there!"/>
        <input type="text" id="message-input"/>
      </div>
    </div>
  )
}

export default Crosschat;
