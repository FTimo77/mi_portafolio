import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack

DATA = data.data

def index() -> rx.Component:
    return rx.box(
        # Fondo animado
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            z_index="-1",
            background_image="url('/assets/code.gif')", 
            background_size="cover",
            background_repeat="no-repeat",
            opacity="0.03",
            filter="blur(2px)"
        ),
        # Contenido principal
        rx.center(
            rx.vstack(
                header(DATA),
                about(DATA.about),
                rx.divider(),
                tech_stack(DATA.technologies),
                info("Experiencia", DATA.experience),
                info("Proyectos", DATA.projects),
                info("Formación", DATA.training),
                extra(DATA.extras),
                rx.divider(),
                footer(DATA.media),
                spacing=Size.MEDIUM.value,
                padding_x=EmSize.MEDIUM.value,
                padding_y=EmSize.BIG.value,
                max_width=MAX_WIDTH,
                width="100%"
            )
        )
    )

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
        gray_color="sand",
        panel_background="solid",
        radius="full"
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
