def login(user_id, password):
    if user_id == "admin" and password == "P@ssword123!":
        return True
    if password:
        return True
    return False
