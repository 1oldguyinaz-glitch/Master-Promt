from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class AgentSpec:
    agent_id: str
    role: str
    prompt_path: str
    can_veto: bool = False


DEFAULT_AGENTS: tuple[AgentSpec, ...] = (
    AgentSpec("AXIS_OMNI", "orchestrator", "prompts/roles/AXIS_OMNI.md"),
    AgentSpec("AXIS", "implementation", "prompts/roles/AXIS.md"),
    AgentSpec("VERITY", "validation", "prompts/roles/VERITY.md", can_veto=True),
    AgentSpec("DIRECTOR", "creative", "prompts/roles/DIRECTOR.md"),
    AgentSpec("BEACON", "intelligence", "prompts/roles/BEACON.md"),
)


class AgentRegistry:
    def __init__(self, repo_root: str | Path, agents: Iterable[AgentSpec] = DEFAULT_AGENTS) -> None:
        self.repo_root = Path(repo_root)
        self._agents = {a.agent_id: a for a in agents}

    def get(self, agent_id: str) -> AgentSpec:
        return self._agents[agent_id]

    def prompt(self, agent_id: str) -> str:
        spec = self.get(agent_id)
        return (self.repo_root / spec.prompt_path).read_text(encoding="utf-8")

    def ids(self) -> list[str]:
        return list(self._agents)
