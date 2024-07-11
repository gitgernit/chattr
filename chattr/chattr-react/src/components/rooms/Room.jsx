import './Room.css'

function Room() {
  return (
    <div className="room">
      <div className="videos">
        <div className="videos-wrapper">
          <div className="user-video">
            <video/>
            <span className="video-username">
              undefined
            </span>
          </div>
          <div className="user-video">
            <video/>
            <span className="video-username">
              undefined
            </span>
          </div>
          <div className="user-video">
            <video/>
            <span className="video-username">
              undefined
            </span>
          </div>
        </div>
      </div>
      <div className="chat">
      </div>
    </div>
  )
}

export default Room
