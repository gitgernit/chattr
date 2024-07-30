import { useEffect, useState } from 'react';
import { loadClientUser } from './userManagement.js';
import './Room.css';

function Room() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    return loadClientUser(setUsers);
  }, []);

  return (
    <div className="room">
      <div className="videos">
        <div className="videos-wrapper">
          {users.map((user) => (
            <div key={user.name} className="user-video">
              <video/>
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
