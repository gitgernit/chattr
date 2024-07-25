import { useState, useEffect } from 'react';
import { User } from './User.js';
import './Room.css';

function Room() {
  const [users, setUsers] = useState([new User('you')]);

  return (
    <div className="room">
      <div className="videos">
        <div className="videos-wrapper">
          {users.map((user) => (
            <div key={user.name} className="user-video">
              <video />
              <span className="video-username">
                {user.name}
              </span>
            </div>
          ))}
        </div>
      </div>
      <div className="chat">
      </div>
    </div>
  );
}

export default Room;