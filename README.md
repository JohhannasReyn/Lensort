# Lensort

**Lensort** is a Sublime Text plugin for sorting lines by length, with options to preserve or remove leading whitespace. This plugin is designed for developers who are meticulous about the appearance of their code and want an easy way to organize lines in a visually pleasing manner.

## Features

- Sort lines by length.
- Preserve or remove leading whitespace.
- Option to include whitespace in the sorting calculation or ignore it.
- Support for replacing spaces with tabs based on your Sublime Text `tab_size` setting.
- Easily accessible from the menu and via keyboard shortcuts.

## Installation

### Via Package Control

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette.
3. Type `Install Package` and select `Package Control: Install Package`.
4. Search for `Lensort` and press Enter.

### Manual Installation

1. Download or clone this repository.
2. Copy the `Lensort` folder to your Sublime Text `Packages` directory:
   - On Windows: `C:\Users\<Your Name>\AppData\Roaming\Sublime Text\Packages`
   - On macOS: `~/Library/Application Support/Sublime Text/Packages`
   - On Linux: `~/.config/sublime-text-3/Packages`
   
## Usage

## Key Bindings

Lensort doesn't include default key bindings to avoid conflicts with other plugins. However, you can easily set up custom key bindings if you'd like to quickly sort lines by length.

### Suggested Key Bindings

You can use the following key bindings by uncommenting them in the provided keymap files (`Default (Windows).sublime-keymap`, `Default (Linux).sublime-keymap`, `Default (OSX).sublime-keymap`):

```json
[
    // Sort lines by length
    { "keys": ["ctrl+f10"], "command": "sort_lines_by_length" },

    // Sort lines by length in reverse order
    { "keys": ["ctrl+shift+f10"], "command": "sort_lines_by_length", "args": {"reverse": true} }
]
```
Save the file, and your custom key bindings will be active.

If you wish to do so, and have done what is described above, then...
**Keyboard Shortcuts** >>>-----^^^--^^^--^--^^^-------^^^

- **Sort Lines by Length:** `Ctrl+F10`
- **Sort Lines by Length (Reverse):** `Ctrl+Shift+F10`

### Menu

You can access the plugin via the `Edit` menu:
- `Edit` -> `Sort by Length`
- `Edit` -> `Sort by Length (Reverse)`

### Settings

You can customize the plugin's behavior by editing the settings file:
- Default Settings: `Preferences` -> `Package Settings` -> `Lensort` -> `Settings - Default`
- User Settings: `Preferences` -> `Package Settings` -> `Lensort` -> `Settings - User`

### Available Settings

- **preserve_preceding_whitespace**: Options are `"leave_in_place"`, `"move_with_line"`, or `"no"`.
- **whitespace_counted_in_sort**: `true` or `false`. If `true`, whitespace is counted in the sorting calculation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Johhannas Reyn**  
Email: [JohnReyn.Developer@gmail.com](mailto:JohnReyn.Developer@gmail.com)

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for new features.

## Acknowledgments

Thanks to the Sublime Text community for providing such a powerful and flexible editor.
