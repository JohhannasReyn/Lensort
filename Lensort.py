import sublime
import sublime_plugin
from queue import PriorityQueue

class SortLinesByLengthCommand(sublime_plugin.TextCommand):
    def run(self, edit, reverse=False):
        settings = sublime.load_settings("Lensort.sublime-settings")

        tab_size = self.view.settings().get("tab_size", 4)  # Default to 4 if not set
        preserve_preceding_whitespace = settings.get("preserve_preceding_whitespace", "no")
        whitespace_counted_in_sort = settings.get("whitespace_counted_in_sort", False)

        leading_whitespace_list = []
        sorted_lines = []
        leading_space = ""
        pq = PriorityQueue()
        for region in self.view.sel():

            if not region.empty():
                lines = self.view.lines(region)
                
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
        if reverse:
            sorted_lines.reverse()
        sorted_text = "\n".join(sorted_lines)
        self.view.replace(edit, region, sorted_text)

