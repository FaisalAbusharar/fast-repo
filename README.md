# Fast Repo

**Fast Repo** is a lightweight Python package designed to quickly setup a git repository without any extra fluff like setting up remotes or anything.

## Features

- Fast and easy repository management
- Lightweight and dependency-free
- Designed for developers who want speed and simplicity

## Installation

Install via PyPI:

```zsh
pip install repoFast
```

or

```zsh
wget https://github.com/FaisalAbusharar/fast-repo/releases/download/v0.1.4-RPM/repofast-0.1.4-1.fc43.noarch.rpm
sudo dnf install ./repofast-0.1.4.1.fc43.noarch.rpm
```

### Dependencies

gh is needed for this to work, so install gh and setup the authentication properly.
[gh Setup Guide](https://cli.github.com/manual/gh_auth_setup-git)

## Usage

In terminal:

```bash
repoFast [-h] [--private] [--source SOURCE] [--remote REMOTE] repo_name
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

#### Starting With Developing Linux Commands
