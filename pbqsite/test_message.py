import channels.layers

channel_layer = channels.layers.get_channel_layer()
from asgiref.sync import async_to_sync


async_to_sync(channel_layer.group_send)('PAYMENT_CHANNEL_GROUP',
                                  {
                                      'type': 'payment_message',
                                      'message': 'Hello Payment'
                                  }, )
print("sent")
