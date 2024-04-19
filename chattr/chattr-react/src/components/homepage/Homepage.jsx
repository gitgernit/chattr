import './Homepage.css';
import {useState} from 'react';
import ReactModal from "react-modal";
import {ToastContainer, toast, Flip} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css'

const toastConfig = {
  position: "top-left",
  autoClose: 2000,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  transition: Flip,
  className: 'notification',
}

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

ReactModal.setAppElement('#root')

function Homepage() {
  const [modalIsOpen, setModalOpen] = useState(false)

  return (
    <>
      <div className="homepage">
        <div className="link-generator">
          <input type="text" id="link-textbox"
                 onClick={copyLink} readOnly/>
          <button id="link-settings">
            <img src="src/assets/cogs.svg" alt="Modal with room settings"
                 id="settings-img"/>
          </button>
          <ReactModal/>
        </div>
        <ToastContainer/>
      </div>
    </>
  )
}

export default Homepage
