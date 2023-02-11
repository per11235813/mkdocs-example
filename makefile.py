
from pathlib import Path
import shutil
import sys
from subprocess import PIPE, CalledProcessError, Popen
import typer


top_dir = Path(".") / "my-docs"
docs_dir = top_dir / "docs"
site_dir = top_dir / "site"
examples_dir = docs_dir / "examples"
examples_output_dir = docs_dir / "examples-output"


app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command()
def run_examples():
    examples_output_dir.mkdir(exist_ok=True)

    for f in examples_dir.glob("*.py"):
        res_txt = run_cmd(f"python {f}", echo_cmd=True, echo_stdout=False)
        example_out_file = examples_output_dir / f"{f.name}.txt"
        example_out_file.write_text(res_txt)
    

@app.command()
def build():
    run_examples()

    for nb in docs_dir.glob("*.ipynb"):
        run_cmd(f"jupyter nbconvert {nb.name} --to markdown", echo_cmd=True, echo_stdout=False, cwd=docs_dir)

    run_cmd("mkdocs build", cwd=top_dir)


@app.command()
def serve():
    build()
    run_cmd("mkdocs serve", cwd=top_dir)


@app.command()
def clean():
    site_dir.exists() and shutil.rmtree(site_dir)
    examples_output_dir.exists() and shutil.rmtree(examples_output_dir)

    for nb in docs_dir.glob("*.ipynb"):
        nb.with_suffix(".md").unlink(missing_ok=True)


def run_cmd(cmd, echo_cmd=True, echo_stdout=True, cwd=None) -> str:
    echo_cmd and print(f"##\n## Running: {cmd}\n")
    res = []
    proc = Popen(cmd, stdout=PIPE, stderr=sys.stderr, shell=True, encoding=sys.getfilesystemencoding(), cwd=cwd)
    while proc.poll() is None:
        line = proc.stdout.readline()
        echo_stdout and print(line, end="")
        res.append(line)


    if proc.returncode != 0:
        raise CalledProcessError(proc.returncode, cmd)

    return "".join(res)


if __name__ == "__main__":
    app()