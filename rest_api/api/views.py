from django.shortcuts import render

# Create your views here.
from .models import Branches, Banks
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BranchSerializer

from .my_pagination import MyLimitOffsetPagination
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class BankViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['ifsc','branch','city','district','address','state']
    filterset_fields =['ifsc']
    ordering_fields = ['ifsc']

def home(request):
     return render(request, 'index.html')


def search_ifsc(request):
    ifsc = request.GET.get('ifsc')
    payload = []
    if ifsc:
        bank_objs = Branches.objects.filter(ifsc__startswith=ifsc)
        
        for bank_obj in bank_objs:
            payload.append(bank_obj.ifsc)


    return JsonResponse({'status' : 200 , 'data' : payload})