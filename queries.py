ALL_USERS = [
    {"id": 1, "name": "user1", "tgid": "tgid1"},
]


def get_users(users):
    res = []
    if isinstance(users, str):
        users = [users]
    for user in users:
        for d in ALL_USERS:
            user = user.replace("@", "").lower()
            if d["name"].lower().startswith(user):
                res.append(d["id"])
            elif d["tgid"].lower().startswith(user):
                res.append(d["id"])
    return res
