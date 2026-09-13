from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, os, re, threading
from datetime import datetime

ROOT = Path(__file__).resolve().parent
VAULT = ROOT / 'Obsidian'
LOCK = threading.Lock()
def save(data):
    (ROOT / 'data').mkdir(exist_ok=True)
    target = ROOT / 'data/state.json'
    temp = target.with_suffix('.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    temp.replace(target)
    folder = VAULT / 'Contas'
    folder.mkdir(parents=True, exist_ok=True)
    for c in data['accounts']:
        name = re.sub(r'[^\w -]', '', c['name'])[:80] or 'Conta'
        lines = ['---', 'tipo: conta', 'tags: [crm, cliente]', '---', f"# {c['name']}", '', f"Objetivo: {c['goal']}", f"Responsável: {c['owner']}", '', '## Stakeholders']
        for s in c['people']: lines.append(f"- {s['name']} — {s['role']} — {s['email']}")
        lines += ['', '## Módulos e jornada']
        for m in c.get('cards', []): lines.append(f"- {m['module']} | Etapa: {m['stage']} | {m['status']} | Valor mensal: R$ {m['value']}")
        lines += ['', '## Atividades e pendências']
        for t in c['tasks']: lines.append(f"- [{'x' if t['done'] else ' '}] {t['title']} | Módulo: {t.get('module', 'Geral')} | Responsável: {t['owner']} | Prazo: {t['due']}")
        lines += ['', '## Reuniões, decisões e sinais']
        for n in c['notes']: lines += [f"### {n['type']} — {n['date']}", f"Módulo: {n.get('module', 'Geral')}", n['text'], '']
        safeid = re.sub(r'[^a-zA-Z0-9-]', '', c['id'])
        (folder / f"{safeid}.md").write_text('\n'.join(lines), encoding='utf-8')

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=str(ROOT / 'web'), **kw)
    def do_GET(self):
        if self.path == '/api/state':
            path = ROOT / 'data/state.json'
            body = path.read_bytes() if path.exists() else b'null'
            self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers(); self.wfile.write(body)
        else: super().do_GET()
    def do_POST(self):
        if self.path != '/api/state': self.send_error(404); return
        if self.headers.get('Origin') not in (None, 'http://localhost:8765', 'http://127.0.0.1:8765'):
            self.send_error(403); return
        try:
            size = int(self.headers.get('Content-Length', 0))
            if not 0 < size < 2_000_000: raise ValueError('Tamanho inválido')
            data = json.loads(self.rfile.read(size))
            if not isinstance(data.get('accounts'), list): raise ValueError('Dados inválidos')
            with LOCK: save(data)
            self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers(); self.wfile.write(b'{"ok":true}')
        except Exception as e:
            self.send_error(400, 'Unable to save data')

if __name__ == '__main__':
    print('CRM em http://localhost:8765', flush=True)
    ThreadingHTTPServer(('127.0.0.1', 8765), Handler).serve_forever()
