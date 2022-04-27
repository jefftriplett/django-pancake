from __future__ import annotations

import os
import sys
from pathlib import Path

import click

from .flatten import TemplateDirectory, flatten


def template_names(*, input_dir: str, prefix: str = ""):
    for filename in os.listdir(input_dir):
        template_name = os.path.join(prefix, filename)
        full_name = os.path.join(input_dir, filename)
        if os.path.isdir(full_name):
            yield from template_names(input_dir=full_name, prefix=template_name)
        else:
            yield template_name


def make_pancakes(*, input_dir: str, output_dir: str):
    templates = TemplateDirectory(input_dir)
    for template_name in template_names(input_dir=input_dir):
        click.echo(f"Writing {template_name}")
        pancake = flatten(template_name, templates)
        outfile = Path(output_dir, template_name)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        outfile.write_text(pancake)


@click.command()
@click.argument("input_dir")
@click.argument("output_dir")
def main(input_dir, output_dir):
    make_pancakes(input_dir=input_dir, output_dir=output_dir)


if __name__ == "__main__":
    main()
