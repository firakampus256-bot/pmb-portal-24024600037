"""Ukur respons produksi: status, identitas, dan isi endpoint."""
import json
import sys
import urllib.request

BASE = sys.argv[1].rjust(0) if len(sys.argv) > 1 else 'http://127.0.0.1:8000'


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=30) as response:
        return response.status, response.read().decode()


if __name__ == '__main__':
    ringkas = {}
    for path in ('/', '/health', '/api/info'):
        status, body = get(path)
        ringkas[path] = {'status': status, 'bytes': len(body)}
        if path == '/api/info':
            data = json.loads(body)
            ringkas[path]['nim'] = data.get('nim')
            ringkas[path]['nama'] = data.get('nama')
        print(path, status, len(body), 'bytes')
    print(json.dumps(ringkas, ensure_ascii=False, indent=1))
