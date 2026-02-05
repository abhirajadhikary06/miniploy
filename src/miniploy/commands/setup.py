import typer

app = typer.Typer(help="Configure selected platform (AI-assisted)")

@app.command("setup")
def setup_command(
    platform: str = typer.Argument(..., help="Target platform: vercel | render | fly | railway | netlify"),
    project: str = typer.Option(".", "--project", "-p", help="Project path"),
):
    """Set up authentication + project on chosen platform"""
    supported = ["vercel", "render", "fly", "railway", "netlify"]
    if platform.lower() not in supported:
        typer.echo(f"Error: platform must be one of {', '.join(supported)}")
        raise typer.Exit(1)
    
    typer.echo(f"Setting up {platform} deployment...")
    typer.echo("→ Asking for API token / login (coming soon)")
    typer.echo("→ AI will help generate platform-specific config")
