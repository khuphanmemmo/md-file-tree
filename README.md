# md-file-tree inspired by [@michalbe](http://github.com/michalbe)

Generate markdown tree of all the files in a directory, recursively.

## How to use?

### Redirect the output to a file

```bash
$ python3 script.py > list.md
```

This generates the `list.md` file with:

```markdown
- 📂 **`md-file-tree`**
  - 📁 **`note`**
  - 📄 [`LICENSE`](LICENSE)
  - 📄 [`README.md`](README.md)
  - 📄 [`script.py`](script.py)
    - 📄 [`test-01.md`](note/test-01.md)
    - 📄 [`test-02.md`](note/test-02.md)
    - 📄 [`test-03.md`](note/test-03.md)
```

## Hidden files & directories

Please note that this script __skips__ all hidden files and directories (with `.`, like `.git` or `.gitignore`) &
 the contents of the `node_modules` directory.