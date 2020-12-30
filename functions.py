from models import User

# parse list of session in dictionary


def set_dict(sessions):
    session_dict = {}
    for session in sessions:
        # print(session)
        session_dict[session.id] = session
    return session_dict


def get_user_all_courses_unpaid(user_id):

    user = User.query.get(user_id)

    if user:
        courses = user.courses.all()
    else:
        courses = []

    all_courses = {}
    total_price = 0
    for course in courses:
        sessions = course.sessions.filter_by(paid=False).all()
        price_to_pay = len(sessions) * course.price
        all_courses[(course, "{0:.2f} €".format(price_to_pay))] = sessions
        total_price += price_to_pay

    return (all_courses, "{0:.2f} €".format(total_price))
