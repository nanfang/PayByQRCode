var paySocket = new WebSocket(
        'ws://' + window.location.host +
        '/merchandise/payment/');

paySocket.onmessage = function(e){
    var data = JSON.parse(e.data);
    var message = data['message'];
    alert(message);
};

setTimeout(function(){
    paySocket.send("Hello from browser websocket");
}, 1000);
