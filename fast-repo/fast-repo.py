#!/usr/bin/env python3
import argparse
import subprocess
from rich import print
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(prog="Fast Repo", description="Quickly setup your repositories")
    parser.add_argument("repo_name", type=str)
    parser.add_argument("--public", '--verbose', action='store_false')
    parser.add_argument("--source", default=".")
    parser.add_argument("--remote", default="origin")
    args = parser.parse_args()


    visibility = "--private" if args.private else "--public"



    readme = Path(f"{args.source}/README.md")

    if not readme.exists() or readme.stat().st_size == 0:
        readme.write_text("This repository was setup using Fast-Repo\n")
        print("[bold green]Created README file[/bold green]")

    subprocess.run([f"git -C \"{args.source}\" init"],
                    shell=True, cwd=f"{args.source}",
                    stdout=subprocess.DEVNULL)
    print("[bold green]Initiated Git[/bold green]")



    subprocess.run(["git add ."],
                    shell=True, cwd=f"{args.source}",
                    stdout=subprocess.DEVNULL)
    print("[bold green]Added files[/bold green]")


    subprocess.run(["git commit -am \"Fast repo Init\""],
                    shell=True, cwd=f"{args.source}",
                    stdout=subprocess.DEVNULL)
    print("[bold green]Created a commit[/bold green]")



    result = subprocess.run(
    [
        "gh", "repo", "create",
        args.repo_name,
        visibility,
        "--source", args.source,
        "--remote", args.remote,
        "--push"
    ],
    check=True,
    text=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    cwd=args.source
)
    print(result.stdout)
    print(f"[bold red]Successfully created repository with source {args.source}[/bold red]")

if __name__ == "__main__":
    main()