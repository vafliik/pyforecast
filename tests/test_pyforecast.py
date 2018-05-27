#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyforecast` package."""

import pytest

from click.testing import CliRunner

from forecast import api, Client
from forecast import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    api = forecast.Api('789164', '1341598.pt.nPJ_Sj-ZZOcV2ace4s184ih5QvqWxN1UYzwZxDVhXq0s8d_SEutk0WKnWWsGEEQy1qZgtq43Pu1VZM3tB6OsRw')
    client = api.get_clients()[0]
    assert isinstance(client, Client)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pyforecast.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
