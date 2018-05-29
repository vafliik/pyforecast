# -*- coding: utf-8 -*-
from typing import List

import requests

from forecast import Client, Project, Person, Assignment, Milestone, Role, UserConnection, Placeholder

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

    def get_project(self, project_id):
        r = requests.get("{}/projects/{}".format(self._base_url, project_id), headers=self._headers)
        data = r.json()['project']

        return Project.from_json(data)

    def get_clients(self):
        r = requests.get("{}/clients".format(self._base_url), headers=self._headers)
        data = r.json()['clients']

        return [Client.from_json(client) for client in data]

    def get_client(self, client_id):
        r = requests.get("{}/clients/{}".format(self._base_url, client_id), headers=self._headers)
        data = r.json()['client']

        return Project.from_json(data)

    def get_people(self):
        r = requests.get("{}/people".format(self._base_url), headers=self._headers)
        data = r.json()['people']

        return [Person.from_json(person) for person in data]

    def get_person(self, person_id):
        r = requests.get("{}/people/{}".format(self._base_url, person_id), headers=self._headers)
        data = r.json()['person']

        return Person.from_json(data)

    def get_assignments(self, start_date=None, end_date=None, state='active',
                        project_id=None, person_id=None, placeholder_id=None):
        params = {'state': state}

        if start_date:
            params['start_date'] = start_date
        if end_date:
            params['end_date'] = end_date
        if project_id:
            params['project_id'] = project_id
        if person_id:
            params['person_id'] = person_id
        if placeholder_id:
            params['placeholder_id'] = placeholder_id

        r = requests.get("{}/assignments".format(self._base_url), headers=self._headers, params=params)
        data = r.json()['assignments']

        return [Assignment.from_json(assignment) for assignment in data]

    def get_assignment(self, assignment_id: int) -> Assignment:
        r = requests.get("{}/assignments/{}".format(self._base_url, assignment_id), headers=self._headers)
        data = r.json()['assignment']

        return Assignment.from_json(data)

    def get_milestones(self, project_id: int = None) -> List[Milestone]:
        params = {}

        if project_id:
            params['project_id'] = project_id

        r = requests.get("{}/milestones".format(self._base_url), headers=self._headers, params=params)
        data = r.json()['milestones']

        return [Milestone.from_json(milestone) for milestone in data]

    def get_milestone(self, milestone_id: int) -> Milestone:
        r = requests.get("{}/milestones/{}".format(self._base_url, milestone_id), headers=self._headers)
        data = r.json()['milestone']

        return Milestone.from_json(data)

    def get_roles(self) -> List[Role]:

        r = requests.get("{}/roles".format(self._base_url), headers=self._headers)
        data = r.json()['roles']

        return [Role.from_json(role) for role in data]

    def get_role(self, role_id: int) -> Role:
        r = requests.get("{}/roles/{}".format(self._base_url, role_id), headers=self._headers)
        data = r.json()['role']

        return Role.from_json(data)

    def get_placeholders(self) -> List[Placeholder]:

        r = requests.get("{}/placeholders".format(self._base_url), headers=self._headers)
        data = r.json()['placeholders']

        return [Placeholder.from_json(placeholder) for placeholder in data]

    def get_placeholder(self, placeholder_id: int) -> Placeholder:
        r = requests.get("{}/placeholders/{}".format(self._base_url, placeholder_id), headers=self._headers)
        data = r.json()['placeholder']

        return Placeholder.from_json(data)

    def get_user_connections(self) -> List[UserConnection]:

        r = requests.get("{}/user_connections".format(self._base_url), headers=self._headers)
        data = r.json()['user_connections']

        return [UserConnection.from_json(connection) for connection in data]

    def get_user_connection(self, user_connection_id: int) -> UserConnection:
        raise NotImplementedError("This feature is not supported by Forecast App API yet")

    def whoami(self) -> Person:
        r = requests.get("{}/whoami".format(self._base_url), headers=self._headers)
        user_id = r.json()['current_user']['id']
        return self.get_person(person_id=user_id)
