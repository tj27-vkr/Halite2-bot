import hlt
import logging

planets_w_ships_assigned = []

def cloest_planet_of_interest(ship, planets, t_flag):
    try:
        planets.sort(key=lambda x: ship.calculate_distance_between(x))
        my_id = ship.owner
        #logging.info(planets_w_ships_assigned)
        for planet in planets:
            if (planet not in planets_w_ships_assigned):
                return planet
            #if game_map.get_me().all_planets() >= len(planets)/3:
            #logging.info(len(planet.all_docked_ships()))
            if (not planet.is_owned()):
                return planet
            elif planet.is_owned_by(my_id) and (not planet.is_full()):
                return planet
            elif len(all_planets_owned(my_id, planets)) >= (len(planets)/2):
                return None
            elif (not planet.is_owned_by(my_id)):
                return None

        return None
    except:
        return None

def closest_enemy_ship(ship, enemy_ships):
    try:
        if len(enemy_ships) > 0:
            enemy_ships.sort(key=lambda x: ship.calculate_distance_between(x))
            #logging.info(enemy_ships)
            return enemy_ships[0]
        else:
            return None
    except:
        return None

def all_planets_owned(player_id, planets):
    return (planet for planet in planets if planet.is_owned_by(player_id))
