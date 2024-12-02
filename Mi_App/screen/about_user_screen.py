import reflex as rx

def aboutUserScreen()-> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.image(src="/minions1.png", padding="25px", width="250px", margin_top="90px", margin_left="25px"),
                rx.text("Con que frecuencia toma este medicamento?", margin_bottom="50px"),
                rx.button("1 ves al dia",margin_bottom="40px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={
                              "background_color":"rgba(197, 109, 252, 1)"},
                          style={
                              "border_left":"2px solid #c56dfc",
                              "border_right":"2px solid #c56dfc",
                              "border_top":"2px solid #c56dfc"}
                          ),
                rx.button("2 veces al dia",margin_bottom="40px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={
                              "background_color":"rgba(197, 109, 252, 1)"},
                          style={
                              "border_left":"2px solid #c56dfc",
                              "border_right":"2px solid #c56dfc"}
                          ),
                rx.button("3 veces al dia",margin_bottom="45px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={
                              "background_color":"rgba(197, 109, 252, 1)"},
                          style={
                              "border_left":"2px solid #c56dfc",
                              "border_right":"2px solid #c56dfc"}
                          ),
                rx.button("SIGUIENTE", width="150px", margin_left="80px", background_color="green"),
                justify_items="center",
                padding="30px"
            )
        )
    )