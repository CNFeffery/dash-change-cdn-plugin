import re
from dash import hooks
from typing import Literal


def setup_change_cdn_plugin(
    cdn_source: Literal["npmmirror", "jsdelivr", "fastly-jsdelivr"] = "npmmirror",
):
    """Setup the change cdn plugin

    Args:
        cdn_source (Literal["npmmirror", "jsdelivr", "fastly-jsdelivr"], optional): The source of CDN. Defaults to "npmmirror".
    """

    @hooks.index()
    def change_cdn(app_index: str):
        # Extract all static resource links pointing to unpkg CDN in app_index
        unpkg_scripts = re.findall(r'src="(https://unpkg\.com.*?)"', app_index)

        # Replace each with new CDN address
        for origin_src in unpkg_scripts:
            # Initialize new CDN address
            new_script = origin_src

            # Extract key information
            library_name, library_version, library_file = re.findall(
                "com/(.+)@(.+?)/(.+?)$", origin_src
            )[0]

            # Construct new CDN address for different types
            if cdn_source == "npmmirror":
                new_script = f"https://registry.npmmirror.com/{library_name}/{library_version}/files/{library_file}"
            elif cdn_source == "jsdelivr":
                new_script = f"https://cdn.jsdelivr.net/npm/{library_name}@{library_version}/{library_file}"
            elif cdn_source == "fastly-jsdelivr":
                new_script = f"https://fastly.jsdelivr.net/npm/{library_name}@{library_version}/{library_file}"

            # Perform replacement
            app_index = app_index.replace(origin_src, new_script)

        return app_index
