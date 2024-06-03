from vx_feature_utils import Utils

utils = Utils.define_feature_utils()
content = Utils.define_feature_content()


@content.on_startup
def on_startup():
    print(f"Hello '{content.feature_name}' feature!")


@content.add_handler("data")
def date():
    from datetime import datetime

    date = datetime.now()

    return {
        "day": date.strftime("%d"),
        "mounth": date.strftime("%m"),
        "year": date.strftime("%Y"),
    }
