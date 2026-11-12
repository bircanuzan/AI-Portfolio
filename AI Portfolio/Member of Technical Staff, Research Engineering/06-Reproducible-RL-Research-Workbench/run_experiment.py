"""Produce independently reproducible synthetic traces and a metrics report."""
import json
import platform
import sys
from pathlib import Path
from benchmark import benchmark
from pipeline import make_episode, sha256, verify_episode, canonical_json
from training import train, greedy


def main():
    output = Path(__file__).parent / 'results'
    output.mkdir(exist_ok=True)
    q, training = train()
    summary = benchmark(q)
    traces = []
    for eid in range(20):
        sample = make_episode(eid, seed=1000+eid, policy=lambda state: greedy(q, state))
        ok, msg = verify_episode(sample)
        if not ok:
            raise RuntimeError('episode verifier failed: '+msg)
        traces.extend(sample)
    digest = sha256(traces)
    with (output/'episodes.jsonl').open('w', encoding='utf-8') as f:
        for entry in traces: f.write(canonical_json(entry)+'\n')
    manifest = {'classification': 'independent educational tabular RL simulation',
                'environment': 'GridWorld 4x4; 2 walls; horizon 30; reward +1 goal/-0.02 step/-0.1 invalid/-0.3 timeout',
                'algorithm': 'tabular q-learning; seed 7; 4500 episodes',
                'python': platform.python_version(),
                'training': training, 'benchmark': summary,
                'synthetic_dataset': {'episodes':20,'transitions':len(traces),'sha256':digest,'replay_verified':True},
                'limits': ['not deep RL', 'not fine-tuning a neural model', 'not scalable RL production infrastructure', 'not external peer-reviewed benchmark']}
    (output/'metrics.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(manifest,indent=2))

if __name__ == '__main__': main()
