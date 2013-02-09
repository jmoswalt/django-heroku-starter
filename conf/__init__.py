from os import environ, path

ENV_ROOT = path.abspath(path.join(path.dirname(__file__), ".."))


def env(e, d=None):
    """
    Helper method to populate settings from the environment.
    Allows passing a default value.
    """
    if e in environ:
        if environ[e].lower() == "false":
            return False
        elif environ[e].lower() == "true":
            return True
        return environ[e]
    else:
        return d


def load_env(separator, line):
    """
    This method parses a line using a separator to
    populate the local environment with a key/value pair.
    """
    env_key = line.rstrip().split(separator)[0].strip()
    env_value = line.rstrip().split(separator, 1)[1].strip()
    environ[env_key] = env_value

# Load the .env file into the os.environ for secure information
try:
    env_file = open(path.join(ENV_ROOT, '.env'), 'r')
except:
    # no .env file
    env_file = None

if env_file:
    for line in env_file.readlines():
        if line[0] != "#":
            if "=" in line:
                load_env("=", line)
            elif ":" in line:
                load_env(":", line)

    env_file.close()
