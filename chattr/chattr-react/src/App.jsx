import Webrtc from './components/webrtc/Webrtc.jsx'
import Room from './components/rooms/Room.jsx'
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Header from './components/shared/header/Header.jsx';
import Footer from './components/shared/footer/Footer.jsx';
import Homepage from './components/homepage/Homepage.jsx';
import Crosschat from './components/crosschat/Crosschat.jsx';

function App() {
  return (
    <BrowserRouter>
      <Header/>
      <Routes>
        <Route exact path="" element={<Homepage />}/>
        <Route path="rooms/:room_id/" element={<Room />}/>
        <Route path="webrtc" element={<Webrtc />}/>
        <Route path="crosschat" element={<Crosschat />}/>
      </Routes>
      <Footer/>
    </BrowserRouter>
  );
}
export default App;
