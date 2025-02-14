#Create a Calss 'Attorney' for storing info of few partners working at Pearson Spector Litt.

class Attorney():
    Firm = 'PSL'
    def __init__(self, name, buy_in, designation):
        self.name = name
        self.buy_in = buy_in
        self.designation = designation
    
Harvey = Attorney('Harvey Spector', '$2,000,000', 'Name Partner')
print(Harvey.name, Harvey.buy_in, Harvey.designation)

Donna = Attorney('Donna Paulsen', '$500,000', 'COO')
print(Donna.name, Donna.buy_in, Donna.designation)

Mike = Attorney('Mike Ross', '$1,000,000', 'Senior Partner')
print(Mike.name, Mike.buy_in, Mike.designation)