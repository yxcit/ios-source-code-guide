import datetime as dt, hashlib, json, os, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=Path(__file__).resolve().parent

def publish(now, check=False):
    queue=json.loads((BASE/'queue.json').read_text())
    pending=[]
    for q in queue:
        assert re.fullmatch('[a-z0-9-]+',q['id'])
        src=(BASE/'content'/q['source']).resolve()
        assert src.parent == BASE/'content'
        assert hashlib.sha256(src.read_bytes()).hexdigest()==q['sha256']
        dest=ROOT/'articles'/(q['id']+'.md')
        if not dest.exists(): pending.append(q)
    due=[q for q in pending if dt.datetime.fromisoformat(q['publish_at'])<=now]
    if check or not due:
        print(json.dumps({'pending':len(pending),'due':len(due),'next':pending[0]['publish_at'] if pending else None}));return
    q=due[0];relative='articles/'+q['id']+'.md'
    readme=ROOT/'README.md';text=readme.read_text()
    assert text.count('<!-- guides:end -->')==1
    (ROOT/relative).write_bytes((BASE/'content'/q['source']).read_bytes())
    readme.write_text(text.replace('<!-- guides:end -->',f"- [{q['title']}]({relative})\n<!-- guides:end -->"))
    print('Prepared '+relative)
if __name__=='__main__':
    publish(dt.datetime.now(dt.timezone.utc),'--check' in sys.argv)
