=====
Usage
=====

To use PyForecast in a project::

    import forecast
    api = forecast.Api(account_id='account_id', authorization_token='authorization_token')

    for project in api.get_projects():
        print(project.name, project.id)

    person = api.get_person(42)
    print(person.first_name, person.last_name, person.email)
