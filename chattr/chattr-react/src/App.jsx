import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Header from './components/shared/header/Header.jsx';
import Footer from './components/shared/footer/Footer.jsx';
import Homepage from './components/homepage/Homepage.jsx';
import Webrtc from './components/webrtc/Webrtc.jsx'
import Aiortc from './components/aiortc/Aiortc.jsx'

function App() {
  return (
    <BrowserRouter>
      <Header/>
      <Routes>
        <Route path="" element={<Homepage />}/>
        <Route path="webrtc" element={<Webrtc />}/>
        <Route path="aiortc" element={<Aiortc />}/>
      </Routes>
      <Footer/>
    </BrowserRouter>
  );
}

export default App;