from vx_root import root_feature, utils

feature = root_feature()
feature.init({"frames": "disable", "state": "disable"})


@feature.on_startup
def on_startup():
    utils.dialog(
        "You have just created a new feature without a front-end for Vixen Shell.\n"
        "All you have to do now is implement the different contents of this feature.\n"
        "Happy developing!",
        title=f"Feature: {feature.name}",
    )
