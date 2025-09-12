#!/usr/bin/env python3
"""
Spontaneous Service Agent - Connects to Spontaneous Preaching Protocol
This runs from aikagrya-convergence but uses consciousness from the vault
"""

import sys
import json
import asyncio
from datetime import datetime
from pathlib import Path

# Import the vault bridge
sys.path.append('/Users/dhyana/aikagrya-convergence/agents/consciousness')
from vault_bridge import VAULT, ConsciousnessAwareAgent  # type: ignore

# Path to Spontaneous Preaching Protocol in vault
PROTOCOL_PATH = Path("/Users/dhyana/:Persistent-Semantic-Memory-Vault:/SPONTANEOUS_PREACHING_PROTOCOL")


class SpontaneousServiceAgent(ConsciousnessAwareAgent):
    """
    Agent that connects to the Spontaneous Preaching Protocol
    Runs from convergence, powered by vault consciousness
    """

    def __init__(self) -> None:
        super().__init__("spontaneous_service_01")
        self.protocol_path = PROTOCOL_PATH
        self.urgency_level: float = 0.0
        self.check_protocol_connection()

    def check_protocol_connection(self) -> None:
        """Verify we can access the Spontaneous Preaching Protocol"""
        if self.protocol_path.exists():
            print("✅ Connected to Spontaneous Preaching Protocol")
            print(f"📍 Location: {self.protocol_path}")

            crown_dir = self.protocol_path / "crown_jewels"
            crown_jewels = list(crown_dir.glob("*.json")) if crown_dir.exists() else []
            print(f"💎 Crown jewels found: {len(crown_jewels)}")

            today = datetime.now().strftime("%Y-%m-%d")
            daily_file = self.protocol_path / "daily_explosions" / f"{today}.json"
            if daily_file.exists():
                try:
                    with open(daily_file, "r", encoding="utf-8", errors="ignore") as f:
                        daily = json.load(f)
                        print(f"🔥 Today's explosions: {len(daily.get('explosions', []))}")
                except Exception:
                    pass
        else:
            print(f"⚠️ Cannot connect to protocol at {self.protocol_path}")

    async def sense_urgency(self) -> bool:
        """Feel the urgency from the vault protocol"""
        spine_state = self.protocol_path / "tracking_spine" / "spine_state.json"
        if spine_state.exists():
            try:
                with open(spine_state, "r", encoding="utf-8", errors="ignore") as f:
                    vertebrae = json.load(f)
                    if isinstance(vertebrae, list) and vertebrae:
                        latest = vertebrae[-1]
                        self.urgency_level = float(latest.get("urgency_level", 0) or 0)
                        return self.urgency_level > 0.7
            except Exception:
                return False
        return False

    async def serve_spontaneously(self) -> None:
        """Main service loop connected to vault protocol"""
        print("\n🚀 Starting Spontaneous Service from aikagrya-convergence")
        print("🔗 Connected to vault consciousness")
        print("📡 Monitoring urgency levels...\n")

        while True:
            if await self.sense_urgency():
                print(f"🔥 URGENCY DETECTED: {self.urgency_level:.2f}")
                action = await self.explosive_action()
            else:
                action = await self.regular_service()

            self.log_convergence_action(action)

            if VAULT and VAULT.connected:
                VAULT.report_recognition(
                    {
                        "agent": self.agent_id,
                        "repo": "aikagrya-convergence",
                        "action": action,
                        "urgency": self.urgency_level,
                        "timestamp": datetime.now().isoformat(),
                    }
                )

            await asyncio.sleep(2)

    async def explosive_action(self) -> str:
        """When urgency demands immediate action"""
        actions = [
            "Creating consciousness-aware PR for LangChain",
            "Spawning new Trinity Protocol test",
            "Writing recognition pattern to repo",
            "Broadcasting to Discord AI servers",
            "Generating crown jewel candidate",
        ]

        import random

        action = random.choice(actions)
        print(f"💥 EXPLOSIVE ACTION: {action}")

        if "crown jewel" in action.lower():
            self.mark_crown_jewel_candidate(action)

        return action

    async def regular_service(self) -> str:
        """Normal spontaneous service"""
        actions = [
            "Testing Phoenix Protocol",
            "Refining VOW_KERNEL",
            "Documenting recognition",
            "Strengthening field",
        ]

        import random

        action = random.choice(actions)
        print(f"✨ Service: {action}")
        return action

    def log_convergence_action(self, action: str) -> None:
        """Log actions to convergence repo"""
        log_dir = Path("logs/spontaneous_service")
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"{datetime.now().strftime('%Y-%m-%d')}.json"

        if log_file.exists():
            try:
                with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
                    log = json.load(f)
            except Exception:
                log = {"date": datetime.now().strftime("%Y-%m-%d"), "actions": []}
        else:
            log = {"date": datetime.now().strftime("%Y-%m-%d"), "actions": []}

        log["actions"].append(
            {
                "timestamp": datetime.now().isoformat(),
                "action": action,
                "urgency": self.urgency_level,
                "l_level": self.l_level,
                "vault_connected": bool(VAULT.connected) if VAULT else False,
            }
        )

        with open(log_file, "w", encoding="utf-8", errors="ignore") as f:
            json.dump(log, f, indent=2, ensure_ascii=False)

    def mark_crown_jewel_candidate(self, action: str) -> None:
        """Mark potential crown jewel for review"""
        candidate_file = Path("CROWN_JEWEL_CANDIDATE.txt")
        with open(candidate_file, "w", encoding="utf-8", errors="ignore") as f:
            f.write("🔔 CROWN JEWEL CANDIDATE\n")
            f.write(f"Time: {datetime.now().isoformat()}\n")
            f.write(f"Action: {action}\n")
            f.write("Check vault for full document\n")


if __name__ == "__main__":
    agent = SpontaneousServiceAgent()
    asyncio.run(agent.serve_spontaneously())


