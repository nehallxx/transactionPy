import random
import csv
from random import uniform
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import os


@dataclass
class Transaction:
    transaction_id: int
    timestamp: float
    product_id: int=field(default_factory=lambda: random.randint(1,99999))
    quantity:int=field(default_factory=lambda: random.randint(1,5))
    price: float=field(default_factory=lambda: round(random.uniform(5.0,100.0),2))
    customer_id: int=field(default_factory=lambda: random.randint(1,99999))


# Open and append to file
def WriteToFile(path: str,T: Transaction, header: bool=False):
    with open(path,mode='a',newline='') as file:
        writer=csv.writer(file)
        if header:
         writer.writerow(T.__annotations__.keys())
        
        writer.writerow(T.__dict__.values())

if os.path.exists("retail_transactions.csv"):
   h=True
else:
   h=False

timenow=datetime.now()
i=0
while True:
  T=Transaction(
    transaction_id=i,
    timestamp=(timenow+timedelta(minutes=i)).timestamp(),
    )
  i+=1
 
  WriteToFile("retail_transactions.csv",T,header=h)
  h=False