def make_album(artist, title, no_tracks=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artist.title(), 'album title': title.title()}
    if no_tracks:
        album['number of tracks'] = no_tracks
    return album


while True:
    print("\n(enter 'q' at any time to quit)")
    artist = input("Enter the album artist: ")
    if artist == 'q':
        break

    title = input("Enter the album title: ")
    if title == 'q':
        break

    print(make_album(artist, title))
