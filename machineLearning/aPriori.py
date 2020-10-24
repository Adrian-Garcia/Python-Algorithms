''' 
	Recovered from
  http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/'''

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

minimum_support = 0.3
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
print(df, end="\n\n")

frequent_itemsets = apriori(df, min_support=minimum_support, use_colnames=True)
frequent_itemsets['iteracion'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

print(frequent_itemsets)
