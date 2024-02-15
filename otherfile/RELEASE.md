
# OPEM Release Instructions

#### Last Update: 2024-02-15

1. Create the `release` branch under `develop`
2. Update all version tags
	1. `setup.py`
	2. `INSTALL.md`
	3. `otherfile/version_check.py`
	4. `otherfile/meta.yaml`
	5. `opem/Params.py`
	6. `OPEM.spec`
	7. `test/test_Functions.py`
	8. `otherfile/Version.rc`
	9. All notebooks (`Documents/*.ipynb`)
3. Update `CHANGELOG.md`
	1. Add a new header under `Unreleased` section (Example: `## [0.1] - 2022-08-17`)
	2. Add a new compare link to the end of the file (Example: `[0.2]: https://github.com/ECSIM/opem/compare/v0.1...v0.2`)
	3. Update `develop` compare link (Example: `[Unreleased]: https://github.com/ECSIM/opem/compare/v0.2...develop`)
4. Update `.github/ISSUE_TEMPLATE/bug_report.yml`
   1. Add new version tag to `OPEM version` dropbox options
5. Update Document
	1. Run `otherfile/notebook_run.py`
6. Create a PR from `release` to `develop`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Wait for all CI pass
	6. Need review (**1** reviewers)
7. Merge `develop` branch into `master`
	1. `git checkout master`
	2. `git merge develop`
	3. `git push origin master`
	4. Wait for all CI pass
8. Build EXE file
	1. Run `build_exe.bat` (Use `Python 3.4.x`)
9. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
	6. Upload EXE file
	7. Zip `MATLAB` folder
	8. Upload `MATLAB.zip`
10. Bump!!
11. Close this version issues
12. Close milestone
13. Generate HTML files
	1. Run `otherfile/notebook_to_html.py`
	2. Copy `doc` folder for the next steps
14. Update website
	1. `git checkout gh-pages`
	2. Update `download.html` page
		1. Add a new section
		2. Add changelogs
	3. Update all version tags
		1. `index.html`
		2. `doc/index.html`
	4. Update size of files
		1. `index.html`
	5. Update `doc` folder (Step **13.2**)
		1. Update `Dynamic` folder
		2. Update `Static` folder