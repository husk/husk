# Husk

**Husk** is an implementation of the Cornell Note-taking System. A page is
composed of three areas including the **notes** area, the **cue** area and
the **summary** area.

The _notes_ area is the dominant area and intended represent a lecture
or some content as thoroughly as possible, but still concise.

The _cue_ area contains the reduced-down ideas derived from the notes.
This should include keywords, brief statements, and questions about the
notes.

The _summary_ area contains, in your own words, a summarization of the
notes and cue content.

The general flow of filling out the page includes:

1. Record
2. Reduce
3. Recite
4. Reflect
5. Review


## Features

- Interface that lays out the areas in the appropriate sizes
- All areas support [MultiMarkdown](http://en.wikipedia.org/wiki/MultiMarkdown) syntax
- Ability to switch between the various "R" modes
- Full-text search across all documents
- Tagging of documents for flat access as well as hierarchy representation
- Export notes into a PDF for offline access or to print

### Features for hackers

- Documents are stored in a flat file broken up by section, i.e.

```
Title: My First Note
Author: Byron Ruth
Date: July 14, 2012

# (title)...

# Notes

...

# Cue

...

# Summary

...
```

- The flat files are stored and versioned using [Git](http://git-scm.com/)
- You can clone your git repo, make changes and push the changes back. Changes
will show up in the Web UI


## Repo structure

Documents are broken up by the date they are created:

```
repo/
    2012/
        06/
            01/
                bio101-lecture-1.md
                ...
        07/
            14/
                cs212-lecture-3.md
                ...
```

Changes pushed back to the repository are validated prior to being merged to
ensure everything is correctly formatted.
