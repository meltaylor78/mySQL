select 
    concat(Customer.FirstName, " ", Customer.LastName) as Name, 
    Invoice.InvoiceDate as Date, 
    Invoice.Total as Total
from Invoice 
inner join Customer on Customer.CustomerId = Invoice.CustomerId  
order by Total desc, InvoiceDate desc 
limit 10;