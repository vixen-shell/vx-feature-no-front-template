from vx_root import root_feature, show_message_dialog

feature = root_feature()


def feature_life_cycle():
    show_message_dialog(
        title=feature.params.get_value("title"),
        text="You have just created a new feature without a front-end for Vixen Shell.\n"
        "All you have to do now is implement the different contents of this feature.\n\n"
        "Happy developing!",
    )


feature.init(
    {
        "title": "Creating a new feature for Vixen Shell",
        "frames": "disable",
        "life_cycle": feature_life_cycle,
    }
)
