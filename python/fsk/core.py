import os
from pathlib import Path

import spiceypy as spice

from .fetch import fetch_url
from .fsk import sum_as_string


def test_moi():
    print(sum_as_string(1, 3))
    
def fetch_metakernel(path_mk: Path, url_root: str, overwrite: bool = False):
    spice.kclear()
    spice.ldpool(path_mk)
    
    USER = os.environ.get("FSK_AUTH_USER")
    PASSWORD = os.environ.get("FSK_AUTH_PASSWORD")
    
    if USER is None or PASSWORD is None:
        AUTH = None 
    else:
        AUTH = (USER, PASSWORD)
    
    NUMBER_KERNELS_TO_LOAD, _ = spice.dtpool("KERNELS_TO_LOAD")
    VALUES_PATH = [Path(VALUE) for VALUE in spice.gcpool("PATH_VALUES", 0, 1, 80)]
    SYMBOLS_PATH = spice.gcpool("PATH_SYMBOLS", 0, 1, 80)
    LIST_KERNELS_TO_LOAD = spice.gcpool("KERNELS_TO_LOAD", 0, NUMBER_KERNELS_TO_LOAD, 200)

    # Create symbol/path dictionary and transform list of kernels string to path.
    MAP_SYMBOL_TO_PATH_ROOT = {
    SYMBOL: PATH for (SYMBOL, PATH) in zip(SYMBOLS_PATH, VALUES_PATH)
    }

    LIST_PATH_KERNELS_TO_LOAD = []

    for STR_KERNEL in LIST_KERNELS_TO_LOAD:
        for SYMBOL, PATH_ROOT_KERNEL in MAP_SYMBOL_TO_PATH_ROOT.items():
            STR_TO_REPLACE = f"${SYMBOL}/"
            if STR_TO_REPLACE in STR_KERNEL:
                PATH_REL_KERNEL = STR_KERNEL.removeprefix(STR_TO_REPLACE)
                LIST_PATH_KERNELS_TO_LOAD.append(PATH_REL_KERNEL)
                break

    # Download kernels.
    for PATH_KERNEL_REL in LIST_PATH_KERNELS_TO_LOAD:
        URL_FULL = f"{url_root}/{PATH_KERNEL_REL}"
        PATH_KERNEL = PATH_ROOT_KERNEL / PATH_KERNEL_REL

        fetch_url(
            URL_FULL,
            PATH_KERNEL,
            auth=AUTH,
            description=f"{PATH_KERNEL_REL}",
            overwrite=overwrite,
        )

    print("Finished.")