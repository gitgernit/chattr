let ws;

const establish_ws_connection = async (username) => {
  const roomName = new URL(window.location.href).pathname.split('/')[2];
  const wsUrl = 'ws://' + 'localhost:8000/ws/rooms/' + roomName + '?username=' + username;
  ws = new WebSocket(wsUrl);

  ws.onopen = () => {
    console.log('open');

    ws.onmessage = (values) => {
      let data = JSON.parse(values['data'])
      console.log(data)
      document.getElementById('chat-messages').innerHTML += '<span>' + data['username'] + ': ' + data['message'] + '</span>'
    }
  }
}

const sendMessage = () => {
  let message = document.getElementById('chat-input').value
  document.getElementById('chat-input').value = ''
  ws.send(JSON.stringify({'message': message}))
}

export {establish_ws_connection, sendMessage};
