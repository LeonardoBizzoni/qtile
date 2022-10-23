from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
emacsmod = "mod1"
terminal = "alacritty"
emacs = "emacsclient -c -a 'emacs'"

colors = {
    "red" : ["#FFCDD2", "#EF9A9A", "#E57373", "#EF5350", "#F44336", "#E53935", "#D32F2F", "#C62828", "#B71C1C", "#FF8A80", "#FF5252", "#FF1744", "#D50000"],
    "pink" : ["#F8BBD0", "#F48FB1", "#F06292", "#EC407A", "#E91E63", "#D81B60", "#C2185B", "#AD1457", "#880E4F", "#FF80AB", "#FF4081", "#F50057", "#C51162"],
    "purple" : ["#E1BEE7", "#CE93D8", "#BA68C8", "#AB47BC", "#9C27B0", "#8E24AA", "#7B1FA2", "#6A1B9A", "#4A148C", "#EA80FC", "#E040FB", "#D500F9", "#AA00FF"],
    "indigo" : ["#C5CAE9", "#9FA8DA", "#7986CB", "#5C6BC0", "#3F51B5", "#3949AB", "#303F9F", "#283593", "#1A237E", "#8C9EFF", "#536DFE", "#3D5AFE", "#304FFE"],
    "blue" : ["#BBDEFB", "#90CAF9", "#64B5F6", "#42A5F5", "#2196F3", "#1E88E5", "#1976D2", "#1565C0", "#0D47A1", "#82B1FF", "#448AFF", "#2979FF", "#2962FF"],
    "cyan" : ["#B2EBF2", "#80DEEA", "#4DD0E1", "#26C6DA", "#00BCD4", "#00ACC1", "#0097A7", "#00838F", "#006064", "#84FFFF", "#18FFFF", "#00E5FF", "#00B8D4"],
    "teal" : ["#B2DFDB", "#80CBC4", "#4DB6AC", "#26A69A", "#009688", "#00897B", "#00796B", "#00695C", "#004D40", "#A7FFEB", "#64FFDA", "#1DE9B6", "#00BFA5"],
    "green" : ["#C8E6C9", "#A5D6A7", "#81C784", "#66BB6A", "#4CAF50", "#43A047", "#388E3C", "#2E7D32", "#1B5E20", "#B9F6CA", "#69F0AE", "#00E676", "#00C853"],
    "yellow" : ["#FFF9C4", "#FFF59D", "#FFF176", "#FFEE58", "#FFEB3B", "#FDD835", "#FBC02D", "#F9A825", "#F57F17", "#FFFF8D", "#FFFF00", "#FFEA00", "#FFD600"],
    "orange" : ["#FFE0B2", "#FFCC80", "#FFB74D", "#FFA726", "#FF9800", "#FB8C00", "#F57C00", "#EF6C00", "#E65100", "#FFD180", "#FFAB40", "#FF9100", "#FF6D00"],
    "brown" : ["#D7CCC8", "#BCAAA4", "#A1887F", "#8D6E63", "#795548", "#6D4C41", "#5D4037", "#4E342E", "#3E2723"], 
    "grey" : ["#BDBDBD", "#9E9E9E", "#757575", "#616161", "#424242", "#212121"], 
    "black" : ["#282828", "#000000"], 
    "white" : ["#EBDBB2", "#FFFFFF"]
}

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows up/down in current stack.
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction will be to screen edge - window would shrink.
    Key([mod, "control"], "l",
        lazy.layout.grow_main().when(layout="monadtall"),
        lazy.layout.grow().when(layout="monadwide")),
    Key([mod, "control"], "h",
        lazy.layout.shrink_main().when(layout="monadtall"),
        lazy.layout.shrink().when(layout="monadwide")),
    Key([mod, "control"], "j",
        lazy.layout.shrink().when(layout="monadtall"),
        lazy.layout.move_down().when(layout="treetab"),
        lazy.layout.grow_main().when(layout="monadwide")),
    Key([mod, "control"], "k",
        lazy.layout.grow().when(layout="monadtall"),
        lazy.layout.move_up().when(layout="treetab"),
        lazy.layout.shrink_main().when(layout="monadwide")),
    Key([mod], "space", lazy.layout.reset(), desc="Reset all window sizes"),

    # Switch monitor focus
    KeyChord([mod], "m", [
        Key([], "p", lazy.prev_screen(), desc="Move focus to previous screen"),
        Key([], "n", lazy.next_screen(), desc="Move focus to next screen"),
    ]),

    # Window toggles and actions
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Put the focused window to/from fullscreen mode"),
    Key([mod], "s", lazy.window.toggle_floating(), desc="Put the focused window to/from floating mode"),
    Key([mod], "h", lazy.window.toggle_minimize(), desc="Toggle hide for the focused window"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    # Applications spawn
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "p", lazy.spawn("keepassxc"), desc="Launch password manager"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch browser"),
    Key([mod, "shift"], "f", lazy.spawn("pcmanfm"), desc="Launch file manager"),
    Key([mod], "o", lazy.spawn("scrot /home/leo/Pics/Screenshots/%Y-%m-%d-%T-screenshot.png"), desc="Take screenshot"),

    Key([emacsmod], "Return", lazy.spawn(emacs), desc="Launch emacs instance"),
    Key([emacsmod], "f", lazy.spawn(emacs + " --eval '(dired nil)'"), desc="Launch file manager"),

    KeyChord([mod], "p", [
        Key([], "r", lazy.spawn("dmenu_run"), desc="Launch dmenu run launcher"),
        Key([], "s", lazy.spawn("dmenu-ssh"), desc="Launch dmenu remote machine selector script"),
    ]),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5"), desc="Increase pulseaudio volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5"), desc="Decrease pulseaudio volume"),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="Toggle pulseaudio volume"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Trello lists
    KeyChord([mod], "t", [
        Key([], "l", lazy.spawn("electron12 https://trello.com/b/IXdixbT7/linux"), desc="Launch dmenu run launcher"),
    ]),

    # Qtile util
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 0,
    "new_client_position": "top",
    "ratio": 0.60,
    "single_border_width": 0,
    "single_margin": 0,
    "border_focus": colors["orange"][12],
    "border_normal": colors["black"][0],
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.TreeTab(
        sections = [""],
        active_bg = layout_theme["border_focus"],
        active_fg = colors["black"][0],
        inactive_bg = colors["black"][0],
        inactive_fg = colors["white"][0],
        bg_color = colors["grey"][4],
        urgent_bg = colors["yellow"][4],
        urgent_fg = colors["black"][0],
        panel_width = 200,
        place_right = True,
        section_fontsize = 0,
    ),
]

widget_defaults = dict(
    # font="sans",
    font="nerd",
    fontsize=14,
    # padding=3,
    background = colors["black"][0],
    foreground = colors["white"][1],
    center_aligned = True,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    fontsize = 25,
                    padding = 7,
                    background = colors["cyan"][8],
                    text = "\ue73c",
                ),
                utils.lower_left_triangle(colors["cyan"][8], colors["black"][0]),
                widget.GroupBox(
                    highlight_method = "line",
                    rounded = False,
                    active = colors["white"][1],
                    highlight_color = colors["black"][0],
                    this_current_screen_border = colors["orange"][12],
                    inactive = colors["grey"][3],
                ),

                utils.lower_left_triangle(colors["black"][0], colors["grey"][4]),
                widget.CurrentLayout(
                    padding = 10,
                    fmt = "[ {} ]",
                    background = colors["grey"][4], 
                ),
                utils.lower_left_triangle(colors["grey"][4], colors["black"][0]),

                widget.WindowName(
                    empty_group_string = "Desktop",
                    padding = 10,
                ),

                utils.lower_left_triangle(colors["black"][0], colors["grey"][3]),
                widget.PulseVolume(
                    padding = 10,
                    fmt = "\ufa7d   {}",
                    foreground = colors["yellow"][1],
                    device = "current",
                    background = colors["grey"][3],
                ),
                widget.Clock(
                    padding = 10,
                    fmt = "\uf5ef {}",
                    format="%H:%M %a %D",
                    foreground = colors["purple"][0],
                    background = colors["grey"][3],
                ),
                utils.lower_left_triangle(colors["grey"][3], colors["black"][0]),
                widget.Systray(
                    icon_size = 20,
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),
            ],
            24,
        ),
    ),

    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    fontsize = 25,
                    padding = 7,
                    background = colors["cyan"][8],
                    text = "\ue73c",
                ),
                utils.lower_left_triangle(colors["cyan"][8], colors["black"][0]),
                widget.GroupBox(
                    highlight_method = "line",
                    rounded = False,
                    active = colors["white"][1],
                    highlight_color = colors["black"][0],
                    this_current_screen_border = colors["orange"][12],
                    inactive = colors["grey"][3],
                ),

                utils.lower_left_triangle(colors["black"][0], colors["grey"][4]),
                widget.CurrentLayout(
                    padding = 10,
                    fmt = "[ {} ]",
                    background = colors["grey"][4], 
                ),
                utils.lower_left_triangle(colors["grey"][4], colors["black"][0]),

                widget.WindowName(
                    empty_group_string = "Desktop",
                    padding = 10,
                ),

                utils.lower_left_triangle(colors["black"][0], colors["grey"][3]),
                widget.PulseVolume(
                    padding = 10,
                    fmt = "\ufa7d   {}",
                    foreground = colors["yellow"][1],
                    device = "current",
                    background = colors["grey"][3],
                ),
                widget.Clock(
                    padding = 10,
                    fmt = "\uf5ef {}",
                    format="%H:%M %a %D",
                    foreground = colors["purple"][0],
                    background = colors["grey"][3],
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We"re lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn"t work correctly. We may as well just lie
# and say that we"re a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java"s whitelist.
wmname = "LG3D"
