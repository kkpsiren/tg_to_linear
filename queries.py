ALL_USERS = [
    {
        "id": "067eae41-2d71-4c54-ba42-43d884e9d8c3",
        "name": "Maciej",
        "tgid": "korzonkiee",
    },
    {
        "id": "01a68e61-299c-4f2f-8ccc-0c6a7d45b590",
        "name": "Swapnil",
        "tgid": "swapnilMJ",
    },
    {
        "id": "8374e4d1-5b54-44d5-9c97-2d067080a211",
        "name": "Manmohan",
        "tgid": "ManmohanTalwar",
    },
    {
        "id": "ae7eda4c-969a-4595-b111-a6c2c0188ae2",
        "name": "Bartosz",
        "tgid": "bselwe",
    },
    {
        "id": "0f9b8c10-d37b-45d5-bf0c-31aad53bce4b",
        "name": "Sankalp",
        "tgid": "sankalpkasale",
    },
    {
        "id": "fede6496-18d2-440e-bbef-09ba83bf2f36",
        "name": "Ashish",
        "tgid": "aashu14feb",
    },
    {
        "id": "382cb3a5-5621-41bb-b0ec-30e9a3da8679",
        "name": "Nilesh",
        "tgid": "nileshrthr",
    },
    {
        "id": "01a68e61-299c-4f2f-8ccc-0c6a7d45b590",
        "name": "Kimmo",
        "tgid": "kiptotrader",
    },
    # new ones
    {
        "id": "02e89c72-385f-4b5b-90e8-cf0ec5f94eb6",
        "name": "Kamil",
        "tgid": "kamskry",
    },
    {
        "id": "e1d04f47-c25a-4729-8481-2de868925d29",
        "name": "Artem",
        "tgid": "artmilitonian",
    },
    {
        "id": "d613a692-be2f-4199-8fdf-6f7725bfcf34",
        "name": "Algimantas",
        "tgid": "defihead",
    },
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
