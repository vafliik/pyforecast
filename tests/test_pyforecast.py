#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyforecast` package."""
import json

import pytest

from click.testing import CliRunner

import forecast
from forecast import Client, Person, Assignment, Milestone
from forecast import cli


def test_content():
    api_ = forecast.Api('test', 'test')


def test_client_from_json():
    json_ = json.loads(
        '{"id":123,"name":"Wayne Enterprises","harvest_id":321,"archived":false,'
        '"updated_at":"2017-06-13T15:14:46.193Z","updated_by_id":4242}')
    client = Client.from_json(json_)
    assert isinstance(client, Client)
    assert client.name == 'Wayne Enterprises'


def test_person_from_json():
    json_ = json.loads(
        '{"id":1,"first_name":"Bruce","last_name":"Wayne","email":"bruce@wayne.enterprises",'
        '"login":"enabled","admin":true,"archived":false,"subscribed":true,'
        '"avatar_url":"https://wayne.enterprises/bw.png","roles":["MGMT", "Research", "Dark Knight"],'
        '"updated_at":"2018-02-06T13:14:57.725Z",'
        '"updated_by_id":1,"harvest_user_id":1,"weekly_capacity":null,'
        '"working_days":{"monday":true,"tuesday":true},"color_blind":false}')
    person = Person.from_json(json_)
    assert isinstance(person, Person)
    assert person.first_name == 'Bruce'
    assert person.working_days['monday']
    assert person.roles == ["MGMT", "Research", "Dark Knight"]

def test_assignment_from_json():
    json_ = json.loads(
        '{"id": 1, "start_date": "2018-06-04", "end_date": "2018-06-08", "allocation": 10800, "notes": null,'
        '"updated_at": "2018-05-27T08:48:20.529Z", "updated_by_id": 2, "project_id": 42, "person_id": 1,'
        '"placeholder_id": null, "repeated_assignment_set_id": null, "active_on_days_off": false}')
    assignment = Assignment.from_json(json_)
    assert isinstance(assignment, Assignment)
    assert assignment.id == 1
    assert assignment.person_id == 1
    assert assignment.project_id == 42

def test_milestone_from_json():
    json_ = json.loads(
        '{"id": 333,"name": "Autopilot Finished","date": "2017-06-23","updated_at": "2017-06-22T13:01:16.067Z",'
        '"updated_by_id": 3,"project_id": 42}')
    milestone = Milestone.from_json(json_)
    assert isinstance(milestone, Milestone)
    assert milestone.id == 333
    assert milestone.name == "Autopilot Finished"
    assert milestone.project_id == 42


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pyforecast.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
