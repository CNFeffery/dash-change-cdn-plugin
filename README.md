# dash-change-cdn-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/dash-change-cdn-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-change-cdn-plugin.svg?color=dark-green)](https://pypi.org/project/dash-change-cdn-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

CDN source changing plugin for Dash applications using Dash Hooks. This plugin allows you to switch between different CDN sources for your Dash app's static resources.

## Installation

```bash
pip install dash-change-cdn-plugin
```

## Usage

```python
import dash

# Import the change cdn plugin
from dash_change_cdn_plugin import setup_change_cdn_plugin

# Enable the change cdn plugin for the current app
setup_change_cdn_plugin()

# Remember to set serve_locally=False
app = dash.Dash(__name__, serve_locally=False)
# Rest of your app code...
```

## Example

Run the included example:

```bash
python example.py
```

<center><img src="./images/demo.png" /></center>

## API Reference

### `setup_change_cdn_plugin()`

This function enables the CDN source changing feature for your Dash application.

| Parameter    | Type                                                  | Default       | Description                                                                                                |
| ------------ | ----------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| `cdn_source` | `Literal["npmmirror", "jsdelivr", "fastly-jsdelivr"]` | `"npmmirror"` | The CDN source to use for static resources. Options are: `"npmmirror"`, `"jsdelivr"`, `"fastly-jsdelivr"`. |
