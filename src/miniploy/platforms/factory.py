class PlatformHandler:
    def setup(self, config):
        raise NotImplementedError

    def deploy(self, config):
        raise NotImplementedError


def get_platform_handler(platform_name: str) -> PlatformHandler:
    # Placeholder - real version imports real classes
    name = platform_name.lower()
    if name == "vercel":
        return PlatformHandler()  # ← replace with VercelHandler()
    elif name == "render":
        return PlatformHandler()
    # etc.
    raise ValueError(f"Unknown platform: {platform_name}")
