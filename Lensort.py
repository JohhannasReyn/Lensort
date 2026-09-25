import sublime
import sublime_plugin
from queue import PriorityQueue

class SortLinesByLengthCommand(sublime_plugin.TextCommand):
    def run(self, edit, reverse=False):
        settings = sublime.load_settings("Lensort.sublime-settings")

        tab_size = self.view.settings().get("tab_size", 4)  # Default to 4 if not set
        preserve_preceding_whitespace = settings.get("preserve_preceding_whitespace", "no")
        whitespace_counted_in_sort = settings.get("whitespace_counted_in_sort", False)

        # Expand each selection to whole lines, leaving a trailing newline that
        # ends the selection outside the region so it is never dropped.
        # With no text selected, sort the whole document.
        selections = [region for region in self.view.sel() if not region.empty()]
        if not selections and self.view.size() > 0:
            selections = [sublime.Region(0, self.view.size())]

        regions = []
        for region in selections:
            begin = self.view.line(region.begin()).begin()
            end = region.end()
            if end > region.begin() and self.view.substr(end - 1) == "\n":
                end -= 1
            end = self.view.line(end).end()
            regions.append(sublime.Region(begin, end))

        # Merge selections that end up covering the same lines.
        merged = []
        for region in sorted(regions, key=lambda r: r.begin()):
            if merged and region.begin() <= merged[-1].end():
                merged[-1] = sublime.Region(merged[-1].begin(), max(merged[-1].end(), region.end()))
            else:
                merged.append(region)

        # Process from last to first so earlier offsets stay valid.
        for region in reversed(merged):
            sorted_lines = self.sort_lines(self.view.lines(region), tab_size,
                                           preserve_preceding_whitespace, whitespace_counted_in_sort)
            if reverse:
                sorted_lines.reverse()
            self.view.replace(edit, region, "\n".join(sorted_lines))

    def sort_lines(self, lines, tab_size, preserve_preceding_whitespace, whitespace_counted_in_sort):
        leading_whitespace_list = []
        sorted_lines = []
        pq = PriorityQueue()

        for line in lines:
            line_str = self.view.substr(line)
            line_str = line_str.replace("\t", " " * tab_size)
            line_str = line_str.rstrip()
            stripped_line = line_str.lstrip()

            if preserve_preceding_whitespace == "move_with_line" and whitespace_counted_in_sort:
                leading_whitespace_list.append("")
                pq.put((len(line_str),line_str)) # uses length of line w/ whitespace

            else:

                if preserve_preceding_whitespace == "leave_in_place":
                    leading_whitespace_list.append(line_str[:len(line_str) - len(stripped_line)])
                    pq.put((len(stripped_line), stripped_line))

                elif preserve_preceding_whitespace == "move_with_line":
                    leading_whitespace_list.append("")
                    pq.put((len(stripped_line), line_str))

                else: # preserve_preceding_whitespace == "no"
                    leading_whitespace_list.append("")
                    pq.put((len(stripped_line),stripped_line))

        i = 0
        while not pq.empty():
            sorted_line = pq.get()[1]
            leading_space = leading_whitespace_list[i] if i < len(leading_whitespace_list) else ""
            sorted_lines.append(leading_space + sorted_line)
            i += 1
        return sorted_lines
