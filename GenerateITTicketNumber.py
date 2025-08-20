import random 
from datetime import datetime 

ticket_number = f"IT-{datetime.now().year}-{random.randint(1000,9999)}" 
output = {"ITTicket":ticket_number}
