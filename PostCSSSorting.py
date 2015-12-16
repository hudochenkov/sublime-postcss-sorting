import sublime
import sublime_plugin
import json
from os.path import dirname, realpath, join

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge

# monkeypatch `Region` to be iterable
sublime.Region.totuple = lambda self: (self.a, self.b)
sublime.Region.__iter__ = lambda self: self.totuple().__iter__()

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'sorting.js')

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
		try:
			return node_bridge(data, BIN_PATH, [json.dumps({
				'sort-order': self.get_setting('sort-order')
			})])
		except Exception as e:
			sublime.error_message('PostCSS Sorting\n%s' % e)

	def has_selection(self):
		for sel in self.view.sel():
			start, end = sel

			if start != end:
				return True

		return False

	def get_setting(self, key):
		settings = self.view.settings().get('PostCSSSorting')

		if settings is None:
			settings = sublime.load_settings('PostCSSSorting.sublime-settings')

		return settings.get(key)
