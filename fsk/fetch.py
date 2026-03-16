import functools
import os
import shutil
import sys
import tempfile
import urllib
from http.client import REQUEST_TIMEOUT
from pathlib import Path

import niquests
from tqdm import tqdm

TIMOUT_REQUEST = 10.0


def fetch_url(
    url: str,
    path: Path | str = None,
    timeout: float = REQUEST_TIMEOUT,
    overwrite: bool = False,
    auth: tuple[str, str] | None = None,
    description: str = None,
    description_method: str = None,
) -> None:
    """Fetch file online at URL and place it at PATH."""
    # Only download if the file does not exist locally.

    url_path = urllib.parse.urlparse(url).path
    url_parts = url_path.split("/")

    if path is None:
        path = Path(url_parts[-1])

    if type(path) is str:
        path = Path(path)

    FILE_EXISTS = path.is_file()
    if not overwrite and FILE_EXISTS:
        return

    # print(url)
    RESPONSE = niquests.get(
        url, stream=True, allow_redirects=True, timeout=timeout, auth=auth
    )

    # Raise for 4xx codes.
    if RESPONSE.status_code != 200:
        RESPONSE.raise_for_status()
        raise RuntimeError(
            f"Request to {url} returned status code {RESPONSE.status_code}"
        )

    # Create parents dir if not existing already.
    path.parent.mkdir(parents=True, exist_ok=True)

    # Loading bar customisation.

    if description is None:
        if description_method == "url_full":
            description = url_path
        elif description_method == "name":
            description = url_parts[-1]
        elif description_method == "path":
            description = path
        else:
            description = ""

    FILE_SIZE = int(RESPONSE.headers.get("content-length", 0))
    DESC_UNKNOWN_SIZE = " (Unknown total file size)" if FILE_SIZE == 0 else ""
    DESC = f"{description}{DESC_UNKNOWN_SIZE}"

    # Decompress if needed.
    RESPONSE.raw.read = functools.partial(RESPONSE.raw.read, decode_content=True)

    # Download to temporary path to ensure file has been downloaded entirely.
    with tempfile.NamedTemporaryFile(delete=False) as FILE:
        TEMPFILE_NAME = FILE.name
        # In case want to change bar format.
        # bar_format = (
        #     "{desc}: {percentage:3.0f}%|"
        #     "{bar:20}"
        #     "| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
        # )

        # Save to temporary file.
        with tqdm.wrapattr(
            RESPONSE.raw,
            "read",
            total=FILE_SIZE,
            desc=DESC,
            # bar_format=bar_format,
        ) as R_RAW:
            shutil.copyfileobj(R_RAW, FILE)

    # Once downloaded, move temporary path to final path.
    # print(TEMPFILE_NAME, path)
    shutil.copy(TEMPFILE_NAME, path)
    os.remove(TEMPFILE_NAME)
