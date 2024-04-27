import './Homepage.css';
import {useEffect, useState} from 'react';
import {ToastContainer, toast, Flip} from 'react-toastify';
import {useFormik} from 'formik';
import ReactModal from 'react-modal';
import axios from "axios";
import Typewriter from 'typewriter-effect';
import * as Yup from 'yup';
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

const validationSchema = Yup.object().shape({
  maxUsers: Yup.number()
    .min(1, '< 1')
    .max(99, '>= 100'),
  maxIdleTime: Yup.number()
    .min(1, '< 1')
    .max(10079, '>= 10080')
});


const copyLink = async () => {
  const textbox = document.getElementById('link-textbox');
  const theme = localStorage.getItem('theme')

  try {
    await navigator.clipboard.writeText(textbox.innerHTML);
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
      const max_users = localStorage.getItem('maxUsers')
      const max_idle_time = localStorage.getItem('maxIdleTime')
      const response = await axios.get(
        `${window.location.href}api/rooms/get_room`,
        {
          params: {
            max_users: max_users || 24,
            max_idle_time: max_idle_time || 1440,
          }
        }
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

  const formik = useFormik({
    initialValues: {
      maxUsers: localStorage.getItem('maxUsers'),
      maxIdleTime: localStorage.getItem('maxIdleTime'),
    },
    validationSchema: validationSchema,
    onSubmit: () => {
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
    },
  });

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
    if (formik.isValid) {
      formik.handleSubmit()
      setModalIsOpen(false);
    }
  };

  useEffect(() => {
    fetchRoomUrl();
  }, []);

  return (
    <>
      <div className="homepage">
        <div className="middle-wrapper">
          <div className="typewriter">
            <Typewriter
              options={{
                strings: [
                  'Instant rooms',
                  'No registration required',
                  'No history saved',
                ],
                delay: 100,
                autoStart: true,
                pauseFor: 5000,
                loop: true,
              }}
            />
          </div>
          <div className="link-generator">
          <span id="link-textbox"
                onClick={copyLink}/>
            <button id="link-settings" onClick={openModal}>
              <img src={cogsUrl} alt="Modal with room settings"
                   id="settings-img"/>
            </button>
          </div>
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
              <input
                type="number"
                className="number-input"
                placeholder="24"
                {...formik.getFieldProps('maxUsers')}
              />
              {formik.touched.maxUsers && formik.errors.maxUsers ? (
                <div className="error-message">{formik.errors.maxUsers}</div>
              ) : null}
            </div>
            <div className="max-idle-time">
              <span>Max idle time</span>
              <input
                type="number"
                className="number-input"
                placeholder="1440"
                {...formik.getFieldProps('maxIdleTime')}
              />
              {formik.touched.maxIdleTime && formik.errors.maxIdleTime ? (
                <div className="error-message">{formik.errors.maxIdleTime}</div>
              ) : null}
            </div>
          </div>
        </div>
      </ReactModal>
    </>
  )
}

export default Homepage
