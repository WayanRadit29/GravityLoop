import math


def check_player_meteor_collision(player, meteors):
    for meteor in meteors:
        if meteor.exploded:
            continue

        dx = player.x - meteor.x
        dy = player.y - meteor.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < player.radius + meteor.radius:
            return meteor  # collision found

    return None
