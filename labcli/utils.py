# Based on
# https://github.com/python-gitlab/python-gitlab/blob/master/gitlab/v4/cli.py
import gitlab


class JSONPrinter(object):
    def display(self, data, **kwargs):
        import json  # noqa

        print(json.dumps(data, indent=4))

    def display_list(self, data, fields, **kwargs):
        import json  # noqa

        print(json.dumps([get_dict(obj, fields) for obj in data], indent=4))


class YAMLPrinter(object):
    def display(self, d, **kwargs):
        import yaml  # noqa

        print(yaml.safe_dump(d, default_flow_style=False))

    def display_list(self, data, fields, **kwargs):
        import yaml  # noqa

        print(
            yaml.safe_dump(
                [get_dict(obj, fields) for obj in data], default_flow_style=False
            )
        )


PRINTERS = {"json": JSONPrinter, "yaml": YAMLPrinter}


def get_dict(obj, fields):
    if isinstance(obj, str):
        return obj

    if fields:
        return {k: v for k, v in obj.attributes.items() if k in fields}
    return obj.attributes


def print_stuff(data, output_printer, fields):
    printer = PRINTERS[output_printer]()

    if isinstance(data, dict):
        printer.display(data)
    elif isinstance(data, list):
        printer.display_list(data, fields)
    elif isinstance(data, gitlab.base.RESTObject):
        printer.display(get_dict(data, fields), obj=data)
    elif isinstance(data, str):
        print(data)
    elif hasattr(data, "decode"):
        print(data.decode())
