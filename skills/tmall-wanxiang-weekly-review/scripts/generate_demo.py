from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = {'classification': 'synthetic_demo', 'label': '模拟数据 DEMO', 'seed': 'tmall-wanxiang-weekly-review-demo-v1', 'unit': 'CNY', 'weeks': [{'period': 'DEMO-baseline', 'spend': 1000, 'gmv': 3000, 'roi': 3, 'clicks': 500, 'orders': 30, 'aov': 100, 'cpc': 2, 'cvr': 0.06}, {'period': 'DEMO-prior', 'spend': 1200, 'gmv': 3600, 'roi': 3, 'clicks': 600, 'orders': 36, 'aov': 100, 'cpc': 2, 'cvr': 0.06}, {'period': 'DEMO-current', 'spend': 1500, 'gmv': 4500, 'roi': 3, 'clicks': 750, 'orders': 45, 'aov': 100, 'cpc': 2, 'cvr': 0.06}], 'current_scenes': [{'scene': 'DEMO-search', 'spend': 900, 'gmv': 2700}, {'scene': 'DEMO-audience', 'spend': 600, 'gmv': 1800}], 'operator_notes': [{'layer': '待验证', 'text': 'DEMO hypothesis only; no causal claim.'}]}

def main():
    destination = ROOT / "examples" / 'demo.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
