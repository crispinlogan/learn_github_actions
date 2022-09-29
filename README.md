Throwaway repo to learn github actions

I made a couple of workflows:
- run_pre_commit.yaml - runs pre-commit on all files - currently install poetry with pip, could use poetry of course too but slower to install entire environment from poetry file and quicker to just install poetry itself
- release_new_version.yaml - given a comment in a PR that says `release patch version` it will do just that (see workflow itself for details). Current drawbacks are: it needs to be done on a branch called release_branch; having written the comment you need to wait a small amount for the release to work before merging (could easily only let people merge once all status checks had successfully passed to circumvent this). We could easily add stuff so it works for minor and major version too.

