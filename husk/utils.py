import os


def parent_dir(target, path=None):
    if not path:
        path = os.getcwd()
    while True:
        if target in os.listdir(path):
            return path
        # No where else to go, break the loop
        if path == '/':
            return
        path = os.path.dirname(path)
