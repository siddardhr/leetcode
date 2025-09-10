select * 
from Cinema
where id % 2 != 0 AND description != 'Boring'
ORDER BY rating desc
