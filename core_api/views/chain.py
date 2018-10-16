from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.chain import ChainSerializer, StatusSerializer, ChatSerializer, \
                                MessageSerializer, RelationSerializer

from ..serializers.customer import CustomerSerializer
from ..serializers.ticket import TicketSerializer
from ..decorators import create_sub_model
from ..models import Customer, Ticket, Status, Chat, StatusType

import json

class ChainViewset(viewsets.ModelViewSet):
    serializer_class = ChainSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)


    def retrieve(self,request,pk=None):
        # Get chain
        chain = self.get_object()
        chain = ChainSerializer(chain)

        customer = Customer.objects.get(pk=int(chain.data['customer']))

        customer = CustomerSerializer(customer)

            # Get tickets
        tickets = []
        for item in json.loads(chain['tickets'].value):
            tickets.append(Ticket.objects.get(pk=item))
        tickets = TicketSerializer(tickets,many=True)

            # Get statuses
        statuses = []
        for item in json.loads(chain['statuses'].value):
            statuses.append(Status.objects.get(pk=item))
        statuses = StatusSerializer(statuses,many=True)

        chats = []
        for item in json.loads(chain['chats'].value):
            chats.append(Chat.objects.get(pk=item))
        chats = ChatSerializer(chats,many=True)

        return Response({'customer': customer.data,
                         'tickets': tickets.data,
                         'statuses': statuses.data,
                         'chats': chats.data
                        })

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = serializer_class.Meta.model.objects.all()

    @create_sub_model(RelationSerializer)
    def create(self, request, obj, *args, **kwargs):
        if obj != None:
            type , created = StatusType.objects.get_or_create(relation=obj.instance)
            request.POST['status_type'] = type.id
        del request.POST['relation.model']
        del request.POST['relation.model_id']
        return super(viewsets.ModelViewSet, self).create(request)

    def list(self, request):
        try:
            self.queryset = Status.objects.filter(status_type=request.GET['status_type'])
        except:
            pass
        return super(StatusViewSet, self).list(request)

class ChatsViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = serializer_class.Meta.model.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def list(self,request):
        return Response({'error':'403 FORBIDDEN'})
