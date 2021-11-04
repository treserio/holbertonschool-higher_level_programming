-- dump hbtn_0d_tvshows and order by title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
	JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
