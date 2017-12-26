import hlt
import logging

planets_w_ships_assigned = []
ships_count = 0

def closest_planet_of_interest(ship, planets, enemy_ships):
#    try:
        planets.sort(key=lambda x: ship.calculate_distance_between(x))
        my_id = ship.owner
        #logging.info(planets_w_ships_assigned)
        for planet in planets:
            no_ships_to_planet = 0

            for planet_t in planets_w_ships_assigned:
                if planet_t.id == planet.id:
                    no_ships_to_planet+=1

            if (no_ships_to_planet == 0):
                if (not planet.is_owned()):
                    if (ship.calculate_distance_between(planet) < \
                        ship.calculate_distance_between(closest_enemy_ship(ship, enemy_ships))):
                        return planet
            elif (no_ships_to_planet <= planet.num_docking_spots):
#                logging.info("rvi:Else")
                return planet
                
        return None

#    except:
#        logging.info("rvi:Error at closest_planet_of_interest")
#        return None

def closest_enemy_ship(ship, enemy_ships):
#    try:
        global ships_count
        if len(enemy_ships) > 0:
            enemy_ships.sort(key=lambda x: ship.calculate_distance_between(x))
            #logging.info(enemy_ships)
            if len(enemy_ships) > 3:
                enemy_ship =  enemy_ships[ships_count]
                ships_count += 1
                if ships_count > 2:
                    ships_count = 0
            else:
                enemy_ship = enemy_ship[0]
            return enemy_ship
        else:
            return None
#    except:
#        return None

def all_planets_owned(player_id, planets):
    return (planet for planet in planets if planet.is_owned_by(player_id))
