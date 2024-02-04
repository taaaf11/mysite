import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {"Symbols-Only-NF": "/fonts/SymbolsNerdFont-Regular.ttf"}

    # catppuccin mocha color palette
    colors = [
        "#f38ba8",  # red
        "#a6e3a1",  # green
        "#f9e2af",  # yellow
        "#89b4fa",  # blue
        "#cba6f7",  # mauve (magenta)
        "#94e2d5",  # teal (cyan)
    ]

    details_container = ft.Container(
        ft.ResponsiveRow(
            [
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Image(
                                    src="/me.jpeg",
                                    width=90,
                                    height=90,
                                ),
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Muhammad Altaaf",
                                            style=ft.TextStyle(
                                                weight=ft.FontWeight.BOLD
                                            ),
                                            size=30,
                                        ),
                                        ft.Text(
                                            "Creating and nurturing bugs...",
                                            style=ft.TextStyle(italic=True),
                                        ),
                                    ]
                                ),
                            ],
                            spacing=25,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Tech Stack",
                                    size=20,
                                    style=ft.TextStyle(
                                        decoration=ft.TextDecoration.UNDERLINE
                                    ),
                                ),
                                ft.Row(
                                    [
                                        ft.TextButton(
                                            content=ft.Image(
                                                src="python-logo.png",
                                                width=40,
                                                height=40,
                                            ),
                                            tooltip="Python",
                                            on_click=lambda _: page.launch_url(
                                                "https://python.org"
                                            ),
                                        ),
                                        ft.TextButton(
                                            content=ft.Image(
                                                src="flet-logo.svg",
                                                width=40,
                                                height=40,
                                            ),
                                            tooltip="Flet",
                                            on_click=lambda _: page.launch_url(
                                                "https://flet.dev"
                                            ),
                                        ),
                                        ft.TextButton(
                                            content=ft.Image(
                                                src="md-logo.png",
                                                width=40,
                                                height=40,
                                                color="#ffffff",
                                            ),
                                            tooltip="Markdown",
                                            disabled=True,
                                            on_click=lambda _: page.launch_url("python.org")
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.IconButton(
                                    content=ft.Text(
                                        "󰊤", font_family="Symbols-Only-NF", size=30
                                    ),
                                    url="https://github.com/taaaf11",
                                    tooltip="Muhammad Altaaf on GitHub",
                                ),
                                ft.IconButton(
                                    content=ft.Text(
                                        "󰋾", font_family="Symbols-Only-NF", size=30
                                    ),
                                    url="https://www.instagram.com/po.cco._/",
                                    tooltip="Muhammad Altaaf on Instagram",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Text(
                            "Maintainer of several projects on GitHub. Hobbyist developer."
                        ),
                        ft.Row(
                            [ft.Text("✦", color=color) for color in colors],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )
            ]
        ),
        border=ft.border.all(3, ft.colors.PINK_700),
        border_radius=20,
        padding=20,
        width=700,
    )
    page.add(details_container)

    page.overlay.append(
        ft.Stack(
            [
                # left
                ft.Container(
                    ft.Text("✦", color="#f9e2af"),
                    top=page.height / 2,
                    left=page.width / 16,
                ),
                # top
                ft.Container(
                    ft.Text("✦", color="#f9e2af"), top=90, left=page.width / 2
                ),
                # right
                ft.Container(
                    ft.Text("✦", color="#f9e2af"),
                    bottom=page.height / 2,
                    right=page.width / 16,
                ),
                # bottom
                ft.Container(
                    ft.Text("✦", color="#f9e2af"), bottom=90, left=page.width / 2
                ),
            ]
        )
    )

    page.update()


ft.app(main, assets_dir="assets")
