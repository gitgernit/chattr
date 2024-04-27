import {useEffect, useState} from 'react';
import {useFormik} from 'formik';
import ReactModal from 'react-modal';
import * as Yup from 'yup';
import './Room.css';
import {establish_ws_connection, sendMessage} from './networking.jsx'
import sendMsgUrl from '/src/assets/send-msg.svg';


const modalStyle = {
  overlay: {
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
};

const validationSchema = Yup.object().shape({
  username: Yup.string()
    .matches(/^[a-zA-Z!_\-.\s]+$/, 'Username can only contain Latin characters and special characters like !, _, -, and .')
    .trim('No leading or trailing spaces allowed')
    .required('Username is required')
    .test(
      'isUsernameAvailable',
      'Username is already taken',
      async function (value) {
        // return await check_name_availability(value);
        return true;
      }
    )
    .strict(true)
});

function Room() {
  const formik = useFormik({
    initialValues: {
      username: '',
    },
    validationSchema: validationSchema,
    validateOnChange: false,
    validateOnBlur: true,
    validateOnMount: true,
    onSubmit: (values) => {
      let username = values.username
      establish_ws_connection(username)
    },
  });

  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => {
    setModalIsOpen(true);
  };

  const afterOpenModal = () => {
  };

  const closeModal = () => {
    if (formik.isValid) {
      formik.handleSubmit();
      setModalIsOpen(false);
    }
  };

  useEffect(() => {
    openModal();
  }, []);

  return (
    <div className="room">
      <ReactModal
        isOpen={modalIsOpen}
        onAfterOpen={afterOpenModal}
        onRequestClose={closeModal}
        className="username-modal"
        style={modalStyle}
        closeTimeoutMS={200}
        shouldCloseOnOverlayClick={false}
        shouldCloseOnEsc={false}
      >
        <span>Enter your username</span>
        <div className="input-wrapper">
          <input type="text" placeholder="username" id="username-input"
                 {...formik.getFieldProps('username')} />
          {formik.touched.username && formik.errors.username && (
            <div className="error-message">{formik.errors.username}</div>
          )}
          <button type="submit" onClick={closeModal} id="submit-username">Submit</button>
        </div>
      </ReactModal>
      {/*<div className="videos">*/}
      {/*  <div className="tracks">*/}
      {/*  </div>*/}
      {/*  <div className="video-inputs">*/}
      {/*    <h1>выключить микрофон, видео</h1>*/}
      {/*  </div>*/}
      {/*</div>*/}
      <div className="chat">
        <div className="messages" id="chat-messages">
        </div>
        <div className="chat-inputs">
          <input type="text" id="chat-input" />
          <img src={sendMsgUrl} alt="send message" onClick={sendMessage} id="send-message"/>
        </div>
      </div>
    </div>
  );
}

export default Room;