import './Homepage.css';
import {useEffect, useState} from 'react';
import {ToastContainer, toast, Flip} from 'react-toastify';
import ReactModal from 'react-modal';
import axios from "axios";
import 'react-toastify/dist/ReactToastify.css';
import cogsUrl from '/src/assets/cogs.svg';
import closeButtonUrl from '/src/assets/close-button.svg';

const toastConfig = {
  position: "top-left",
  autoClose: 2000,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  transition: Flip,
  className: 'notification',
}

const modalStyle = {
  overlay: {
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
};

const copyLink = async () => {
  const textbox = document.getElementById('link-textbox');
  const theme = localStorage.getItem('theme')

  try {
    await navigator.clipboard.writeText(textbox.value);
    toast.success('Link saved to clipboard', {
      ...toastConfig,
      theme: theme,
    });
  } catch (error) {
    toast.error('Couldnt save link to clipboard', {
      ...toastConfig,
      theme: theme,
    });
  }
}

const fetchRoomUrl = async () => {
    try {
      const response = await axios.get(
        `${window.location.href}api/homepage/get_room`,
        {}
      );
      document.getElementById('link-textbox').innerHTML = response.data['room_id'];
    } catch (error) {
      const theme = localStorage.getItem('theme')

      toast.error('Couldnt fetch room URl', {
        ...toastConfig,
        theme: theme,
      })
    }
  }
;

ReactModal.setAppElement('#root')

function Homepage() {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => {
    setModalIsOpen(true);
  };

  const afterOpenModal = () => {
    const maxUsersInput = document.querySelector('.max-users .number-input');
    const maxIdleTimeInput = document.querySelector('.max-idle-time .number-input');

    const storedMaxUsers = localStorage.getItem('maxUsers');
    const storedMaxIdleTime = localStorage.getItem('maxIdleTime');

    maxUsersInput.value = storedMaxUsers ? storedMaxUsers : ''
    maxIdleTimeInput.value = storedMaxIdleTime ? storedMaxIdleTime : ''
  }

  const closeModal = () => {
    setModalIsOpen(false);

    const maxUsersInput = document.querySelector('.max-users .number-input');
    const maxIdleTimeInput = document.querySelector('.max-idle-time .number-input');

    const maxUsers = maxUsersInput.value
    const maxIdleTime = maxIdleTimeInput.value

    const storedMaxUsers = localStorage.getItem('maxUsers');
    const storedMaxIdleTime = localStorage.getItem('maxIdleTime');

    if (maxUsers !== storedMaxUsers || maxIdleTime !== storedMaxIdleTime) {
      localStorage.setItem('maxUsers', maxUsers);
      localStorage.setItem('maxIdleTime', maxIdleTime);

      fetchRoomUrl()
    }
  };

    useEffect(() => {
      fetchRoomUrl();
    }, []);

    return (
      <>
        <div className="homepage">
          <div className="link-generator">
          <span id="link-textbox"
                onClick={copyLink}/>
            <button id="link-settings" onClick={openModal}>
              <img src={cogsUrl} alt="Modal with room settings"
                   id="settings-img"/>
            </button>
          </div>
          <ToastContainer/>
        </div>
        <ReactModal isOpen={modalIsOpen} onAfterOpen={afterOpenModal}
                    onRequestClose={closeModal}
                    className="settings-modal" style={modalStyle}
                    closeTimeoutMS={200}>
          <h2>Room Settings</h2>
          <input type="image" alt="Close modal button"
                 src={closeButtonUrl}
                 id="close-button" onClick={closeModal}/>
          <div className="settings-inputs">
            <div className="inputs-wrapper">
              <div className="max-users">
                <span>Max users</span>
                <input type="number" className="number-input"
                       placeholder="24"/>
              </div>
              <div className="max-idle-time">
                <span>Max idle time</span>
                <input type="number" className="number-input"
                       placeholder="10800"/>
              </div>
            </div>
          </div>
        </ReactModal>
      </>
    )
  }

  export default Homepage
