-- Write your query below
SELECT p.first_name, p.last_name, d.city, d.state 
FROM person p LEFT JOIN address d ON
p.person_id = d.person_id;