#include <iostream>
#include <string>
#include <boost/asio.hpp>
#include <boost/array.hpp>

using namespace std;
using namespace boost::asio;

io_service service;
ip::udp::endpoint sender_endpoint;
ip::udp::socket socket(service);

void receive_message()
{
  boost::array<char, 1> buf;
  boost::system::error_code error;

  while (true)
  {
    size_t len = socket.receive_from(buffer(buf), sender_endpoint, 0, error);

    if (error && error != error::message_size)
      throw boost::system::system_error(error);

    cout << buf.data() << endl;
  }
}

void send_message(const string& message)
{
  socket.send_to(buffer(message), sender_endpoint);
}

int main()
{
  cout << "Enter your name: ";
  string name;
  getline(cin, name);

  socket.open(ip::udp::v4());

  // Listen for messages on any available IP address and port 10000
  socket.bind(ip::udp::endpoint(ip::udp::v4(), 10000));

  cout << "Enter the IP address of the peer: ";
  string ip_address;
  getline(cin, ip_address);

  // Set the sender endpoint to the specified IP address and port 10000
  sender_endpoint = ip::udp::endpoint(ip::address::from_string(ip_address), 10000);

  // Start listening for messages in a separate thread
  thread receive_thread(receive_message);

  while (true)
  {
    string message;
    getline(cin, message);

    // Prepend the sender's name to the message
    message = name + ": " + message;

    send_message(message);
  }

  return 0;
}
