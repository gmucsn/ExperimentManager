from experimentManager import app
from flask import render_template
from git_request_methods import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/production')
def production():
    gitaccess = EconGit()

    current_commit_date, current_commit_sha, github_commits = gitaccess.getNewGithubCommits()

    for github_commit in github_commits:
        if github_commit .commit is not None:
            print github_commit.commit.author.date

        print "sjsj"
        m = gitaccess.getGithubCommitInfo(github_commit.sha)
        print m.author
        for gstatus in github_commit.get_statuses():
            print gstatus.created_at
            print "test..."

    github_repo = gitaccess.getGithubRepo()
    return render_template('production.html', recent_commit_time=current_commit_date,
                           disk_commit_sha=current_commit_sha,
                           github_commits=github_commits,
                           github_repo=github_repo)

@app.route('/staging')
def staging():
    return render_template('staging.html')