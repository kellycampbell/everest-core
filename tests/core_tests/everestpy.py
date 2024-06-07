# SPDX-License-Identifier: Apache-2.0
# Copyright Pionix GmbH and Contributors to EVerest

import pytest

from everest.testing.core_utils.fixtures import *
from everest.testing.core_utils.everest_core import EverestCore
from everest.testing.core_utils.probe_module import ProbeModule

@pytest.mark.asyncio
@pytest.mark.everest_core_config('config-probe.yaml')
async def test_everestpy_01(everest_core: EverestCore):
    everest_core.start(standalone_module='probe')
    probe_module = ProbeModule(everest_core.get_runtime_session())
    with pytest.raises(Exception):
        probe_module.start()

@pytest.mark.asyncio
@pytest.mark.everest_core_config('config-probe.yaml')
async def test_everestpy_02(everest_core: EverestCore):
    everest_core.start(standalone_module='probe')
    probe_module = ProbeModule(everest_core.get_runtime_session())
    probe_module.implement_command('example', 'uses_something', lambda: True)
    probe_module.start()
