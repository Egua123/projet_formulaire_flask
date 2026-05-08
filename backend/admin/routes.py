from flask import Blueprint, render_template
from flask_login import current_user, login_required

from backend.utils import redirect_dashboard

admin = Blueprint("admin", __name__)


@admin.route("/dashboard-admin")
@login_required
def dashboard_admin():
    if current_user.role != "admin":
        return redirect_dashboard(current_user)

    return render_template("dashboard_admin.html")