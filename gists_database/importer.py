import requests
#from pprint import pprint

def import_gists_to_database(db, username, commit=True):
    
    #pull gists from github
    resp = requests.get("https://api.github.com/users/{}/gists".format(username))
    resp.raise_for_status()
    
    gist_data = resp.json()
    #pprint(gist_data)
    
    for gist in gist_data:
        params = {
            'github_id': gist['id'],
            'html_url': gist['html_url'], 
            'git_pull_url': gist['git_pull_url'], 
            'git_push_url': gist['git_push_url'], 
            'commits_url': gist['commits_url'], 
            'forks_url': gist['forks_url'], 
            'public': gist['public'], 
            'created_at': gist['created_at'], 
            'updated_at': gist['updated_at'], 
            'comments': gist['comments'], 
            'comments_url': gist['comments_url']
        }
    
    ## insert each gist - in the for loop - to gists table.
        db.execute("""
            INSERT INTO gists
            (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url)
            VALUES
            (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, :comments_url)
        """, params)
    
    if commit:
        db.commit()