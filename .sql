select name, destination
from Events
where delay <=2
    and conditions = '_'
ORDER BY destination, name;