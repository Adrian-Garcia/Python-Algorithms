""" 
  Recovered from
  http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/"""

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("max_rows", None)
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

minimum_support = 0.3
transactions = [
    [
        "parmesano",
        "yoghurt",
        "leche",
        "milanesa",
        "carne",
        "aceite",
        "pasta",
        "tomate",
        "cereal",
        "zanahoria",
        "papa",
        "cerveza",
    ],
    [
        "arroz",
        "chilorio",
        "frijoles",
        "parmesano",
        "cereal",
        "jugo",
        "durazno",
        "pasta",
        "tomate",
        "carne",
        "uva",
        "yoghurt",
        "harina",
        "miel",
        "milanesa",
        "insecticida",
    ],
    [
        "huevo",
        "leche",
        "parmesano",
        "milanesa",
        "oregano",
        "carne",
        "limon",
        "jugo",
        "salchicha",
        "bicarbonato",
        "azucar",
        "cocoa",
        "cacao",
        "cereal",
        "palomitas",
        "esponja",
        "avellana",
        "tostadas",
        "mango",
        "manzana",
        "levadura",
        "sacapuntas",
    ],
    [
        "refresco",
        "agua",
        "servilletas",
        "pinzas",
        "leche",
        "crema",
        "cafe",
        "colador",
        "huevo",
        "azucar",
        "yoghurt",
        "vainilla",
        "chispas",
        "lavatrastes",
        "harina",
        "hisopos",
        "pure",
        "canela",
    ],
    [
        "leche",
        "pasta",
        "tomate",
        "refresco",
        "pimienta",
        "servilletas",
        "milanesa",
        "cilantro",
        "jugo",
        "pepino",
        "cebolla",
        "pan",
        "tomillo",
        "mejorana",
        "caldo",
        "arroz",
        "papa",
        "cereal",
        "yoghurt",
        "palillos",
        "mozarella",
        "jabon",
        "carne",
    ],
    ["huevo", "leche", "refresco", "parmesano", "silicon", "jugo", "cafe"],
    [
        "leche",
        "parmesano",
        "cereal",
        "pan",
        "zanahoria",
        "chayote",
        "papa",
        "crema",
        "bbq",
        "limon",
        "manzana",
    ],
    ["leche", "jamon", "tomate", "totopos", "asadero", "galletas", "pasta", "refresco"],
    [
        "huevo",
        "mantequilla",
        "pasta",
        "jugo",
        "leche",
        "parmesano",
        "refresco",
        "manzana",
        "servilletas",
        "cereal",
        "hisopos",
    ],
    [
        "tomate",
        "pasta",
        "pan",
        "leche",
        "zanahoria",
        "papa",
        "chayote",
        "chilorio",
        "frijoles",
        "milanesa",
        "carne",
        "aceite",
        "yoghurt",
    ],
]

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
# print(df, end="\n\n")

frequent_itemsets = apriori(df, min_support=minimum_support, use_colnames=True)
frequent_itemsets["iteracion"] = frequent_itemsets["itemsets"].apply(lambda x: len(x))
frequent_itemsets

print(frequent_itemsets)
