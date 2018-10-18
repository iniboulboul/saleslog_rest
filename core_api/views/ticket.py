from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from ..serializers.ticket import TicketSerializer

class TicketViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        super(TicketViewset, self).create(request, *args, **kwargs)
        return super(TicketViewset, self).list(request, *args, **kwargs)
