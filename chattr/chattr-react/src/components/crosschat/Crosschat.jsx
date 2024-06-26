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
    </div>
  )
}

export default Crosschat;
