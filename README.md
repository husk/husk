# Husk

Husk is an API and CLI written in Python for the Cornell
Note-taking System.

- [Install]
- [CLI]

## Install

```
# using pip
pip install husk

# using easy_install
easy_install husk
```

## CLI

### Terminology

- **repository** - A directory containing bundles
- **bundle** - A directory containing each component of a Cornell notes page
including the `notes`, `cues` and `summary` files.

### View Help

Husk command help:

```
husk -h
```

Husk subcommand help:

```
husk [command] -h
```

### Initialize Repository

Initializes a repository in the specified path.

```
husk init [PATH] [--add-config]
```

- `path` - Optional path for the repository to be created. Defaults
to the current working directory.
- `--add-config` or `-a` - Create a default config file in the
repository

The result will be the creation of a `.husk` directory in the
specified path.

### Add Bundle

Add a _bundle_ to the specified repo.

```
husk add PATH [--repo REPO]
```

- `path` - A path to a non-existent directory
- `--repo` or `-r` - Path to the Husk repo this bundle will be written to.
If ommitted, it is assumed you are somewhere in a repo.
