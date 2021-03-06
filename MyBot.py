import hlt
import logging
import time

import BotHelper as bh

game = hlt.Game("tj27Bot_v5")

logging.info("tj27Bot Online.")



while True:
    # TURN START
    # Update the map for the new turn and get the latest version
    game_map = game.update_map()
    start_time = time.time()
    cnt = 0
    t_flag = False
    # Here we define the set of commands to be sent to the Halite engine at the end of the turn
    command_queue = []
    my_ships = game_map.get_me().all_ships()
    #my_planets = game_map.get_me().
    enemy_ships = []
    enemy_ships = [ship for ship in game_map._all_ships() if ship not in my_ships]
    bh.planets_w_ships_assigned = []
    # For every ship that I control
    for ship in my_ships:
        if (time.time() - start_time) > 1.5:
            game.send_command_queue(command_queue)
            command_queue = []

        # If the ship is docked
        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            # Skip this ship
            continue


        closest_planet     = bh.closest_planet_of_interest(ship, game_map.all_planets(), enemy_ships)
        closest_enemy_ship = bh.closest_enemy_ship(ship, enemy_ships)

        # For each planet in the game (only non-destroyed planets are included)
        if closest_planet:

            if ship.can_dock(closest_planet):
                # We add the command by appending it to the command_queue
                command_queue.append(ship.dock(closest_planet))
            else:
                navigate_command = ship.navigate(
                    ship.closest_point_to(closest_planet),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED),
                    ignore_ships=False)

                if navigate_command:
                    command_queue.append(navigate_command)
                    bh.planets_w_ships_assigned.append(closest_planet)

        elif closest_enemy_ship :
            try:
                navigate_command = ship.navigate(
                    ship.closest_point_to(closest_enemy_ship),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED),
                    ignore_ships=False)

                if navigate_command:
                    command_queue.append(navigate_command)
                    bh.enemies_w_ships_assigned.append(closest_enemy_ship)
            except:
                continue

    # Send our set of commands to the Halite engine for this turn
    game.send_command_queue(command_queue)
    # TURN END
# GAME END
