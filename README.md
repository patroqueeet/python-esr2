# python-esr2
Swiss ESR bank record reader. Forked from https://bitbucket.org/loss/python-esr/src/default/

```py
from esr.esr import ESR

with open('/Users/jirkaschaefer/Desktop/tmp/__spy/testimport.v11', 'rt') as f:
    data = f.read()

statement = ESR.parse(data)
for record in statement.records:
    print(record)
```
