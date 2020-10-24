import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

transactions = [['milk', 'bread', 'eggs'],
				['milk', 'juice'],
				['juice', 'butter'],
				['milk', 'bread', 'eggs'],
				['coffe', 'eggs'],
				['coffe'],
				['coffe', 'juice'],
				['milk', 'bread', 'cookies', 'eggs'],
				['cookies', 'butter'],
				['milk', 'bread']]

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

print(apriori(df, min_support=0.3))
