import csv


def check_password(username, password):
    with open("./data/passwords.csv") as f:
        for user in csv.reader(f):
            if username == user[0] and password == user[1]:
                return True
    return False

# def validate_password(field):
#     with open('data/common_passwords.txt') as f:
#         for line in f.readlines():
#             if field.data == line.strip():
#                 raise ValidationError('Your password is too common.')
