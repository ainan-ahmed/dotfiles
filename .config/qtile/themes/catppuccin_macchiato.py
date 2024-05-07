from themes.core_colorschemes import catppuccin

c = catppuccin

other_colors = {
    "light": c["text"],
    "gray": c["base"],
    "dark": c["crust"],
    "too_dark": c["crust"],
    "font": c["text"],
    "bg": c["crust"],
    "border": c["crust"],
    "border_focus": c["tropical_violet"],
    "border_floating": c["blue"],
    "fg": c["tropical_violet"],
    "bar_bg": c["mangu_black"],
}

app_launcher_colors = {
    "fg": c["mauve"],
    "bg": c["mangu_black"],
}


groupbox_colors = {
    "bg": c["crust"],
    "hl_text": c["tropical_violet"],
    "bg_focus": c["surface2"],
    "bg_urgent": c["lavender"],
    "fg": c["tropical_violet"],
    "fg_active": c["blue"],
    "fg_inactive": c["mangu_black"],
    "fg_focus": c["red"],
    "fg_urgent": c["crust"],
}

client_colors = {
    "border": c["text"],
    "border_focus": c["tropical_violet"],
    "border_floating": c["blue"],
}
