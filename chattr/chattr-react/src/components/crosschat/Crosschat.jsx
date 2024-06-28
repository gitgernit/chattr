import './Crosschat.css'

function Crosschat() {
  return (
    <div className="crosschat">
      <div className="controls">
        <textarea className="sdp-area" id="sdp-area"
                  placeholder="Paste \ copy SDP"/>
        <div className="sdp-buttons">
          <button>Offer</button>
          <button>Answer</button>
        </div>
      </div>
      <div className="chat">
        <textarea className="chat-area" readOnly/>
        <input type="text" id="message-input"/>
      </div>
    </div>
  )
}

export default Crosschat;
