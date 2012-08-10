# Husk

Husk is an API and CLI written in Python for the Cornell
Note-taking System.

- [Install](Install)
- [CLI](CLI)

## Install

```
# using pip
pip install husk

# using easy_install
easy_install husk
```

## CLI

### General Help

Husk command help:

```bash
usage: husk [-h] [-v] {init,add,move,remove,workon,info} ...

Husk is an API and CLI written in Python for the Cornell Note-taking System.

positional arguments:
  {init,add,move,remove,workon,info}

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

### Initialize Repository

```
usage: husk init [-h] [-d] [path]

Initialize a Husk repository in the current working directory (cwd) unless a
`path` is specified.

positional arguments:
  path            Path to Husk repository

optional arguments:
  -h, --help      show this help message and exit
  -d, --defaults  Add a copy of the Husk defaults to the repo control
                  directory.
```

The result will be the creation of a `.husk` directory in the
specified path.

### Add Note

```
usage: husk add [-h] [-r REPO] [-f] [path [path ...]]

Adds a note to the repository specified by it's `path`. If `path` is an
existing directory/note, pass `--force` to register it with the repository.
Existing files of the same name will not be overwritten.

positional arguments:
  path                  Paths to note directory

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Path to Husk repository
  -f, --force           Force an existing unregistered note to be added to the
                        repository
```

### Move a Note

```
usage: husk move [-h] [-r REPO] src dest

Moves an existing note to a new path.

positional arguments:
  src                   Source path to note that will be moved
  dest                  Destination path of the note

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Path to Husk repository
```

### Remove a Note

```
usage: husk remove [-h] [-r REPO] [-d] [path [path ...]]

Remove a note from the specified repo. By default note files are not deleted.

positional arguments:
  path                  Path to note directory

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Path to Husk repository
  -d, --delete          Delete note files from disk
```

### Workon a Note

```
usage: husk workon [-h] [-r REPO] path [files [files ...]]

Command to "work on" a note of files with the editor defined in your Husk
settings and falls back to what is set in the $EDITOR environment variable.

positional arguments:
  path                  Path to note directory
  files                 Filenames to be opened

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Path to Husk repository
```

### Repo Info

```
usage: husk info [-h] [-r REPO] [{notes} [{notes} ...]]

Shows various info about the repo.

positional arguments:
  {notes}               Specify which kinds of info to be presented

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Path to Husk repository
```
