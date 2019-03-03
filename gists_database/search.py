from .models import Gist

def search_gists(db_connection, **kwargs):
    if not kwargs:
        query = "SELECT * FROM gists"
    elif 'github_id' in kwargs:
        query = "SELECT * FROM gists WHERE github_id = :github_id"
    elif 'created_at' in kwargs:
        query = "SELECT * FROM gists WHERE date(created_at) = date(:created_at)"
    
    cursor = db_connection.execute(query,kwargs)
    result = []
    for gist in cursor:
        result.append(Gist(gist))
    
    return result