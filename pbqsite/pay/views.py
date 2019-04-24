from django.shortcuts import render
from django.views import View
import channels.layers
from asgiref.sync import async_to_sync


class PayView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.channel_layer = channels.layers.get_channel_layer()

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})

        return render(request, 'pay/pay_form.html', {})

    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')
        async_to_sync(self.channel_layer.group_send)('PAYMENT_CHANNEL_GROUP',
                                                {
                                                    'type': 'payment_message',
                                                    'message': 'Hello Payment'
                                                }, )

        return render(request, 'pay/pay_result.html', {})