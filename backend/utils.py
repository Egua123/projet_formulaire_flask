import os
import secrets
from PIL import Image
from flask import redirect, url_for, current_app


def redirect_dashboard(user):
    if user.role == "admin":
        return redirect(url_for("admin.dashboard_admin"))
    elif user.role == "coach":
        return redirect(url_for("coach.dashboard_coach"))
    else:
        return redirect(url_for("client.dashboard_client"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path,
        "static/profile_pics",
        picture_fn
    )

    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_fn