import typer
from miniploy.ai.analyzer import analyze_project

app = typer.Typer(help="Analyze codebase and prepare deployment config")

@app.command("deploy")
def deploy_command(
    path: str = typer.Argument(".", help="Project directory (default: current)"),
    auto: bool = typer.Option(False, "--auto", "-a", help="Auto-approve AI suggestions"),
):
    """Scan project, detect framework, let AI suggest config"""
    typer.echo(f"Analyzing project at: {path}")
    
    result = analyze_project(path)
    
    typer.echo("\n[AI Analysis]")
    typer.echo(result.get("summary", "No summary available yet"))
    
    if auto:
        typer.echo("Auto mode → would save config now (not implemented)")
    else:
        typer.confirm("Looks good? (Y/n)", default=True)
