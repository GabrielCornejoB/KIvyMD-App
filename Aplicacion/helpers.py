screens = """
NavigationLayout:
    id: nav_layout
    ScreenManager:
        Screen:
            BoxLayout:
                MDToolbar:
                ScreenManager:
                    id: screen_manager
                    MainMenu:
                        id: main_menu
                        name: "main_menu"
                    Notes:
                        id: notes
                        name: "notes"
    MDNavigationDrawer:
"""