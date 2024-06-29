import './Crosschat.css'
import {stunServers, createOffer} from './networking.js'

const rtcConfiguration = {
  iceServers: stunServers.map(server => ({urls: `stun:${server}`}))
};

let pc = new RTCPeerConnection(rtcConfiguration)

async function offerButton() {
  let sdpArea = document.getElementById('sdp-area')
  let [offer, dc] = await createOffer(pc, 'ham')

  sdpArea.textContent = offer.sdp
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
          <button id="answer-button">Answer</button>
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
