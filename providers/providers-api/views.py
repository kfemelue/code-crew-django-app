import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
import plotly
from .models import Clinician
from django.shortcuts import render
from rest_framework import generics
# from django.contrib.sites import requests


class ClinicianListGet(APIView):

    def get(self, request, *args, **kwargs):
        # URL of the external API
        external_api_url = 'https://data.cms.gov/provider-data/api/1/datastore/query/mj5m-pzi6/0?offset=0&count=true&results=true&schema=true&keys=true&format=json&rowIds=false'

        # Fetch data from the external API
        response = requests.get(external_api_url)
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from external API'}, status=status.HTTP_502_BAD_GATEWAY)

        data_json = response.json()
        data = json.loads(data_json).results
        print(data[0])

        # this dictionary will track the number of medicaid accepting clinicians in each city for data analysis
        frequency_dict = defaultdict(int)

        # this dictionary will map those clinicians to each city, to enable identifying the available clinicians
        location_map = defaultdict(list)

        # Iterate through the list and update the frequency dictionary
        for item in data:
            if item.ind_assgn == "Y":
                key = (item.citytown, item.state)
                frequency_dict[key] += 1
                location_map[key].append(item)

        frequency_dict = dict(frequency_dict)
        objects_dict = dict(location_map)

        """
        create X and Y variables to use with plotly
        The X variable will be  city_state_array: a list of strings "City, State"
        The Y variable will be frequency_array: the number of Clinicians accepting medicare
        in each city, state combination
        """
        frequency_array = list(frequency_dict.values())
        city_state_array = [f"{key[0]}, {key[1]}" for key in frequency_dict.keys()]

