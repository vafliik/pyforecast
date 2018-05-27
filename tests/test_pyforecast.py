#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyforecast` package."""
import json

import pytest

from click.testing import CliRunner

import forecast
from forecast import Client, Person
from forecast import cli


def test_content():
    api_ = forecast.Api('test', 'test')

def test_client_from_json():
    json_ = json.loads(
        '{"id":503865,"name":"Salsita","harvest_id":2688091,"archived":false,'
        '"updated_at":"2017-06-13T15:14:46.193Z","updated_by_id":263476}')
    client = Client.from_json(json_)
    assert isinstance(client, Client)
    assert client.name == 'Salsita'

def test_person_from_json():
    json_ = json.loads(
        '{"id":263476,"first_name":"R. Bradley","last_name":"Byrd","email":"brad@salsitasoft.com",'
        '"login":"enabled","admin":true,"archived":false,"subscribed":true,'
        '"avatar_url":"https://avatars/RB.png","roles":["MGMT"],"updated_at":"2018-02-06T13:14:57.725Z",'
        '"updated_by_id":263476,"harvest_user_id":808603,"weekly_capacity":null,'
        '"working_days":{"monday":true,"tuesday":true},"color_blind":false}')
    person = Person.from_json(json_)
    assert isinstance(person, Person)
    assert person.first_name == 'R. Bradley'
    assert person.working_days['monday']


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pyforecast.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
