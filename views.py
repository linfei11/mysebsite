import re
from django.http.response import FileResponse

from rest_framework import response, status
from rest_framework.generics import get_object_or_404
from .models import Attack
from rest_framework import routers, serializers, viewsets
from .serializers import AttackSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from django.db.models import Q
# ViewSets定义视图的行为。
def str2array(arra):
    array_len = len(arra)
    arra = arra[1:array_len-1]
    arra = arra.split(',')
    return arra
class AttackViewSet(viewsets.ModelViewSet):
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer

    @action(methods=['GET'],detail=False)
    def search1(self, request):
        print(request.query_params)
        st_time = request.GET.get('st_time', None)
        en_time = request.GET.get('en_time', None)

        #attacks = Attack.objects.filter(risk_level__exact=risk).filter(input_type__exact=in_type).\
        #filter(rule_type__contains=ru_type).filter(update_time__range=(st_time,en_time))
        if st_time and en_time:
            attacks = Attack.objects.filter(update_time__range=(st_time, en_time))
        else:
            risk = request.query_params['risk']
            risk = str2array(risk)

            in_type = request.GET.get('in_type', None)
            in_type = str2array(in_type)
            ru_type = request.GET.get('ru_type', None)
            ru_type = str2array(ru_type)
            temp = []
            for item in ru_type:
                temp.append(item.strip('"'))
            ru_type = temp
            print(ru_type)
            attacks = Attack.objects.filter(Q(risk_level__in=risk) & Q(input_type__in=in_type) & Q(rule_type__in=ru_type))
        serializer = self.get_serializer(instance=attacks, many=True)
        return Response(serializer.data)
    @action(methods=['GET'],detail=False)
    def search2(self, request):
        fuzzycontent = request.GET.get('content', None)
        #print('content:',fuzzycontent)
        attacks = Attack.objects.filter(content__icontains=fuzzycontent)
        serializer = self.get_serializer(instance=attacks, many=True)
        return Response(serializer.data)
    
    @action(methods=['GET'],detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        response = FileResponse(open(file_obj.pcap_path.path, 'rb'))
        return response

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(methods=['delete'],detail=False)
    def multiple_delete(self, request, *args, **kwargs):
        delete_id = request.query_params.get('deleteid', None)
        print('delete_id:',delete_id)
        if not delete_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for i in delete_id.strip('\"').split(','):
            get_object_or_404(Attack, pk=int(i)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
