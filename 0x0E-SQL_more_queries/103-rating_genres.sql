-- List all genres in the databse by their rating

SELECT tv_genres.name, SUM(rating) AS 'rating'
FROM tv_genres
JOIN genre_rating ON tv_genres.id = genre_rating.genre_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
