from django.views.generic import TemplateView


class RoomView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_id'] = kwargs['room_id']
        print(context['room_id'])
        return context
