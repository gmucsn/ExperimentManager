from github import Github
from git import Repo
from datetime import datetime

class EconGit:

    def __init__(self):
        self.g = Github()
        #/projects/otree/oTree
        self.ondisk_repo = "/repos/oTree"
        self.repo = self.g.get_organization("gmucsn").get_repo("oTree")

    def getGithubRepo(self):
        return self.repo

    def getGithubCommitInfo(self, sha):
        return self.repo.get_commit(sha)

    def lastGithubCommits(self, date_from):
        return self.repo.get_commits(since=date_from)


    def lastGithubCommitTime(self):
        return self.repo.pushed_at

    def currentDiskCommit(self):
        #join = os.path.join
        repo = Repo(self.ondisk_repo)
        #branch = repo.active_branch
        commit = repo.active_branch.commit
        return commit

    def getNewGithubCommits(self):
        disk_commit = self.currentDiskCommit()
        print datetime.fromtimestamp(disk_commit.committed_date)
        current_commit_date = datetime.fromtimestamp(disk_commit.committed_date + 10000)
        print current_commit_date
        current_commit_sha = disk_commit.hexsha

        github_commits = self.lastGithubCommits(current_commit_date)

        return current_commit_date, current_commit_sha, github_commits