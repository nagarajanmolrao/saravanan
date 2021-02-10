from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from saravanan.models import Saravanan
from saravanan.serializers import SaravananSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def saravanan_list(request):
    # GET list of Saravanan, POST a new entry, Delete all Entries
    if request.method == 'GET':
        saravanan = Saravanan.objects.all()
        avName = request.GET.get('avName', None)
        if avName is not None:
            saravanan = saravanan.filter(avName_contains=avName)
        saravanan_serializer = SaravananSerializer(saravanan, many=True)
        return JsonResponse(saravanan_serializer.data, safe=False)
    elif request.method == 'POST':
        saravanan_data = JSONParser().parse(request)
        saravanan_serializer = SaravananSerializer(data=saravanan_data)
        if saravanan_serializer.is_valid():
            saravanan_serializer.save()
            return JsonResponse(saravanan_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(saravanan_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Saravanan.objects.all.delete()
        return JsonResponse({'message': '{} Entries were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def saravanan_detail(request, pk):
    # find tutorial by pk (id)
    try:
        saravanan = Saravanan.objects.get(pk=pk)
    except Saravanan.DoesNotExist:
        return JsonResponse({'message': 'The Entry does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        saravanan_serializer = SaravananSerializer(saravanan)
        return JsonResponse(saravanan_serializer.data)

    elif request.method == 'PUT':
        saravanan_data = JSONParser().parse(request)
        saravanan_serializer = SaravananSerializer(saravanan, data=saravanan_data)
        if saravanan_serializer.is_valid():
            saravanan_serializer.save()
            return JsonResponse(saravanan_serializer.data)
        return JsonResponse(saravanan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        saravanan.delete()
        return JsonResponse({'message': 'Entry was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def saravanan_list_activated(request):
    # GET all published tutorials
    saravanan = Saravanan.objects.filter(avActivated=False)

    if request.method == 'GET':
        saravanan_serializer = SaravananSerializer(saravanan, many=True)
        return JsonResponse(saravanan_serializer.data, safe=True)
