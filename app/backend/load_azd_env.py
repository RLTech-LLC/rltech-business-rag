import json
import logging
import os
import subprocess

from dotenv import load_dotenv

logger = logging.getLogger("scripts")


def load_azd_env():
    """Get path to current azd env file and load file using python-dotenv.

    If azd is not installed or not authenticated (e.g., running in CI with
    environment variables already set via AZURE_USE_CLI_CREDENTIAL=true), this
    function logs a warning and returns without modifying the environment.
    """
    result = subprocess.run("azd env list -o json", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        logger.warning(
            "azd env list failed (azd may not be installed or authenticated). "
            "Relying on environment variables already set in the current shell."
        )
        return
    env_json = json.loads(result.stdout)
    env_file_path = None
    for entry in env_json:
        if entry["IsDefault"]:
            env_file_path = entry["DotEnvPath"]
    if not env_file_path:
        raise Exception("No default azd env file found")
    loading_mode = os.getenv("LOADING_MODE_FOR_AZD_ENV_VARS") or "override"
    if loading_mode == "no-override":
        logger.info("Loading azd env from %s, but not overriding existing environment variables", env_file_path)
        load_dotenv(env_file_path, override=False)
    else:
        logger.info("Loading azd env from %s, which may override existing environment variables", env_file_path)
        load_dotenv(env_file_path, override=True)
