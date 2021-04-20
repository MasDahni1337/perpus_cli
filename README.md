# perpus_cli
library yang dibutuhkan
```
pip3 install mysql-connector
pip3 install tabulate
```
run program
```
python main.py
```

## Library Zerodata
sesuaikan config dibawah ini dengan database lu
```python
cekdb = mysql.connector.connect(
    host = "localhost",
    user = "zeromind",
    passwd = "1",
    database = "testdb"
)
```
