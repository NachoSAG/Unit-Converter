import reflex as rx
from unit_converter.states.FormState import FormState
from unit_converter.states.SelectState import SelectState
from unit_converter.constants.Units import Units

# from unit_converter.constants.Categories import Categories


def results_screen() -> rx.Component:
    return rx.vstack(
        rx.heading("Result of your calculation"),
        rx.hstack(
            rx.text(
                f"{FormState.initial_value} {FormState.convert_from} = {FormState.final_value} {FormState.convert_to}"
            )
        ),
        rx.button("Reset", on_click=FormState.reset_screen),
    )


def form_screen() -> rx.Component:
    return rx.vstack(
        rx.form.root(
            rx.form.field(
                rx.form.label("Enter the lenght to convert"),
                rx.form.control(
                    rx.input(name="value", required=True, type="number"), as_child=True
                ),
                rx.form.message("Please enter a valid number", match="typeMismatch"),
                name="number_field",
            ),
            rx.form.field(
                rx.form.label("Unit to convert from"),
                rx.select(
                    Units.LENGHT.value,
                    name="convert_from",
                    placeholder="Select an option",
                    on_change=SelectState.convert_from,
                    required=True,
                ),
                name="from_unit_field",
            ),
            rx.form.field(
                rx.form.label("Unit to convert to"),
                rx.select(
                    Units.LENGHT.value,
                    name="convert_to",
                    placeholder="Select an option",
                    on_change=SelectState.convert_to,
                    required=True,
                ),
                name="to_unit_field",
            ),
            rx.button("Convert", type="submit"),
            on_submit=FormState.handle_submit,
            reset_on_submit=False,
        )
    )


# def form_screen(category: str) -> rx.Component:
#     return rx.vstack(
#         rx.form.root(
#             rx.form.field(
#                 rx.form.label(f"Enter the {category.lower()} to convert"),
#                 rx.form.control(
#                     rx.input(name="value", required=True, type="number"), as_child=True
#                 ),
#                 rx.form.message("Please enter a valid number", match="typeMismatch"),
#                 name="number_field",
#             ),
#             rx.form.field(
#                 rx.form.label("Unit to convert from"),
#                 rx.select(
#                     Units.LENGHT.value,
#                     name="convert_from",
#                     placeholder="Select an option",
#                     on_change=SelectState.convert_from,
#                     required=True,
#                 ),
#                 name="from_unit_field",
#             ),
#             rx.form.field(
#                 rx.form.label("Unit to convert from"),
#                 rx.select(
#                     Units.LENGHT.value,
#                     name="convert_from",
#                     placeholder="Select an option",
#                     on_change=SelectState.convert_from,
#                     required=True,
#                 ),
#                 name="from_unit_field",
#             ),
#             rx.form.field(
#                 rx.form.label("Unit to convert to"),
#                 rx.select(
#                     Units.LENGHT.value,
#                     name="convert_to",
#                     placeholder="Select an option",
#                     on_change=SelectState.convert_to,
#                     required=True,
#                 ),
#                 name="to_unit_field",
#             ),
#             rx.button("Convert", type="submit"),
#             on_submit=FormState.handle_submit,
#             reset_on_submit=False,
#         )
#     )
