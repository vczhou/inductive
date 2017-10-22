import requests
payload = { 'q': 'Gen1',
            'include-css-link': 'true',
            'inline-styles': 'true',
            'wrapping-div': 'true',
            'include-passage-references': 'true',
            'include-verse-anchors': 'true',
            'include-chapter-numbers': 'true',
            'include-first-verse-numbers': 'true',
            'include-verse-numbers': 'true',
            'include-headings': 'true'
            }
r = requests.get('https://api.esv.org/v3/passage/html/', params = payload, headers={'Authorization': 'Token cbf78308c748ab16c2bf250961ba5e1d5e619e56'})
print(r.json()['passages'])