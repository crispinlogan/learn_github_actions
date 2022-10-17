![Tests](https://github.com/crispinlogan/learn_github_actions/actions/workflows/tests.yml/badge.svg)
![Pre-commit run (black, flake8, isort)](https://github.com/crispinlogan/learn_github_actions/actions/workflows/run_pre_commit.yaml/badge.svg)
![Slack notifs for new release](https://github.com/crispinlogan/learn_github_actions/actions/workflows/slack_notif_on_new_version_release.yml/badge.svg)
<!-- ![Version release on PR comment](https://github.com/crispinlogan/learn_github_actions/actions/workflows/release_new_version.yml/badge.svg) -->


learn_github_actions
--------------------

Throwaway repo to learn github actions

I made a few workflows:
- run_pre_commit.yaml - runs pre-commit on all files - currently install poetry with pip, could use poetry of course too but slower to install entire environment from poetry file and quicker to just install poetry itself
- release_new_version.yaml - given a comment in a PR that says `release patch version` it will do just that (see workflow itself for details). Current drawbacks are: it needs to be done on a branch called release_branch; having written the comment you need to wait a small amount for the release to work before merging (could easily only let people merge once all status checks had successfully passed to circumvent this). We could easily add stuff so it works for minor and major version too.
- slack_notif_on_new_version_release.yml - posts to Slack channel on a Bump version commit (which signals new version release). Useful videos were https://www.youtube.com/watch?v=hzIub2noFw8 and https://www.youtube.com/watch?v=1n-jHHNSoTw - make sure to  /invite your_slack_app_name in the channel

I also added in some tests with pytest, you can run `pytest --cov` in the root of the repo to run the tests.
I also added the tests to a noxfile, so you can just run `nox` and the tests within the noxfile will run (only pytest tets for now).
I also added the nox command to a github actions workflow - tests.yml, so it runs the tests on every push to github.
