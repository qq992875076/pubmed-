import requests
import re
url = 'https://pubmed.ncbi.nlm.nih.gov/23479479/'
headers = {

            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            'cookie':"pm-csrf=WOMsnAg8u2ia9ytoBd3zS6hSHVViliyRaIXoJBH5yIiZbPMZggSVs4OvhHgDPLWt; ncbi_sid=7F8235C7274A9C53_11604SID; pm-sb=relevance; _ce.s=v~b7b03023b86e701b27f3384c2c9dd618fd943682~vpv~1; _ga_HF818T9R4Y=GS1.1.1655482980.28.1.1655482980.0; pm-sessionid=zafnn4vwlixxjtnga3dgz04sefn8g4ho; _gid=GA1.2.1969268230.1659676642; _gat_ncbiSg=1; _gat_dap=1; _ga=GA1.1.1166724415.1651816378; _ga_DP2X732JSX=GS1.1.1659709798.48.1.1659713590.0; pm-sfs=; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgCwFFcAiADCQIwBiAHAMwDCA7EQKxMkkBM5AggafQEL9c/AgQB0pMQFs4ANhAAaEAGMANsmUBrAHZQAHgBdMoIphDJtuiAFoA7hACGYBQFcAzg+tuoDiMsSuHl4+fojWAEbIAOYABN6+/tYAZgD2EFIxyinaBlA51mAOUVDWqg4AnikuRkqkZvGhyWlSiiDUAJxm7OzUROyt2KZYPe1M9APYZmoaOvo1OExmpkrY8lhJDqreA+NYLPIrlGak7HUrnVgNiRZg1dYGENHFEAoOygbIMFCtrGaIBgYwG4MAB6EG3cJSKCoMTaZSRWGqKSw5CIMRRFIwEE9bD0dq49oggDEPzqWB+/SwAB1tDE6TEQABfJQubSqFIOVC6QzGNrUMwbLbfJTUSZYB4uYVtI7kkUXNocforIZtUiyejjFZikCs9mc7nzbCLLBnEBMNYgZZm3aW1qyMkgdodJlKLJSKTZA28yngFyQ6GtflYCFQ9ArMwOcJuB5vebGkCtdgqvCENgUGgMZisNicHh8QTCUQSaRyRMOkPQjAV1AYSPRxzvDAAOQA8k3cImfdXYfDkIjkdpUejMYn5aR2knAyrSERKFbqA7x5ORT6Z4MBkHLWJqPQxFamJvZOxFkomNqnZqQLILdAHshYFLZDKQDi8QSmYygA; pm-sid=93KVyvge-yCJkO36TK6VUg:128da6d9582077d2a5259dc45e632554; pm-adjnav-sid=StaJkdq21k-yxxY5uqo_zw:128da6d9582077d2a5259dc45e632554"
            }
data = requests.get(url = url,headers=headers,timeout=10)
data = data.text
ab = re.findall(r'\<div\ class\=\"abstract\"\ id\=\"abstract\"\>(.*?)\<div\ class\=\"similar\-articles\"\ id\=\"similar\"\>', data, re.S)
ab = str(ab)
print(ab)
ab = ab.replace("\n", "")
ab = ab.replace(" ", "")
ab = re.sub(r'<.*?>', '', ab)
ab = ab.replace('\\n', ' ')
ab = re.sub(r'\s{4,}', '\n', ab)
ab = ab.replace(" ", "")
print(ab)