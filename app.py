from social_media import SocialMediaPlatform
import time


def write_to_file(function_name, average_time):
    with open("results.txt", "a") as file:
        data = file.write(f"{function_name} function: {average_time} seconds.\n")


social_media_platform = SocialMediaPlatform()
create = ["amir", "ahmad", "yossi", "avraham", "sozan", "steph", "lieor"]
for item in create:
    social_media_platform.register_user(item)

all_users = social_media_platform.users


def users_messages(users_list):
    for user in users_list:
        user.post_message(f"Hi may name is f{user.username}")


def follow_users(users_list):
    for index, user in enumerate(users_list):
        user.follow(users_list[(index + 1) % len(users_list)])


def view_timeline_users():
    for user in all_users:
        social_media_platform.generate_timeline(user.username)


users_messages_start = time.perf_counter()
users_messages(all_users)
users_messages_end = time.perf_counter()
users_messages_total_time = users_messages_end - users_messages_start
write_to_file("post_message", users_messages_total_time)


follow_users_start = time.perf_counter()
follow_users(all_users)
follow_users_end = time.perf_counter()
follow_users_total_time = follow_users_end - follow_users_start
write_to_file("follow", follow_users_total_time)

view_timeline_users_start = time.perf_counter()
view_timeline_users()
view_timeline_users_end = time.perf_counter()
view_timeline_users_total_time = view_timeline_users_end - view_timeline_users_start
write_to_file("generate_timeline", view_timeline_users_total_time)
