select MediaTypeId as ID, count(*) from Track
join MediaType on MediaType.MediaTypeId = Customer.MediaTypeId as ID
group by MediaTypeId order by count(*) desc;