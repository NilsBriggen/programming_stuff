// Connect to the WebSocket server
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });


// When the connection is established
wss.onopen = () => {
  // Send a message to the server
  wss.send('Hello from the client!');
};

// When a message is received from the server
wss.onmessage = (event) => {
  // Print the message to the page
  const message = document.createElement('p');
  message.innerText = event.data;
  document.body.appendChild(message);
};

// When the send button is clicked
document.getElementById('send-button').onclick = () => {
  // Get the message from the input field
  const message = document.getElementById('message').value;

  // Send the message to the server
  wss.send(message);

  // Clear the input field
  document.getElementById('message').value = '';
};
