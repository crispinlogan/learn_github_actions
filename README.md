Throwaway repo to learn github actions

I made a few workflows:
- run_pre_commit.yaml - runs pre-commit on all files - currently install poetry with pip, could use poetry of course too but slower to install entire environment from poetry file and quicker to just install poetry itself.....this takes around a minute to run - could speed up by just installing the required tools e.g. black and running that with same settings as in pre-commit file
- release_new_version.yaml - given a comment in a PR that says `release patch version` it will do just that (see workflow itself for details). Current drawbacks are: it needs to be done on a branch called release_branch; having written the comment you need to wait a small amount for the release to work before merging (could easily only let people merge once all status checks had successfully passed to circumvent this). We could easily add stuff so it works for minor and major version too.
- slack_notif_on_new_version_release.yml - posts to Slack channel on a Bump version commit (which signals new version release). Useful videos were https://www.youtube.com/watch?v=hzIub2noFw8 and https://www.youtube.com/watch?v=1n-jHHNSoTw - make sure to  /invite your_slack_app_name in the channel

Quirks of above:
- if you use release_new_version workflow method to release a version, then the slack_notif_on_new_version_release won't trigger (not quite sure why as it should trigger on a push to the repo which is what is done in release_new_version workflow)


