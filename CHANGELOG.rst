v0.8.0 (2023-03-04)
===================
- Partial fix for using letter selection for menu items (issue #73). Menu items
  can now be selected using letters rather than numbers; however, the Enter key
  is still required for input to be accepted.
- Added support for Python 3.10 and 3.11.
- Dropped support for Python 3.6.

v0.7.1 (2022-04-01)
===================
- Partial fix for ansiwrap import when using PyInstaller (issue #66). The issue
  is caused by the ansiwrap library (ansiwrap issue #6). Until ansiwrap #6 is
  properly fixed, the workaround is to use a conditional import and fall back
  to textwrap if ansiwrap fails to import. The drawback to this workaround is
  that ANSI colored text will no longer wrap properly when using PyInstaller.

v0.7.0 (2022-01-08)
===================
- Add feature to allow menu text to be dynamically updated (issue #25).
- Add feature to disable the automatic screen refresh when a menu item is
  selected - add "clear_screen=False" argument during Menu instantiation
  (issue #23).
- Allow colors in menu item names (issue #45).
- Menu items with text longer than the menu width will now wrap and indent
  properly (issue #62)
- Migrate from Travis-CI to GitHub Actions.

v0.6.0 (2019-09-07)
===================
- Fix issue #28, allow console screen argument for SelectionMenu.
- Fix issue #22, allow custom exit text for main menu.
- Fix issue #19, failure to clear screen using Windows 10 SSH.
- Potentially Breaking Change: reverted screen.input() method to return the
  simple string value, as it did in v0.4.0 and prior. Moved the InputResult
  tuple for input validation to the PromptUtils class.
- Expanding documentation and converting to Google-style docstrings (WIP).
- Add flush() method to screen.

v0.5.1 (2018-11-18)
===================
- Remove unnecessary imports (#10).

v0.5.0 (2018-11-02)
===================
- Add new input validation feature, contributed by DaBbleR23.
- Add feature to allow menu item removal.
- Add feature to allow user to cancel input.
- Remove external readline dependency.

v0.4.0 (2018-03-13)
===================
- Add feature to hide borders for menu items.
- Add feature to return to previous menu.
- Add printf and println functions to prompt_utils.

v0.3.0 (2018-03-09)
===================
- Add prompt_utils class.
- Add feature to show borders above or below menu items.
- Fix unit tests to run on windows.
- Add new borders for heavy outer/light inner; and double-line outer/light inner.

v0.2.0 (2018-03-09)
===================
- Add new multi-select menu feature.
- Use editable flag for installing project.
- Clean up imports.
- Expanded unit tests.
- Change doc theme to sphinx_rtd_theme.

v0.1.0 (2018-03-08)
===================
- Add Python 2.7, 3.5, and 3.6 to build matrix.
- Remove Python 2.6, 3.3, 3.4.
- PEP8 cleanup.
- Add pycodestyle to build process.
- Expanded unit tests.
- Add updated screenshots for Readme.
- Enhance text section to allow multi-line wrapping.
- Expand examples to show more features.
- Fix bug in heavy borders showing incorrect characters.
- Add optional bottom border to header section.
- Add prologue and epilogue sections to menus.
- Add methods for setting the border style factory and style type.
- Add border style type enumeration and factory.
- Change default padding for left and right to 2.
- Add new double-line border and rename border styles for consistency.
- Change default prompt.
- Update screen input method for python2 & 3 compatibility
- Remove deprecated methods
- Change sphinx theme and fix errors in rst files.
- Fix warnings/errors uncovered by pytest.
- Add unicode heavy border style.
- Add menu formatter class and related changes.
- Remove curses dependency.
- Initial commit of project, forked from curses-menu.

