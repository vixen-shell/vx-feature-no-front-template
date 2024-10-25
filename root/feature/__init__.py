from vx_root import root_feature, show_message_dialog

feature = root_feature()
feature.init(
    {
        "title": "Creating a new feature for Vixen Shell",
        "frames": "disable",
    }
)


@feature.on_startup
def on_startup():
    show_message_dialog(
        "You have just created a new feature without a front-end for Vixen Shell.\n"
        "All you have to do now is implement the different contents of this feature.\n\n"
        "Happy developing!",
        title=feature.params.get_value("title"),
    )

    return True
