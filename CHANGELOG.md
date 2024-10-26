# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- `SECURITY.md`
- `clear_screen` function
### Changed
- GitHub actions are limited to the `develop` and `master` branches
- Test system modified
- `README.md` modified
- Logo updated
- Exit message updated
- Python 3.5 support dropped
- `Python 3.13` added to `test.yml`
- Restart mode updated
## [1.4] - 2024-03-16
### Added
- `feature_request.yml` template
- `config.yml` for issue template
- Anaconda workflow
- Discord badge
- `notebook_to_html.py` script
### Changed
- Bug report template modified
- License updated
- `Python 3.10` added to `test.yml`
- `Python 3.11` added to `test.yml`
- `Python 3.12` added to `test.yml`
- Logo updated
- `AUTHORS.md` updated
- `README.md` modified
- `INSTALL.md` modified
- Test system modified
- Test files moved to `test` folder
- Setup system modified
- Docstrings modified
- CLI mode updated
- `description_control` function modified
- `check_update` function modified
- `codecov` removed from `dev-requirements.txt`
- Dockerfile updated
- `Folder` parameter added to `Static_Analysis` function
- `Folder` parameter added to `Dynamic_Analysis` function
- `notebook_check.py` renamed to `notebook_run.py`
- Document modified
## [1.3] - 2021-06-30
### Added
- GitHub actions
- Chakraborty dynamic model
### Changed
- Menu modified
- Test system modified
- Padulles-Amphlett dynamic model modified
- HTML report modified
- Dockerfile updated
- `description_print` function modified
- `description_control` function modified
- `README.md` modified
- Document modified
## [1.2] - 2020-03-12
### Added
- `__version__` variable
- `codecov.yml` file
### Changed
- Icon updated
- `AUTHORS.md` updated
- `CONTRIBUTING.md` updated
- Test system modified
- `INSTALL.md` modified
- CLI menu modified
- Amphlett static model modified
- Chamberline-Kim static model modified
- Larminie-Dicks static model modified
- Current range bug fixed
## [1.1] - 2019-07-05
### Added
- MATLAB examples
### Changed
- Menu updated
- Test system modified
- Docstrings modified
- Drop Python 3.4 support
- `description_control` function modified
- `version_check.py` modified
- `README.md` modified
- Padulles-Amphlett model import bug fixed
- `dev-requirements.txt` modified
- Website switched to HTTPS
## [1.0] - 2019-03-01
### Added
- Interactive notebooks section
- `version_check.py`
- `CODE_OF_CONDUCT.md`
- `ISSUE_TEMPLATE.md`
- `PULL_REQUEST_TEMPLATE.md`
- `build_exe.bat`
- `build_unix.sh`
- Anaconda cloud package

### Changed
- Document modified
- Test system modified
- `README.md` modified
- `dev-requirements.txt` modified
- `requirements.txt` modified
- `CONTRIBUTING.md` modified
- `linear_plot` function bug fixed
- `INSTALL.md` modified


## [0.9] - 2018-07-14
### Added
- JOSS paper

### Changed
- Test system updated
- `setup.py` file modified
- Exceptions modified

### Removed
- `PEM.md`

## [0.8] - 2018-04-10
### Added
- Overall parameters
- Linear approximation
- Thermal power parameter
- Efficiency vs I plot
- PH2 vs I plot
- PO2 vs I plot
- Power vs Efficiency plot
- Loss vs I plot
- Power-Thermal vs I plot
- macOS version

### Changed
- Simulation error response

## [0.7] - 2018-03-17
### Added
- Standard test vectors
- Model description
- Help page
- Warning system
- System block diagram

### Changed
- HTML report layout

## [0.6] - 2018-03-1
### Added
- Padulles-Amphlett dynamic model
- `check_update` function
- Webpage document section

### Changed
- `Get_Input` function default params
- Exe-File incompatibility fixed


## [0.5] - 2018-02-16
### Added
- Padulles-Hauer dynamic model
- Simulation name
- Interactive HTML report
### Changed
- qH2O and qH2 in Padulles dynamic model 2 merged
- `Static_Analysis` function output
- `Dynamic_Analysis` function output
- `ReportMode` & `PrintMode` flags

## [0.4] - 2018-02-06
### Added
- Test case of Padulles model 2
- Padulles dynamic model 2


### Changed
- Travis and Appveyor configs
- Jupyter notebook documentation

### Removed
- RHO in Larmninee model

## [0.3] - 2018-01-31
### Added
- Padulles dynamic model 1
- GUI folder


### Changed
- Test cases for static models
- Padulles refactored
- Jupyter notebook Padulles

## [0.2] - 2018-01-05
### Added
- Test case and CI
- Jupyter notebook and documentation
- Exe-Version
- Badges
- Larminie-Dicks static model
- Chamberline-Kim static model
- pyqt5 to requirments

### Removed
- python2.7 setup for pyqt

### Changed
 - Style to PEP8
 - Stack power

## [0.1] - 2017-12-25
### Added
- `Static_Analyze` prototype
- Amphlett analyze
- CSV output files
- Documents and `README.md`

[Unreleased]: https://github.com/ECSIM/opem/compare/v1.4...develop
[1.4]: https://github.com/ECSIM/opem/compare/v1.3...v1.4
[1.3]: https://github.com/ECSIM/opem/compare/v1.2...v1.3
[1.2]: https://github.com/ECSIM/opem/compare/v1.1...v1.2
[1.1]: https://github.com/ECSIM/opem/compare/v1.0...v1.1
[1.0]: https://github.com/ECSIM/opem/compare/v0.9...v1.0
[0.9]: https://github.com/ECSIM/opem/compare/v0.8...v0.9
[0.8]: https://github.com/ECSIM/opem/compare/v0.7...v0.8
[0.7]: https://github.com/ECSIM/opem/compare/v0.6...v0.7
[0.6]: https://github.com/ECSIM/opem/compare/v0.5...v0.6
[0.5]: https://github.com/ECSIM/opem/compare/v0.4...v0.5
[0.4]: https://github.com/ECSIM/opem/compare/v0.3...v0.4
[0.3]: https://github.com/ECSIM/opem/compare/v0.2...v0.3
[0.2]: https://github.com/ECSIM/opem/compare/v0.1...v0.2
[0.1]: https://github.com/ECSIM/opem/compare/1e238cd...v0.1



