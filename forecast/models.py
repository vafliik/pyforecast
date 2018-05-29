class Model:

    def __init__(self, **kwargs):
        self.param_defaults = {}

    @classmethod
    def from_json(cls, data, **kwargs):
        """ Create a new instance based on a JSON dict. Any kwargs should be
        supplied by the inherited, calling class.

        Args:
            data: A JSON dict, as converted from the JSON in the Forecast API.

        """

        json_data = data.copy()
        if kwargs:
            for key, val in kwargs.items():
                json_data[key] = val

        c = cls(**json_data)
        c._json = data
        return c


class Client(Model):
    """A class representing the Client API structure. """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'name': None,
            'harvest_id': None,
            'archived': False,
            'updated_at': None,
            'updated_by_id': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Client(name={name})".format(
            name=self.name,
        )


class Project(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'name': None,
            'color': None,
            'code': None,
            'notes': None,
            'start_date': None,
            'end_date': None,
            'harvest_id': None,
            'archived': None,
            'updated_at': None,
            'updated_by_id': None,
            'client_id': None,
            'tags': []
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Project(name={name})".format(
            name=self.name,
        )


class Person(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'first_name': None,
            'last_name': None,
            'email': None,
            'login': None,
            'admin': False,
            'archived': False,
            'subscribed': True,
            'avatar_url': None,
            'roles': [],
            'updated_at': None,
            'updated_by_id': None,
            'harvest_user_id': None,
            'weekly_capacity': None,
            'working_days': {},
            'color_blind': False
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Person(name={first_name} {last_name}, email={email})".format(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )


class Assignment(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'start_date': None,
            'end_date': None,
            'allocation': None,
            'notes': None,
            'updated_at': None,
            'updated_by_id': None,
            'project_id': None,
            'person_id': None,
            'placeholder_id': None,
            'repeated_assignment_set_id': None,
            'active_on_days_off': False
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Assignment(start_date={start_date}, end_date={end_date}, project_id={pid})".format(
            start_date=self.start_date,
            end_date=self.end_date,
            pid=self.project_id,
        )


class Milestone(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'name': None,
            'date': None,
            'updated_at': None,
            'updated_by_id': None,
            'project_id': None}

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Milestone(name={name}, date={date}, project_id={pid})".format(
            name=self.name,
            date=self.date,
            pid=self.project_id,
        )


class UserConnection(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'person_id': None,
            'last_active_at': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "UserConnection(person_id={person_id}, last_active_at={date})".format(
            person_id=self.person_id,
            date=self.last_active_at,
        )


class Role(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'name': None,
            'placeholder_ids': [],
            'person_ids': [],
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Role(name={name})".format(
            name=self.name,
        )


class Placeholder(Model):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': None,
            'name': None,
            'archived': False,
            'roles': [],
            'updated_at': None,
            'updated_by_id': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Placeholder(name={name})".format(
            name=self.name,
        )
