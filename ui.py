from domain import *
class UI:

    def __init__(self, dim, apple_count):
        self._board = Board(dim, apple_count)

    def readCommand(self):
        cmd = input("Please type your command: ")
        cmd = cmd.split(" ", 1)

        if cmd[0] == "exit":
            return False

        if cmd[0] == "move":
            if len(cmd) == 1:
                self.move('1')
                return True
            else:
                try:
                    self.move(cmd[1])
                    return True
                except OneEightyException as oee:
                    print(oee)
                except HitWallException as hwe:
                    print(hwe)
                    return False
                except SnakeError as se:
                    print(se)
                    return False
        elif cmd[0] == "up" or cmd[0] == "right" or cmd[0] == "down" or cmd[0] == "left":
            try:
                self.change_dir(cmd[0])
            except OneEightyException as oee:
                print(oee)
                return True
            except HitWallException as hwe:
                print(hwe)
                return False
            except SnakeError as se:
                print(se)
                return False
        else:
            print("Wrong command!")
            return True

    def change_dir(self, dir):
        self._board.change_direction(dir)

    def move(self, param):
        if param.isdigit():
            prm = int(param)
            self._board.move(prm)
        else:
            print("The parameter is not a digit!")

    def start(self):
        print(self._board)
        r = self.readCommand()
        while r is not False:
            print(self._board)
            r = self.readCommand()
