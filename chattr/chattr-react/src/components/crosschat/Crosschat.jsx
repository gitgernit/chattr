import './Crosschat.css'
import {stunServers, createOffer, createAnswer, sendMessage} from './networking.js'

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
  let pseudo_dc = await createAnswer(pc, 'ham', sdpArea.value)

  dc = pseudo_dc ? pseudo_dc : dc

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
                  onClick={answerButton}>Answer
          </button>
        </div>
      </div>
      <div className="chat">
        <textarea className="chat-area" id="chat-area" readOnly
                  placeholder="Messages will appear there!"/>
        <input type="text"
               onKeyDown={(event) => sendMessage(event, dc)}
               id="message-input"/>
      </div>
    </div>
  )
}

export default Crosschat;
