var deactivateModal = function(modalId) {
    var target = $(modalId);
    if (target.hasClass("is-active")) {
        $(modalId).removeClass("is-active");
    }

}

var activateModal = function(modalId) {
    var target = $(modalId);
    if (!target.hasClass("is-active")) {
        target.addClass("is-active");
    }
}


var paySocket = new WebSocket(
        'ws://' + window.location.host +
        '/merchandise/payment/');

paySocket.onmessage = function(e){
    var data = JSON.parse(e.data);
    var message = data['message'];
//    alert(message);
    // get from message
    product_id = 2;
    deactivateModal("#modal-card-pay-" + product_id);
    activateModal("#modal-card-paid-" + product_id);
};

setTimeout(function(){
    paySocket.send("Hello from browser websocket");
}, 1000);
