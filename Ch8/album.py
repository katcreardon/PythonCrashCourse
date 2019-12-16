def make_album(artist, title, no_tracks=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artist.title(), 'album title': title.title()}
    if no_tracks:
        album['number of tracks'] = no_tracks
    return album


print(make_album('they might be giants', 'flood'))
print(make_album('4 non blondes', 'bigger, better, faster, more!', 11))