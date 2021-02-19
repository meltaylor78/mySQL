select Title, Name from Album
join Artist on Album.ArtistID = Artist.ArtistID
limit 5;