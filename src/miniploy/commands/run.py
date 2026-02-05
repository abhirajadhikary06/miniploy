import typer

app = typer.Typer(help="Deploy to the configured platform")

@app.command("run")
def run_command(
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be deployed without doing it"),
):
    """Trigger the actual deployment"""
    if dry_run:
        typer.echo("[DRY RUN] Would push code and trigger deployment now...")
    else:
        typer.echo("Deploying... (implementation coming soon)")
