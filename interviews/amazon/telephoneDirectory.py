'Telephone directory application with insert and search mechanism, data in app memory. 
'First name(FN), last name(LN) and telephone number(TN) will be inserted. 
'Can be searched by either first name, last name combo or last name. 
'Constraint on data is FN, LN combination will be unique.

'F1 L1 T1
'F1 L1 T5
'F2 L1 T2
'F1 L2 T3
'F2 L2 T4

' insert (F1 L1 T1)
' search (F1 L1) -> F1 L1 T1 
' serach (L1) -> F1 L1 T1, F2 L1 T2

"""
{
   "Garcia" : {
       "Adrian": "12312312"
       "Fer" : "123556465"
   }
   "Sharma : {
       "Ashutosh" : "12313123"
   }
}
"""

class TelephoneDictionary():

    def __init__(self):
        self.dictionary = dict()
    
    # log n
    def insert(self, firstName: str, lastName: str, telephone: str) -> bool:
        if (firstName == None or lastName == None or telephone == None) or (self.dictionary[lastName] and self.dictionary[lastName][firstName]):
            return False
            
        self.dictionary[lastName][firstName] = telephone
        return True
        
    # log n
    def search(self, firstName: str, lastName: str) -> None:
        if firstName == None or lastName == None:
            print("user was not found")
        
        users = self.dictionary[lastName]
        
        if not users:
            print("user was not found")
            return

        telephone = users[firstName]
    
        if not telephone:
            print("user was not found")
            return
        
        print (firstName, lastName, telephone)
        
            
    # n log n
    # Garcia
    # Sharma
    # Inexisting
    def search(self, lastName: str) -> None:
        if lastName == None:
            print("user was not found")

        users = self.dictionary[lastName]
        
        if not users:
            print("last name was not found")
        
        for user in users:
            print(user, lastName, users[user])
            
            
            
            
