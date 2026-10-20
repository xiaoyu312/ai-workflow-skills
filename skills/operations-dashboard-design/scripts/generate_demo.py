from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = {'classification': 'synthetic_demo', 'label': '模拟数据 DEMO', 'seed': 'operations-dashboard-design-demo-v1', 'rows': [{'channel': 'DEMO Alpha', 'amount': 1200, 'status': '模拟已对账'}, {'channel': 'DEMO Beta', 'amount': None, 'status': '模拟待核'}]}

HTML = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>模拟数据 DEMO</title><link rel="stylesheet" href="../tokens/colors_and_type.css"><style>body{font-family:var(--font-ui);background:var(--canvas);color:var(--ink);padding:2rem;line-height:var(--leading-body)}main{max-width:70rem;margin:auto}table{border-collapse:collapse;width:100%;background:var(--surface)}th,td{text-align:left;padding:1rem;border-bottom:1px solid var(--line)}td:nth-child(2){text-align:right;font-variant-numeric:tabular-nums}.scroll{overflow:auto}.status{color:var(--warn)}a:focus-visible{outline:3px solid var(--focus-ring);outline-offset:3px}</style><main><h1>模拟数据 DEMO</h1><p>固定合成样例；不是任何品牌的经营数据。</p><div class="scroll"><table><thead><tr><th>渠道</th><th>金额（示例单位）</th><th>状态</th></tr></thead><tbody><tr><td>DEMO Alpha</td><td>1,200</td><td>模拟已对账</td></tr><tr><td>DEMO Beta</td><td>—</td><td class="status">模拟待核</td></tr></tbody></table></div><p><a href="../README.md">说明</a></p></main></html>\n'

def main():
    destination = ROOT / "examples" / 'demo.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "examples" / "index.html").write_text(HTML, encoding="utf-8")

if __name__ == "__main__":
    main()
