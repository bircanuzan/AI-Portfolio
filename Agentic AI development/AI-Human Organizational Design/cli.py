"""Run six enterprise HR analytics tools and combined executive briefing offline."""
import argparse
import json
from src.hcia.engine import CAPABILITIES,load_data,execute
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("capability",choices=CAPABILITIES)
    p.add_argument("--entity",choices=("ALL","CORP","INV","INF"),default="ALL")
    a=p.parse_args()
    print(json.dumps(execute(load_data(),a.capability,a.entity),indent=2))
