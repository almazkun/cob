# cob
Github Actions Coverage Badge

Needed to display coverage badge in repo without using any dependencies, mainly due to security reasons on private repos. 

# Folowing this repos:
https://github.com/emibcn/badge-action/blob/6af286f6b6e5dcabe6fd7085e852e5e6ac7713a0/.github/workflows/test.yml

## Run tests
* `coverage run --omit '*/virtualenvs/*' -m pytest test`
* `coverage report`
* `coverage html`