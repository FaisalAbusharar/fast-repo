import argparse
import subprocess
from rich import print
from pathlib import Path
# print("[bold green]Example Text[/bold green]")

visbility = ""

parser = argparse.ArgumentParser(prog="Fast Repo", description="Quickly setup your repositories")
parser.add_argument("repo_name", type=str)
parser.add_argument("--public", '--verbose', action='store_false')
parser.add_argument("--source", default=".")
parser.add_argument("--remote", default="origin")
args = parser.parse_args()
print(args.repo_name)
print(args.public)
print(args.source)
print(args.remote)


if args.public != True: visbility = "--private"
else: visbility="--public"



readme = Path("README.md")

if not readme.exists() or readme.stat().st_size == 0:
    readme.write_text("This repository was setup using Fast-Repo\n")
subprocess.run(["git add ."], shell=True)
subprocess.run(["git commit -am \"Fast repo Init\""], shell=True)


result = subprocess.run(
    ["gh", "repo", "create", args.repo_name, visbility, "--source" + args.source, "--source" + args.remote, "--push"],
    check=True,
    capture_output=True,
    text=True
)

print(result.stdout)