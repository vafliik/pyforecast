# -*- coding: utf-8 -*-
import requests

from forecast import Client, Project, Person

"""Main module."""


class Api:

    def __init__(self, account_id, auth_token, base_url=None):

        self._account_id = account_id
        self._auth_token = auth_token
        if base_url is None:
            self._base_url = "https://api.forecastapp.com"

        self._headers = {
            'Forecast-Account-ID': self._account_id,
            'Authorization': 'Bearer {}'.format(self._auth_token),
            'User-Agent': 'Forecast Harvest Python API',
        }

    def get_projects(self):
        r = requests.get("{}/projects".format(self._base_url), headers=self._headers)
        data = r.json()['projects']

        return [Project.from_json(project) for project in data]

    def get_clients(self):
        r = requests.get("{}/clients".format(self._base_url), headers=self._headers)
        data = r.json()['clients']

        return [Client.from_json(client) for client in data]

    def get_people(self):
        r = requests.get("{}/people".format(self._base_url), headers=self._headers)
        data = r.json()['people']

        return [Person.from_json(person) for person in data]

    def get_person(self, person_id):
        r = requests.get("{}/people/{}".format(self._base_url, person_id), headers=self._headers)
        data = r.json()['person']

        return Person.from_json(data)
