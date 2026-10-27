# Third-Party Notices

The original code in this repository is licensed under the Apache License 2.0
(see [`LICENSE`](LICENSE)), copyright LimX Dynamics Technology Co., Ltd.

This repository also contains code that is derived from, or bundled from, the
third-party projects below. Those files keep their original copyright headers
and are distributed under the terms of their own licenses, reproduced here.

## Isaac Lab

- Project: <https://github.com/isaac-sim/IsaacLab> (version 2.0.0)
- License: BSD-3-Clause
- Files derived from Isaac Lab, identified by their
  `The Isaac Lab Project Developers` copyright header:
  - `scripts/list_envs.py`
  - `scripts/rsl_rl/cli_args.py`
  - `scripts/rsl_rl/play.py`
  - `scripts/rsl_rl/train.py`
  - `source/limx_rl_forge/limx_rl_forge/assets/config/HU_D04_01.py`
  - `source/limx_rl_forge/limx_rl_forge/tasks/locomotion/agents/rsl_rl_ppo_cfg.py`
  - `source/limx_rl_forge/limx_rl_forge/tasks/locomotion/mdp/curriculums.py`
  - `source/limx_rl_forge/limx_rl_forge/tasks/locomotion/terrain/rough.py`

```text
Copyright (c) 2022-2025, The Isaac Lab Project Developers.

All rights reserved.

SPDX-License-Identifier: BSD-3-Clause

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## RSL-RL

- Project: <https://github.com/leggedrobotics/rsl_rl> (version 2.3.2)
- License: BSD-3-Clause, full text in [`rsl_rl_lib/LICENSE`](rsl_rl_lib/LICENSE)
- Location: [`rsl_rl_lib/`](rsl_rl_lib)
- Modifications by LimX Dynamics: entropy-coefficient decay in
  `rsl_rl_lib/rsl_rl/runners/on_policy_runner.py`
  (`entropy_decay`, `entropy_decay_rate`, `entropy_decay_interval`,
  `entropy_decay_min`).
- `rsl_rl_lib/rsl_rl/modules/normalizer.py` additionally carries a
  `Copyright (c) 2020 Preferred Networks, Inc.` notice, retained as published
  upstream.
- Licenses of RSL-RL's own dependencies are in
  [`rsl_rl_lib/licenses/dependencies/`](rsl_rl_lib/licenses/dependencies).

## Robot description

The robot model is not part of this repository. It is downloaded separately
from [humanoid-description](https://github.com/limxdynamics/humanoid-description)
under that repository's license.
