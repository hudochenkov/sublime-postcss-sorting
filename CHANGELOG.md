# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## 3.0.1

* Fix for a crash if file was opened outside of a project.

## 3.0.0

BREAKING CHANGES!

* Update to postcss-sorting@3.1.0
* Config for 3.0.0 might be partially incompatible with 2.0.0 config. Please read migration guide and postcss-sorting release notes:
	* Release notes: https://github.com/hudochenkov/postcss-sorting/releases/tag/3.0.0
	* Migration guide from 2.x: https://github.com/hudochenkov/postcss-sorting#migration-from-2x
* Added support for config in `postcss-sorting.json` and `.postcss-sorting.json`, which could be located in the root folder of a project.

## 2.1.1

* Fixed a regression when `emptyLineBefore` wasn't working properly when `declaration-empty-line-before` wasn't set.

## 2.1.0

* Update to postcss-sorting@2.1.0 https://github.com/hudochenkov/postcss-sorting/releases/tag/2.1.0
* Add support for `n` Node.js version manager

## 2.0.0

* Update to postcss-sorting@2.0.1
* Config for 2.0.0 is incompatible with previous configs. Please read migration guide and docs https://github.com/hudochenkov/postcss-sorting#migration-from-1x

## 1.7.0
* Update to postcss-sorting@1.7.0

## 1.6.1
* Update to postcss-sorting@1.6.1

## 1.6.0
* Update to postcss-sorting@1.6.0
* Update dependencies

## 1.5.1
* Update to postcss-sorting@1.4.1

## 1.5.0
* Added `preserve-empty-lines-between-children-rules`, which preserve empty lines between children rules and preserve empty lines for comments between children rules.

## 1.4.1
* Update to postcss-sorting@1.3.1

## 1.4.0
* Added `empty-lines-between-media-rules` option which set a number of empty lines between nested media rules.

## 1.3.3
* Update to postcss-sorting@1.2.3

## 1.3.2
* Update to postcss-sorting@1.2.2

## 1.3.1
* Update to postcss-sorting@1.2.1

## 1.3.0
* Added `empty-lines-between-children-rules` option which set a number of empty lines between nested children rules. (thanks, @scalder27)

## 1.2.0
* Added options for auto-sorting on save (disabled by defaut):

	```json
	{
		"sort-on-save": false
	}
	```

## 1.1.0
* Update postcss-sorting to 1.1.0
* Support for SCSS files to sort

## 1.0.1
* Fix package folder name in menu paths.

## 1.0.0
* Initial release.
