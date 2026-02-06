import click
from crate.scan import scan_folder
from crate.export import export_csv

@click.group()
def cli():
    pass

@cli.command()
@click.argument("path")
@click.option("--out", default="samples.csv")
def scan(path, out):
    rows = scan_folder(path)
    export_csv(rows, out)
    click.echo(f"Saved {len(rows)} samples to {out}")

if __name__ == "__main__":
    cli()
