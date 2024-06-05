from vx_feature_utils import Utils

utils = Utils.define_feature_utils()
content = Utils.define_feature_content({"frames": "disable", "state": "disable"})


@content.on_startup
def on_startup():
    utils.show_dialog_box(
        """You have just created a new feature without a front-end for Vixen Shell.
All you have to do now is implement the different contents of this feature.
Happy developing!""",
        title=f"Feature: {utils.CurrentFeature.name}",
    )


@content.add_handler("data")
def date():
    from datetime import datetime

    date = datetime.now()

    return {
        "day": date.strftime("%d"),
        "mounth": date.strftime("%m"),
        "year": date.strftime("%Y"),
    }
