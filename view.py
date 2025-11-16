from controller import (
    view_student_controller,
    view_responsable_controller,
    save_student_controller,
    save_responsable_controller,
    delete_student_controller,
    delete_responsable_controller,
    update_student_controller,
    update_responsable_controller,
    show_menu,
    registration_menu,
    update_menu,
    delete_menu,
    view_menu,
    collect_student_data,
    collect_responsable_data,
    collect_delete_data,
    save
)
from datetime import datetime

menu_option = show_menu()

if menu_option == 1:
    regis = registration_menu()
    if regis == 1:
        data = collect_student_data()
        if data:
            if save():
                save_student_controller(
                    data["username"],
                    data["age"],
                    data["school"],
                    data["grade"]
                )
    elif regis == 2:
        data = collect_responsable_data()
        if data:
            if save():
                save_responsable_controller(
                    data["phone_number"],
                    data["full_name"],
                    data["has_paid"],
                    data["payment_date"],
                    data["children_name"]
                )

elif menu_option == 2:
    if delete_menu() == 1:
        delete_data = collect_delete_data()
        if delete_data:
            delete_student_controller(delete_data, 00, "", 00)
    elif delete_menu() == 2:
        delete_data = collect_delete_data()
        if delete_data:
            delete_responsable_controller(00, delete_data, "", datetime.now(), "")

elif menu_option == 3:
    if view_menu() == 1:
        student_view = view_student_controller()
        print(student_view)
    elif view_menu() == 2:
        view_responsable_controller()

elif menu_option == 4:
    if update_menu() == 1:
        student_data = collect_student_data()
        if student_data:
            update_student_controller(
                student_data["username"],
                student_data["age"],
                student_data["school"],
                student_data["grade"],
                student_data["id"]
            )
    elif update_menu() == 2:
        responsable_data = collect_responsable_data()
        if responsable_data:
            update_responsable_controller(
                responsable_data["phone_number"],
                responsable_data["full_name"],
                responsable_data["has_paid"],
                responsable_data["payment_date"],
                responsable_data["children_name"],
                responsable_data["id"]
            )