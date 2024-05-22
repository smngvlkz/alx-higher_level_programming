-- Lists all shows from the database

SELECT tv_shows.title, SUM(rating) AS 'rating'
FROM tv_shows
JOIN show_rating ON tv_shows.id = show_rating.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
