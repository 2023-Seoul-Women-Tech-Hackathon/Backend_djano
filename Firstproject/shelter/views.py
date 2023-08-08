import requests
from shelter.models import AreaCode
from django.shortcuts import render ##
from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import renderers

# Create your views here.

@api_view(['GET'])
@renderer_classes([renderers.JSONRenderer])
def find_shelters_api(request):
    if request.method == 'GET':
        
        area_codes = AreaCode.objects.all()
        shelters_list=[]

        for area_code in area_codes:
            current_area_code = area_code.code
            
            #행정안전부 API 요청
            url = 'http://apis.data.go.kr/1741000/HeatWaveShelter2/getHeatWaveShelterList2'
            params ={'serviceKey' : '9sbRZvwvCxfN/4rChbm235uIHxeCO71K9PPFkAFEyTRA3roFDJrMqnCkL9iSnJDoawD8119dyG+bf8YqjCOKUA==', 
            'pageNo' : '1', 'numOfRows' : '10', 'type' : 'JSON', 'year' : '2023', 'areaCd' : current_area_code, 'equptype' : '001' }

            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()

        
                for shelter_data in data['HeatWaveShelter'][1]['row']:
                    restName = shelter_data['restname']
                    lat = shelter_data['la']
                    log = shelter_data['lo']
                    shelters_list.append({'la': lat, 'lo': log, 'restname': restName})
                
            except requests.exceptions.RequestException as e:
                return Response({'error': 'API request error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except KeyError as e:
                return Response({'error': f'Invalid API response: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
        return JsonResponse(shelters_list, safe=False, json_dumps_params={'ensure_ascii': False})