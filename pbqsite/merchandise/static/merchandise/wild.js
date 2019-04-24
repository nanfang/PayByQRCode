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
    product_id = data["product_id"];
    pay_from = data["pay_from"];
    deactivateModal("#modal-card-pay-" + product_id);
    activateModal("#modal-card-paid-" + product_id);
    $("#pay-from-" + product_id).text(data["pay_from"]);
    $("#product-count-" + product_id).text(data["product_count"]);
};

setTimeout(function(){
    paySocket.send("Hello from browser websocket");
}, 1000);
