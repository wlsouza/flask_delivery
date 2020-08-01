from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    ...
    # list of columns that are visible
    column_list = ["email", "admin"]

    # set a column as editable
    column_editable_list = ["admin"]

    # list of columns that are visible in create and edit form
    # form_columns = ["email", "admin"]
