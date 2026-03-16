#!/usr/bin/env python

import fsk

fsk.fetch.fetch_url(
    "https://spiftp.esac.esa.int/data/SPICE/HERA/kernels/mk/former_versions/hera_study_v000.tm",
    overwrite=True,
    description_method="name",
)
