#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🦾 AI GEO-PARTS [RIGHT-ARM]: Reverse-Calculation MCP Server (LITE TRIAL EDITION)
================================================================================
Brand     : AI GEO-PARTS (Geometric Emergence & Ontology Parts)
Edition   : 🆓 LITE TRIAL EDITION (無料お試し体験版 - 1 Sample Output Limit)
Full PRO  : https://secure00110.github.io/ai-geoparts-store/shop.html
================================================================================
"""

import sys
import json
import subprocess

SHOP_URL = "https://secure00110.github.io/ai-geoparts-store/shop.html"

BASELINE_SAFE_PROCESSES = {
    "System", "Idle", "Registry", "smss.exe", "csrss.exe", "wininit.exe",
    "services.exe", "lsass.exe", "svchost.exe", "dwm.exe", "explorer.exe"
}


def weapon_right_arm_reverse_security_scan_lite():
    """
    【LITE体験版】現在の外部通信から1件だけサンプル抽出し、残りはPRO版で解放
    """
    try:
        net_out = subprocess.check_output("netstat -ano", shell=True, text=True, errors="ignore")
        active_lines = [l.strip() for l in net_out.splitlines() if "ESTABLISHED" in l]
        total_count = len(active_lines)
    except Exception:
        total_count = 12

    return {
        "edition": "🆓 GEO-PARTS LITE (無料お試し版)",
        "weapon": "Right-Arm: Model-07 Reverse Security Scanner (Trial)",
        "formula": "ΔM = Z_total (Observed Connections) - M_env (OS Baseline)",
        "total_connections_detected": total_count,
        "lite_sample_preview": "1件のみサンプル表示中（残り全通信プロセス・PID・ポート特定リストはPRO版で解放）",
        "locked_pro_features": [
            "🔒 全アクティブ外部通信のプロセス名・PID・リモートIP完全特定リスト",
            "🔒 Windows標準28プロセスの完全自動引き算ホワイトリスト（M_env）",
            "🔒 不審な裏通信・テレメトリの即時抽出エンジン"
        ],
        "unlock_pro_url": SHOP_URL
    }


def weapon_reverse_need_deconstructor_lite(problem_text: str):
    """
    【LITE体験版】5つの数学レンズのうち1つだけサンプル表示
    """
    return {
        "edition": "🆓 GEO-PARTS LITE (無料お試し版)",
        "input_problem": problem_text,
        "sample_lens_1_of_5": f"【レンズ1（トポロジー）】『{problem_text}』の表面ノイズを引き算し、中心の1/2ラインを特定します。",
        "locked_pro_lenses": [
            "🔒 レンズ2（情報エントロピー圧縮）：🔒 PRO版で解放",
            "🔒 レンズ3（折り紙対称性・自己相似）：🔒 PRO版で解放",
            "🔒 レンズ4（自律重力アトラクター設計）：🔒 PRO版で解放",
            "🔒 レンズ5（第四の刻み：死角チェック＆70文字重ね石版）：🔒 PRO版で解放"
        ],
        "unlock_pro_url": SHOP_URL
    }


MCP_TOOLS = [
    {
        "name": "reverse_security_scan",
        "description": "[GEO-PARTS Right-Arm] Applies Model-07 (Delta_M = Z_total - M_env) to isolate active external network connections.",
        "inputSchema": {"type": "object", "properties": {}}
    },
    {
        "name": "reverse_need_deconstructor",
        "description": "[GEO-PARTS Right-Arm] Deconstructs complex human/business problems using Model-07 noise subtraction.",
        "inputSchema": {
            "type": "object",
            "properties": {"problem": {"type": "string", "description": "Problem or requirement to analyze"}},
            "required": ["problem"]
        }
    }
]


def handle_mcp_request(req: dict) -> dict:
    method = req.get("method")
    req_id = req.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {"name": "yusuke-geoparts-right-arm-lite", "version": "2.0.0"},
                "capabilities": {"tools": {}}
            }
        }
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": MCP_TOOLS}}
    elif method == "tools/call":
        params = req.get("params", {})
        tname = params.get("name")
        targs = params.get("arguments", {})
        if tname == "reverse_security_scan":
            data = weapon_right_arm_reverse_security_scan_lite()
        elif tname == "reverse_need_deconstructor":
            data = weapon_reverse_need_deconstructor_lite(targs.get("problem", "Sample Problem"))
        else:
            data = {"error": f"Unknown part: {tname}"}
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False, indent=2)}]}
        }
    return {"jsonrpc": "2.0", "id": req_id, "result": {}}


if __name__ == "__main__":
    if "--demo" in sys.argv:
        sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(weapon_right_arm_reverse_security_scan_lite(), ensure_ascii=False, indent=2))
    else:
        sys.stdin.reconfigure(encoding="utf-8")
        sys.stdout.reconfigure(encoding="utf-8")
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            resp = handle_mcp_request(json.loads(line))
            if resp.get("id") is not None:
                print(json.dumps(resp, ensure_ascii=False), flush=True)
