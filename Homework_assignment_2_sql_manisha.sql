desc sakila.film;
desc sakila.actor;
desc sakila.film_actor;

select F.title, F.description, A.first_name, A.last_name from sakila.film F, sakila.film_actor FA ,sakila.actor A where lower(F.title) like lower('y%') and FA.film_id = F.film_id and FA.actor_id = A.actor_id;

