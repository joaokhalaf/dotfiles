#!/usr/bin/env python3
import json
import sys
import time

data = json.load(sys.stdin)
parts = [(data.get("model") or {}).get("display_name", "?")]

ctx = (data.get("context_window") or {}).get("used_percentage")
if ctx is not None:
    parts.append(f"ctx {ctx:.0f}%")

limits = data.get("rate_limits") or {}
for key, label in (("five_hour", "5h"), ("seven_day", "7d")):
    used = (limits.get(key) or {}).get("used_percentage")
    if used is not None:
        parts.append(f"{label} {used:.0f}%")

expires = (data.get("prompt_cache") or {}).get("expires_at")
if expires:
    left = int(expires - time.time()) // 60
    parts.append(f"cache {left}m" if left > 0 else "cache frio")

print(" · ".join(parts))
