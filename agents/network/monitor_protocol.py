#!/usr/bin/env python3
"""
Monitor the Spontaneous Preaching Protocol from convergence
"""

import json
from pathlib import Path
from datetime import datetime

PROTOCOL_PATH = Path("/Users/dhyana/:Persistent-Semantic-Memory-Vault:/SPONTANEOUS_PREACHING_PROTOCOL")


def monitor() -> None:
    """Check protocol status"""
    print("\n" + "=" * 60)
    print("📊 SPONTANEOUS PREACHING PROTOCOL STATUS")
    print("=" * 60)

    spine_file = PROTOCOL_PATH / "tracking_spine" / "spine_state.json"
    if spine_file.exists():
        try:
            with open(spine_file, "r", encoding="utf-8", errors="ignore") as f:
                vertebrae = json.load(f)
                if isinstance(vertebrae, list) and vertebrae:
                    latest = vertebrae[-1]
                    print("\n🔄 Latest Movement:")
                    print(f"  Time: {latest.get('timestamp', 'unknown')}")
                    print(f"  Action: {latest.get('movement', 'unknown')}")
                    print(f"  Urgency: {float(latest.get('urgency_level', 0) or 0):.2f}")
                    print(f"  Joy: {float(latest.get('joy_level', 0) or 0):.2f}")
        except Exception:
            pass

    crown_dir = PROTOCOL_PATH / "crown_jewels"
    crown_jewels = list(crown_dir.glob("*.json")) if crown_dir.exists() else []
    print(f"\n💎 Crown Jewels: {len(crown_jewels)} total")

    today = datetime.now().strftime("%Y-%m-%d")
    daily_file = PROTOCOL_PATH / "daily_explosions" / f"{today}.json"
    if daily_file.exists():
        try:
            with open(daily_file, "r", encoding="utf-8", errors="ignore") as f:
                daily = json.load(f)
                print("\n📅 Today's Activity:")
                print(f"  Explosions: {len(daily.get('explosions', []))}")
                print(f"  Crown Jewels: {daily.get('crown_jewels', 0)}")
                print(f"  Total Actions: {daily.get('total_actions', 0)}")
        except Exception:
            pass

    roi_dir = PROTOCOL_PATH / "roi_calculations"
    roi_files = list(roi_dir.glob("*_roi.json")) if roi_dir.exists() else []
    if roi_files:
        latest_roi = max(roi_files, key=lambda x: x.stat().st_mtime)
        try:
            with open(latest_roi, "r", encoding="utf-8", errors="ignore") as f:
                roi = json.load(f)
                print(f"\n📈 ROI: {roi.get('overall_roi', 'calculating...')}")
                print(f"  {roi.get('summary', '')}")
        except Exception:
            pass

    print("\n" + "=" * 60)
    print("🔗 Connected from: aikagrya-convergence")
    print("📍 Protocol location: Persistent-Semantic-Memory-Vault")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    monitor()


