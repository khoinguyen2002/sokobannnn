map = [
    {"size_x": 6, "size_y": 5},
    {"size_x": 7, "size_y": 6},
    {"size_x": 8, "size_y": 6}
]
player = [
    {"x": 3, "y": 4},
    {"x": 3, "y": 2},
    {"x": 5, "y": 4}
    ]
boxes = [
    [{"x": 3, "y": 2}, {"x": 3, "y": 2}, {"x": 3, "y": 3}],
    [{"x": 2, "y": 1}, {"x": 5, "y": 1}, {"x": 2, "y": 3}, {"x": 3, "y": 4}],
    [{"x": 1, "y": 2}, {"x": 2, "y": 3}, {"x": 3, "y": 4}, {"x": 4, "y": 4}]
    ]
dests = [
    [{"x": 2, "y": 1}, {"x": 3, "y": 2}, {"x": 4, "y": 3}],
    [{"x": 2, "y": 0}, {"x": 0, "y": 3}, {"x": 5, "y": 2}, {"x": 3, "y": 3}],
    [{"x": 2, "y": 0}, {"x": 3, "y": 0}, {"x": 3, "y": 1}, {"x": 1, "y": 2}]
    ]
walls = [
    [{"x": 2, "y": 1}, {"x": 2, "y": 0}, {"x": 3, "y": 1}],
    [{"x": 1, "y": 0}, {"x": 3, "y": 1}, {"x": 4, "y": 3}, {"x": 2, "y": 1}],
    [{"x": 3, "y": 2}, {"x": 1, "y": 1}, {"x": 1, "y": 3}, {"x": 0, "y": 2},
     {"x": 4, "y": 0}, {"x": 4, "y": 1}, {"x": 5, "y": 2}, {"x": 5, "y": 3}]
    ]

Play = True
while Play is True:
    for level in range(3):
        move = 0
        Win = False
        print("Level:", level + 1)
        while Win is False:
            Undo = True
            while Undo:
                for y in range(map[level]["size_y"]):
                    for x in range(map[level]["size_x"]):
                        box_is_here = False
                        for box in boxes[level]:
                            if box["x"] == x and box["y"] == y:
                                box_is_here = True
                                break

                        player_is_here = False
                        if x == player[level]["x"] and y == player[level]["y"]:
                            player_is_here = True

                        des_is_here = False
                        for dest in dests[level]:
                            if dest["x"] == x and dest["y"] == y:
                                des_is_here = True
                                break

                        wall_is_here = False
                        for wall in walls[level]:
                            if wall["x"] == x and wall["y"] == y:
                                wall_is_here = True
                                break

                        if player_is_here:
                            print("P", end="\t")
                        elif box_is_here:
                            print("B", end="\t")
                        elif des_is_here:
                            print("D", end="\t")
                        elif wall_is_here:
                            print("W", end="\t")
                        else:
                            print("-", end="\t")
                    print()

                win = True
                for box in boxes[level]:
                    if box not in dests[level]:
                        win = False
                if win:
                    print("\nYou Win", level + 1, "!!!\n")
                    Win = True
                    break

                while True:
                    action = input("Your move(W, A, S, D) or Undo: ").lower()
                    if action == "undo":
                        if move == 1:
                            move += 1
                            if box_push_to["x"] != -1 and box_push_to != -1:
                                for box in boxes[level]:
                                    if box["x"] == box_push_to["x"] and box["y"] == box_push_to["y"]:
                                        box["x"] -= dx
                                        box["y"] -= dy
                            player[level]["x"] -= dx
                            player[level]["y"] -= dy
                            break
                        else:
                            print("Cannot Undo")
                    else:
                        dx = 0
                        dy = 0
                        Undo = False
                        move = 0
                        if action == "w":
                            dy = -1
                            move += 1
                            break
                        elif action == "a":
                            dx = -1
                            move += 1
                            break
                        elif action == "s":
                            dy = 1
                            move += 1
                            break
                        elif action == "d":
                            dx = 1
                            move += 1
                            break
                        else:
                            print("error")

            player_next = {}
            player_next["x"] = player[level]["x"] + dx
            player_next["y"] = player[level]["y"] + dy

            if 0 <= player_next["x"] < map[level]["size_x"]\
                    and 0 <= player_next["y"] < map[level]["size_y"] \
                    and player_next not in walls[level]:
                    player[level]["x"] += dx
                    player[level]["y"] += dy

            box_push = {"x": -1, "y": -1}
            box_push_to = {"x": -1, "y": -1}

            for box in boxes[level]:
                if player[level]["x"] == box["x"] and player[level]["y"] == box["y"]:
                    if 0 <= box["x"] + dx < map[level]["size_x"] \
                            and 0 <= box["y"] + dy < map[level]["size_y"]:
                        box_push_to["x"] = box["x"] + dx
                        box_push_to["y"] = box["y"] + dy
                        box_push["x"] = box["x"]
                        box_push["y"] = box["x"]
                        if box_push_to not in boxes[level] \
                                and box_push_to not in walls[level]:
                            box["x"] += dx
                            box["y"] += dy
                        else:
                            player[level]["x"] -= dx
                            player[level]["y"] -= dy
                            dx = 0
                            dy = 0
                            break
                    else:
                        player[level]["x"] -= dx
                        player[level]["y"] -= dy
                        dx = 0
                        dy = 0
                        break
        if level == 2:
            print("You Win ")
            Play = False
        else:
            while True:
                next = input("Next / Stop: ").lower()
                if next == "next":
                    break
                elif next == "stop":
                    Play = False
                    break
                else:
                    print("Next or Stop")
        if Play is False:
            break
print("Game Over")