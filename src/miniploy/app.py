import typer
from miniploy.commands import deploy, setup, run

app = typer.Typer(
    name="miniploy",
    help="One-stop AI-powered deployment to Render, Fly.io, Vercel, Railway, Netlify",
    add_completion=True,
    no_args_is_help=True,
)

app.add_typer(deploy.app, name="deploy", help="Analyze codebase and prepare deployment config")
app.add_typer(setup.app,  name="setup",  help="Configure selected platform (AI-assisted)")
app.add_typer(run.app,    name="run",    help="Deploy to the configured platform")


@app.callback()
def main_callback(
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
):
    """miniploy - the simplest way to ship your app"""
    if verbose:
        print("[DEBUG] Verbose mode enabled")
    # You can store global state here later (config, logger level, etc.)
