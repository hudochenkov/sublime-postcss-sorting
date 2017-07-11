import sublime
import sublime_plugin
import json
from os.path import dirname, realpath, join, basename, splitext
from os import path

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge

# monkeypatch `Region` to be iterable
sublime.Region.totuple = lambda self: (self.a, self.b)
sublime.Region.__iter__ = lambda self: self.totuple().__iter__()

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'sorting.js')
CONFIG_NAMES = ['.postcss-sorting.json', 'postcss-sorting.json']

def local_postcss_settings():
	for folder in sublime.active_window().project_data()['folders']:
		for config_name in CONFIG_NAMES:
			config_file = join(folder['path'], config_name)
			if path.isfile(config_file):
				with open(config_file) as data_file:
					return json.load(data_file)

	return {}

def sublime_project_settings(view):
	settings = view.settings().get('PostCSSSorting')

	if settings is None:
		settings = {}

	return settings

def get_setting(view, key):
	setting = local_postcss_settings().get(key)

	if setting is None:
		setting = sublime_project_settings(view).get(key)

	if setting is None:
		setting = sublime.load_settings('PostCSSSorting.sublime-settings').get(key)

	return setting

def is_supported_syntax(view):
	syntax = splitext(basename(view.settings().get('syntax')))[0]

	return syntax in ('CSS', 'PostCSS', 'SCSS')

class PostcsssortingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if not self.has_selection():
			region = sublime.Region(0, self.view.size())
			originalBuffer = self.view.substr(region)
			processed = self.sorting(originalBuffer)

			if processed:
				self.view.replace(edit, region, processed)

			return

		for region in self.view.sel():

			if region.empty():
				continue

			originalBuffer = self.view.substr(region)
			processed = self.sorting(originalBuffer)

			if processed:
				self.view.replace(edit, region, processed)

	def sorting(self, data):
		sorting_options = {}

		if get_setting(self.view, 'order'):
			sorting_options['order'] = get_setting(self.view, 'order')

		if get_setting(self.view, 'properties-order'):
			sorting_options['properties-order'] = get_setting(self.view, 'properties-order')

		if get_setting(self.view, 'unspecified-properties-position'):
			sorting_options['unspecified-properties-position'] = get_setting(self.view, 'unspecified-properties-position')

		if get_setting(self.view, 'clean-empty-lines'):
			sorting_options['clean-empty-lines'] = get_setting(self.view, 'clean-empty-lines')

		if get_setting(self.view, 'rule-nested-empty-line-before'):
			sorting_options['rule-nested-empty-line-before'] = get_setting(self.view, 'rule-nested-empty-line-before')

		if get_setting(self.view, 'at-rule-nested-empty-line-before'):
			sorting_options['at-rule-nested-empty-line-before'] = get_setting(self.view, 'at-rule-nested-empty-line-before')

		if get_setting(self.view, 'declaration-empty-line-before'):
			sorting_options['declaration-empty-line-before'] = get_setting(self.view, 'declaration-empty-line-before')

		if get_setting(self.view, 'custom-property-empty-line-before'):
			sorting_options['custom-property-empty-line-before'] = get_setting(self.view, 'custom-property-empty-line-before')

		if get_setting(self.view, 'dollar-variable-empty-line-before'):
			sorting_options['dollar-variable-empty-line-before'] = get_setting(self.view, 'dollar-variable-empty-line-before')

		if get_setting(self.view, 'comment-empty-line-before'):
			sorting_options['comment-empty-line-before'] = get_setting(self.view, 'comment-empty-line-before')

		try:
			return node_bridge(data, BIN_PATH, [json.dumps(sorting_options)])
		except Exception as e:
			sublime.error_message('PostCSS Sorting\n%s' % e)

	def has_selection(self):
		for sel in self.view.sel():
			start, end = sel

			if start != end:
				return True

		return False

class PostcsssortingPreSaveCommand(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if get_setting(view, 'sort-on-save') is True and is_supported_syntax(view):
			view.run_command('postcsssorting')
