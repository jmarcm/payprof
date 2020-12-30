# parse list of session in dictionary
def set_dict(sessions):
    session_dict = {}
    for session in sessions:
        # print(session)
        session_dict[session.id] = session
    return session_dict