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
        <Route exact path="crosschat" element={<Crosschat />}/>
      </Routes>
      <Footer/>
    </BrowserRouter>
  );
}

export default App;
