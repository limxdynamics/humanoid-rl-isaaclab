# Copyright (c) 2025, LimX Dynamics Technology Co., Ltd.
# SPDX-License-Identifier: Apache-2.0

"""Static checks of the Oli task configuration.

These tests parse the configuration files instead of importing them, so they
run without Isaac Sim, Isaac Lab or a GPU.
"""

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "source" / "limx_rl_forge" / "limx_rl_forge"
ENV_CFG = PKG / "tasks" / "locomotion" / "robots" / "oli" / "31dof" / "velocity_env_cfg.py"
ROBOT_CFG = PKG / "assets" / "config" / "HU_D04_01.py"


def _module_list(path: Path, name: str) -> list:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError(f"{name} not found in {path}")


def _init_joint_pos() -> dict:
    tree = ast.parse(ROBOT_CFG.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg == "joint_pos" and isinstance(node.value, ast.Dict):
            return ast.literal_eval(node.value)
    raise AssertionError("joint_pos not found in HU_D04_01.py")


def _actuator_dict(key: str) -> dict:
    tree = ast.parse(ROBOT_CFG.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg == key and isinstance(node.value, ast.Dict):
            return {ast.literal_eval(k): v for k, v in zip(node.value.keys, node.value.values)}
    raise AssertionError(f"{key} not found in HU_D04_01.py")


def test_policy_controls_31_unique_joints():
    joints = _module_list(ENV_CFG, "JOINT_NAMES")
    assert len(joints) == 31
    assert len(set(joints)) == 31


def test_joint_weights_match_joint_count():
    assert len(_module_list(ENV_CFG, "JOINT_WEIGHT")) == len(_module_list(ENV_CFG, "JOINT_NAMES"))


def test_init_pose_covers_exactly_the_policy_joints():
    assert set(_init_joint_pos()) == set(_module_list(ENV_CFG, "JOINT_NAMES"))


def test_every_policy_joint_has_actuator_limits():
    joints = _module_list(ENV_CFG, "JOINT_NAMES")
    for key in ("stiffness", "damping", "effort_limit", "velocity_limit", "armature"):
        patterns = list(_actuator_dict(key))
        for joint in joints:
            assert any(re.fullmatch(p, joint) for p in patterns), f"{joint} has no {key} entry"


def test_play_and_train_share_the_log_root():
    """play.py must look for checkpoints where train.py writes them."""

    def log_root(path: Path) -> str:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("log_root_path = os.path.join("):
                return line.strip()
        raise AssertionError(f"log_root_path not found in {path}")

    scripts = ROOT / "scripts" / "rsl_rl"
    assert log_root(scripts / "train.py") == log_root(scripts / "play.py")
