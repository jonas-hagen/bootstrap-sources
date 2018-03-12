import os


def scss_path():
    return os.path.join(root_path(), 'scss')


def js_path():
    return os.path.join(root_path(), 'js')


def root_path():
    return os.path.dirname(os.path.abspath(__file__))
