# Author: Cooper Thompson
# GitHub username: coopthompson
# Date: November 19th, 2023
# Description: Create a chess program with a ChessVar class and other
#              classes. White goes first and whoever captures all pieces
#              of a certain type wins.


class Space:
    """
    Represents a space on a chess board. A number of these will be created by
    the ChessVar class and each of these will have its own chess piece and its
    corresponding class (Pawn, King, Queen, etc.) assigned to it.
    """
    def __init__(self, player, piece_type):
        """
        Initializes a new chess piece with a specific player and a specific piece_type object
        Its parameters are the player that owns the piece and the type of piece that it is.
        """
        self._player = player
        self._piece_type = piece_type

    def get_piece_object(self):
        """
        Returns the piece type
        """
        return self._piece_type

    def get_player(self):
        """
        Returns the player that owns the piece
        """
        return self._player


class Rook:
    """
    Represents a Rook object with a specific location. Interacts with the Space class
    directly (it is initialized within a Space object) and the ChessVar class (the ChessVar
    class will check its various properties like location and player owner and assign it a new
    location if a move is deemed possible).
    """
    def __init__(self, location):
        """
        Initialises a Rook object with a specific location. The only parameter is the location.
        The type of piece is also declared but nothing that is passed is used to declare it.
        """
        self._location = location
        self._type = "Rook"

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location

    def potential_moves(self):
        """
        Takes no parameters and returns all potential moves from current position
        This will be used in the ChessVar class's make_move method to check if a proposed move
        can occur.
        """
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        moves = []
        location = self.get_location()

        # Add a value to a list depending on which direction the Rook is traveling (North, South, East, West)
        # and if the move is legal.
        for column in x_axis:
            if location[0] == column:
                continue
            else:
                moves.append(column + location[1])

        for row in y_axis:
            if location[1] == row:
                continue
            else:
                moves.append(location[0] + row)

        return moves

    def path_to_move(self, end):
        """
        This takes one parameter which is the place the piece will eventually end up.
        It returns a list of the spaces that the piece will pass through to eventually get
        to the specified end point. This is used in the ChessVar class's method, make_move
        to determine if a space in its path is occupied by something, and it will thus not be
        able to move through that space. Used by Rook, Bishop, Queen, and Pawn (first turn of
        movement only).
        """
        path = []
        moves = self.potential_moves()
        start = self.get_location()
        # Check the path taken from the start point to the end point and append those spaces to a list
        if start[1] == end[1] and start[0] > end[0]:
            for move in moves:
                if move == end:  # Excludes the end value because that has already been tested.
                    continue
                # Depending on the path taken, we only want certain values. This one wants values where the
                # letter value is greater than the end letter value and less than the starting letter value
                elif end[0] < move[0] < start[0]:
                    path.append(move)
        elif start[1] == end[1] and start[0] < end[0]:
            for move in moves:
                if move == end:
                    continue
                elif end[0] > move[0] > start[0]:
                    path.append(move)
        elif start[0] == end[0] and start[1] < end[1]:
            for move in moves:
                if move == end:
                    continue
                elif end[1] > move[1] > start[1]:
                    path.append(move)
        else:
            for move in moves:
                if move == end:
                    continue
                elif end[1] < move[1] < start[1]:
                    path.append(move)

        return path


class Knight:
    """
    Represents a Knight object with a specific location. Interacts with the Space class
    directly (it is initialized within a Space object) and the ChessVar class (the ChessVar
    class will check its various properties like location and player owner and assign it a new
    location if a move is deemed possible).
    """
    def __init__(self, location):
        """
        Initialises a Knight object with a specific location. The only parameter is the location.
        The type of piece is also declared but nothing that is passed is used to declare it.
        """
        self._location = location
        self._type = "Knight"

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location

    def potential_moves(self):
        """
        Takes no parameters and returns all potential moves from current position
        This will be used in the ChessVar class's make_move method to check if a proposed move
        can occur.
        """

        moves = []
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        location = self.get_location()

        letter_value = x_axis.index(location[0])
        number_value = y_axis.index(location[1])

        start_letter_value = letter_value
        start_number_value = number_value

        # A knight could, at maximum, have 8 legal moves depending on where on the board it is.
        # This method appends all the moves that are legal (not off the board) to a list.
        # Check every variation of adding and subtracting one and 2 to the letter and number values.
        letter_value += 1
        number_value += 2

        if letter_value > 7 or number_value > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        letter_value -= 1
        number_value += 2
        if letter_value < 0 or number_value > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        letter_value += 1
        number_value -= 2
        if letter_value > 7 or number_value < 0:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        letter_value -= 1
        number_value -= 2
        if letter_value < 0 or number_value < 0:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        letter_value += 2
        number_value += 1
        if letter_value > 7 or number_value > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        letter_value -= 2
        number_value += 1
        if letter_value < 0 or number_value > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        letter_value += 2
        number_value -= 1
        if letter_value > 7 or number_value < 0:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            letter_value = start_letter_value
            number_value = start_number_value
            moves.append(final_value)

        letter_value -= 2
        number_value -= 1
        if letter_value < 0 or number_value < 0:
            return moves
        else:
            letter_value = x_axis[letter_value]
            number_value = y_axis[number_value]
            final_value = letter_value + number_value
            moves.append(final_value)
            return moves


class Bishop:
    """
    Represents a Bishop with a specific location. Interacts with the Space class
    directly (it is initialized within a Space object) and the ChessVar class (the ChessVar
    class will check its various properties like location and player owner and assign it a new
    location if a move is deemed possible).
    """
    def __init__(self, location):
        """
        Initialises a Bishop object with a specific location. The only parameter is the location.
        The type of piece is also declared but nothing that is passed is used to declare it.
        """
        self._location = location
        self._type = "Bishop"

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location

    def potential_moves(self):
        """
        Takes no parameters and returns all potential moves from current position
        This will be used in the ChessVar class's make_move method to check if a proposed move
        can occur.
        """

        moves = []
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        location = self.get_location()

        letter_value = x_axis.index(location[0])
        number_value = y_axis.index(location[1])
        start_letter_value = letter_value
        start_number_value = number_value

        letter_value = start_letter_value
        number_value = start_number_value

        # Checks the four potential directions a bishop can travel and appends all legal moves to a list
        # Directions are NorthWest, NorthEast, SouthWest, and SouthEast
        for i in range(8):
            letter_value += 1
            number_value += 1
            if letter_value > 7 or number_value > 7:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value -= 1
            number_value -= 1
            if letter_value < 0 or number_value < 0:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value += 1
            number_value -= 1
            if letter_value > 7 or number_value < 0:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value -= 1
            number_value += 1
            if letter_value < 0 or number_value > 7:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        return moves

    def path_to_move(self, end):
        """
        This takes one parameter which is the place the piece will eventually end up.
        It returns a list of the spaces that the piece will pass through to eventually get
        to the specified end point. This is used in the ChessVar class's method, make_move
        to determine if a space in its path is occupied by something, and it will thus not be
        able to move through that space. Used by Rook, Bishop, Queen, and Pawn (first turn of
        movement only).
        """
        path = []
        moves = self.potential_moves()
        start = self.get_location()
        # Checks the path from the start point to the end point similarly to the Rook except using diagonal
        # movement rather than vertical and horizontal.
        if start[0] < end[0] and start[1] < end[1]:
            for move in moves:
                if move == end:
                    continue
                elif move[0] > end[0] and move[1] > end[1]:
                    continue
                elif move[0] > start[0] and move[1] > start[1]:
                    path.append(move)

        elif start[0] > end[0] and start[1] < end[1]:
            for move in moves:
                if move == end:
                    continue
                elif move[0] < end[0] and move[1] > end[1]:
                    continue
                elif move[0] < start[0] and move[1] > start[1]:
                    path.append(move)

        elif start[0] > end[0] and start[1] > end[1]:
            for move in moves:
                if move == end:
                    continue
                elif move[0] < end[0] and move[1] < end[1]:
                    continue
                elif move[0] < start[0] and move[1] < start[1]:
                    path.append(move)

        else:
            for move in moves:
                if move == end:
                    continue
                elif move[0] > end[0] and move[1] < end[1]:
                    continue
                elif move[0] > start[0] and move[1] < start[1]:
                    path.append(move)

        return path


class Queen:
    """
    Represents a Queen object with a specific location. Interacts with the Space class
    directly (it is initialized within a Space object) and the ChessVar class (the ChessVar
    class will check its various properties like location and player owner and assign it a new
    location if a move is deemed possible).
    """
    def __init__(self, location):
        """
        Initialises a Queen object with a specific location. The only parameter is the location.
        The type of piece is also declared but nothing that is passed is used to declare it.
        """
        self._location = location
        self._type = "Queen"

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location

    def potential_moves(self):
        """
        Takes no parameters and returns all potential moves from current position
        This will be used in the ChessVar class's make_move method to check if a proposed move
        can occur.
        """
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        moves = []
        location = self.get_location()

        # Combines both movement rules for Bishop and Rook and appends all legal moves to its list.
        for column in x_axis:
            if location[0] == column:
                continue
            else:
                moves.append(column + location[1])

        for row in y_axis:
            if location[1] == row:
                continue
            else:
                moves.append(location[0] + row)

        letter_value = x_axis.index(location[0])
        number_value = y_axis.index(location[1])
        start_letter_value = letter_value
        start_number_value = number_value

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value += 1
            number_value += 1
            if letter_value > 7 or number_value > 7:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value -= 1
            number_value -= 1
            if letter_value < 0 or number_value < 0:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value += 1
            number_value -= 1
            if letter_value > 7 or number_value < 0:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        letter_value = start_letter_value
        number_value = start_number_value

        for i in range(8):
            letter_value -= 1
            number_value += 1
            if letter_value < 0 or number_value > 7:
                continue
            else:
                current_letter = x_axis[letter_value]
                current_number = y_axis[number_value]
                final_value = current_letter + current_number
                moves.append(final_value)

        return moves

    def path_to_move(self, end):
        """
        This takes one parameter which is the place the piece will eventually end up.
        It returns a list of the spaces that the piece will pass through to eventually get
        to the specified end point. This is used in the ChessVar class's method, make_move
        to determine if a space in its path is occupied by something, and it will thus not be
        able to move through that space. Used by Rook, Bishop, Queen, and Pawn (first turn of
        movement only).
        """
        path = []
        moves = self.potential_moves()
        start = self.get_location()
        if start[1] == end[1] and start[0] > end[0]:
            for move in moves:
                if move == end:
                    continue
                elif end[0] < move[0] < start[0] and move[1] == start[1]:
                    path.append(move)
        elif start[1] == end[1] and start[0] < end[0]:
            for move in moves:
                if move == end:
                    continue
                elif end[0] > move[0] > start[0] and move[1] == start[1]:
                    path.append(move)
        elif start[0] == end[0] and start[1] < end[1]:
            for move in moves:
                if move == end:
                    continue
                elif end[1] > move[1] > start[1] and move[0] == start[0]:
                    path.append(move)
        elif start[0] == end[0] and start[1] > end[1]:
            for move in moves:
                if move == end:
                    continue
                elif end[1] < move[1] < start[1] and move[0] == start[0]:
                    path.append(move)
        elif start[0] < end[0] and start[1] < end[1]:
            for move in moves:
                if move == end:
                    continue
                elif move[0] > end[0] and move[1] > end[1]:
                    continue
                elif move[0] > start[0] and move[1] > start[1]:
                    path.append(move)

        elif start[0] > end[0] and start[1] < end[1]:
            for move in moves:
                if move == end:
                    continue
                elif move[0] < end[0] and move[1] > end[1]:
                    continue
                elif move[0] < start[0] and move[1] > start[1]:
                    path.append(move)

        elif start[0] > end[0] and start[1] > end[1]:
            for move in moves:
                if move == end:
                    continue
                elif move[0] < end[0] and move[1] < end[1]:
                    continue
                elif move[0] < start[0] and move[1] < start[1]:
                    path.append(move)

        else:
            for move in moves:
                if move == end:
                    continue
                elif move[0] > end[0] and move[1] < end[1]:
                    continue
                elif move[0] > start[0] and move[1] < start[1]:
                    path.append(move)

        return path


class King:
    """
    Represents a King object with a specific location. Interacts with the Space class
    directly (it is initialized within a Space object) and the ChessVar class (the ChessVar
    class will check its various properties like location and player owner and assign it a new
    location if a move is deemed possible).
    """
    def __init__(self, location):
        """
        Initialises a King object with a specific location. The only parameter is the location.
        The type of piece is also declared but nothing that is passed is used to declare it.
        """
        self._location = location
        self._type = "King"

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location

    def potential_moves(self):
        """
        Takes no parameters and returns all potential moves from current position
        This will be used in the ChessVar class's make_move method to check if a proposed move
        can occur.
        """
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        moves = []
        location = self.get_location()

        letter_value = x_axis.index(location[0])
        number_value = y_axis.index(location[1])
        start_letter_value = letter_value
        start_number_value = number_value

        # Like a knight, a king also has, at maximum, 8 legal moves at a given time. It might be less
        # but never more. Add and subtract 1 to both the letter and number values in every combination.
        current_letter = letter_value + 1
        current_number = number_value + 1

        if current_letter > 7 or current_number > 7:  # 7 and 0 are both bounds to ensure we don't go off the board
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value - 1
        current_number = number_value + 1

        if current_letter < 0 or current_number > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value + 1
        current_number = number_value - 1

        if current_letter > 7 or current_number < 0:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value - 1
        current_number = number_value - 1

        if current_letter < 0 or current_number < 0:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value + 0
        current_number = number_value + 1

        if current_number > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value - 1
        current_number = number_value + 0

        if current_letter < 0:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value + 1
        current_number = number_value + 0

        if current_letter > 7:
            letter_value = start_letter_value
            number_value = start_number_value
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            letter_value = start_letter_value
            number_value = start_number_value

        current_letter = letter_value + 0
        current_number = number_value - 1

        if current_number < 0:
            return moves
        else:
            final_value = x_axis[current_letter] + y_axis[current_number]
            moves.append(final_value)
            return moves


class Pawn:
    """
    Represents a Pawn object with a specific location. Interacts with the Space class
    directly (it is initialized within a Space object) and the ChessVar class (the ChessVar
    class will check its various properties like location and player owner and assign it a new
    location if a move is deemed possible).
    """
    def __init__(self, location, player):
        """
        Initialises a Pawn object with a specific location. The Pawn has two parameters, location
        and player, because the player is required to determine where it will be allowed to move.
        The Pawn is the only piece that can't move backwards. The type of piece is also declared
        but nothing that is passed is used to declare it.
        """
        self._location = location
        self._type = "Pawn"
        self._player = player
        # Pawn has a dedicated player value because it cannot move backwards, and it is important to
        # track which direction it can move.

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location

    def potential_moves(self):
        """
        Consider possible moves for a pawn whether its turn 1, or not and
        whether it is White or Black. Takes no parameters and returns all potential moves
        from current position. This will be used in the ChessVar class's make_move method
        to check if a proposed move can occur.
        """
        moves = []
        location = self.get_location()

        letter_value = location[0]
        number_value = int(location[1])
        start_number_value = number_value

        # Since a pawn cannot move backwards, it will only be at row 2 (or row 7 if its black) before it has
        # made any moves yet. This allows me to control the pawn into only moving 2 spaces on its first move.
        if self._player == "Black":
            if number_value == 7:
                number_value -= 2
                moves.append(letter_value + str(number_value))
                number_value = start_number_value
                number_value -= 1
                moves. append(letter_value + str(number_value))

                return moves

            number_value -= 1
            moves.append(letter_value + str(number_value))
            return moves

        else:
            if number_value == 2:
                number_value += 2
                moves.append(letter_value + str(number_value))
                number_value = start_number_value
                number_value += 1
                moves.append(letter_value + str(number_value))
                return moves

            number_value += 1
            moves.append(letter_value + str(number_value))
            return moves

    def potential_attacks(self):
        """
        Consider possible attacks for a pawn whether it is White or Black. Takes no parameters
        and returns all potential attacks that a pawn could make from its current position. This will
        also interact with the ChessVar class's make_move object to see if a proposed attack is feasible.
        """

        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        moves = []
        location = self.get_location()

        letter_value = x_axis.index(location[0])
        number_value = y_axis.index(location[1])

        start_letter_value = letter_value

        # The Pawn needs a separate method for attacking because it moves and attacks in two different ways.
        if self._player == "Black":
            letter_value += 1
            number_value += 1

            if letter_value > 7 or number_value > 7:
                moves = []
            else:
                moves.append(x_axis[letter_value] + y_axis[number_value])

            letter_value = start_letter_value

            letter_value -= 1
            if letter_value < 0 or number_value > 7:
                return moves
            else:
                moves.append(x_axis[letter_value] + y_axis[number_value])
                return moves
        else:
            letter_value += 1
            number_value -= 1
            if letter_value > 7 or number_value < 0:
                moves = []
            else:
                moves.append(x_axis[letter_value] + y_axis[number_value])

            letter_value = start_letter_value

            letter_value -= 1
            if letter_value < 0 or number_value < 0:
                return moves
            else:
                moves.append(x_axis[letter_value] + y_axis[number_value])
                return moves

    def path_to_move(self, end):
        """
        This takes one parameter which is the place the piece will eventually end up.
        It returns a list of the spaces that the piece will pass through to eventually get
        to the specified end point. This is used in the ChessVar class's method, make_move
        to determine if a space in its path is occupied by something, and it will thus not be
        able to move through that space. Used by Rook, Bishop, Queen, and Pawn (first turn of
        movement only).
        """
        path = []
        moves = self.potential_moves()
        player = self._player

        # The Pawn needs this method for its first movement if it moves two spaces
        if player == "White":
            for move in moves:
                if move == end:
                    continue
                else:
                    path.append(move)
        else:
            for move in moves:
                if move == end:
                    continue
                else:
                    path.append(move)

        return path


class Empty:
    """
    Represents an empty space. This Empty object is stored in a Space class and those
    Space objects will be checked by the ChessVar class to see if there is anything within
    the space. If a space is empty, it will have little functionality other than being a
    place-holder for when/if a piece moves there.
    """
    def __init__(self, location):
        """
        Initialises an object of class Empty with a specific location
        """
        self._location = location
        self._type = "None"

    def get_type(self):
        """
        Returns the type
        """
        return self._type

    def get_location(self):
        """
        Returns the location
        """
        return self._location


class ChessVar:
    """
    Represents a game of chess. Interacts with all other classes, either directly or indirectly.
    creates and changes the Space and various chess piece classes when using make_move. Checks the
    current state of the board with get_board_state.
    """
    def __init__(self):
        """
        Initialises a game of chess with a specific board and turn number. Takes no parameters and
        initialises a game_board object and turn_number that starts at 0 and increments as the game
        progresses.
        """
        self._turn_number = 0
        self._game_board = [
            [
                Space("Black", Rook("a8")),
                Space("Black", Knight("b8")),
                Space("Black", Bishop("c8")),
                Space("Black", Queen("d8")),
                Space("Black", King("e8")),
                Space("Black", Bishop("f8")),
                Space("Black", Knight("g8")),
                Space("Black", Rook("h8"))
            ],
            [
                Space("Black", Pawn("a7", "Black")),
                Space("Black", Pawn("b7", "Black")),
                Space("Black", Pawn("c7", "Black")),
                Space("Black", Pawn("d7", "Black")),
                Space("Black", Pawn("e7", "Black")),
                Space("Black", Pawn("f7", "Black")),
                Space("Black", Pawn("g7", "Black")),
                Space("Black", Pawn("h7", "Black"))
            ],
            [
                Space("None", Empty("a6")),
                Space("None", Empty("b6")),
                Space("None", Empty("c6")),
                Space("None", Empty("d6")),
                Space("None", Empty("e6")),
                Space("None", Empty("f6")),
                Space("None", Empty("g6")),
                Space("None", Empty("h6"))
            ],
            [
                Space("None", Empty("a5")),
                Space("None", Empty("b5")),
                Space("None", Empty("c5")),
                Space("None", Empty("d5")),
                Space("None", Empty("e5")),
                Space("None", Empty("f5")),
                Space("None", Empty("g5")),
                Space("None", Empty("h5"))
            ],
            [
                Space("None", Empty("a4")),
                Space("None", Empty("b4")),
                Space("None", Empty("c4")),
                Space("None", Empty("d4")),
                Space("None", Empty("e4")),
                Space("None", Empty("f4")),
                Space("None", Empty("g4")),
                Space("None", Empty("h4"))
            ],
            [
                Space("None", Empty("a3")),
                Space("None", Empty("b3")),
                Space("None", Empty("c3")),
                Space("None", Empty("d3")),
                Space("None", Empty("e3")),
                Space("None", Empty("f3")),
                Space("None", Empty("g3")),
                Space("None", Empty("h3"))
            ],
            [
                Space("White", Pawn("a2", "White")),
                Space("White", Pawn("b2", "White")),
                Space("White", Pawn("c2", "White")),
                Space("White", Pawn("d2", "White")),
                Space("White", Pawn("e2", "White")),
                Space("White", Pawn("f2", "White")),
                Space("White", Pawn("g2", "White")),
                Space("White", Pawn("h2", "White"))
            ],
            [
                Space("White", Rook("a1")),
                Space("White", Knight("b1")),
                Space("White", Bishop("c1")),
                Space("White", Queen("d1")),
                Space("White", King("e1")),
                Space("White", Bishop("f1")),
                Space("White", Knight("g1")),
                Space("White", Rook("h1"))
            ]
        ]

    def get_board_state(self):
        """
        Returns the current board state
        """
        return self._game_board

    def print_board(self):
        """
        Prints out the current board state to the console including x-axis and y-axis
        """
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]

        x_string = "   ".join(x_axis)
        print("   " + x_string)  # Empty space to account for y-axis labels

        board_state = self.get_board_state()

        for i in range(len(board_state)):
            row_array = []
            row = board_state[i]
            for space in row:
                space_value = ""
                if space.get_player() == "None":
                    space_value += "E "  # E stands for empty
                    row_array.append(space_value)
                    continue
                elif space.get_player() == "Black":
                    space_value += "B"
                else:
                    space_value += "W"  # This means the player is White

                if space.get_piece_object().get_type() == "Rook":
                    space_value += "R"
                    row_array.append(space_value)
                elif space.get_piece_object().get_type() == "Knight":
                    space_value += "H"
                    row_array.append(space_value)
                elif space.get_piece_object().get_type() == "Bishop":
                    space_value += "B"
                    row_array.append(space_value)
                elif space.get_piece_object().get_type() == "Queen":
                    space_value += "Q"
                    row_array.append(space_value)
                elif space.get_piece_object().get_type() == "King":
                    space_value += "K"
                    row_array.append(space_value)
                else:
                    space_value += "P"  # This piece is a pawn
                    row_array.append(space_value)

            row_string = "  ".join(row_array)
            print(y_axis[i] + "  " + row_string)

    def update_board(self, player, piece_type, move_to, move_from):
        """
        Updates the current board state after a move has been made. This means it will change the
        board to reflect a move that was just made, changing a piece and such, it will also check the
        get_game_state method to ensure no one has one the game yet.
        """
        board = self.get_board_state()
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        piece_column = x_axis.index(move_to[0])
        piece_row = y_axis.index(move_to[1])
        empty_column = x_axis.index(move_from[0])
        empty_row = y_axis.index(move_from[1])

        if piece_type == "Pawn":
            piece_moving = Space(player, Pawn(move_to, player))
        elif piece_type == "King":
            piece_moving = Space(player, King(move_to))
        elif piece_type == "Queen":
            piece_moving = Space(player, Queen(move_to))
        elif piece_type == "Rook":
            piece_moving = Space(player, Rook(move_to))
        elif piece_type == "Bishop":
            piece_moving = Space(player, Bishop(move_to))
        else:
            piece_moving = Space(player, Knight(move_to))

        # Replace the spot moved to with a new Space object (with piece object inside) and leave an empty space
        # in the spot the piece moved from.
        board[piece_row][piece_column] = piece_moving
        board[empty_row][empty_column] = Space("None", Empty(move_from))
        self.get_game_state()

    def get_game_state(self):
        """
        Returns UNFINISHED, BLACK_WON, or WHITE_WON depending on the state of the board.
        It does so by checking the pieces left on the board and if one player has none of a particular
        piece type, it declares the other player the winner.
        """
        pieces_left = []
        black_count = 0
        white_count = 0
        board = self.get_board_state()
        for row in board:
            for space in row:
                player = space.get_player()
                piece = space.get_piece_object().get_type()
                piece_tuple = (player, piece)
                if piece_tuple not in pieces_left:
                    pieces_left.append(piece_tuple)

        if len(pieces_left) < 13:
            for tup in pieces_left:
                if tup[0] == "Black":
                    black_count += 1
                elif tup[0] == "White":
                    white_count += 1
                else:
                    continue

            if black_count > white_count:
                return "BLACK_WON"
            else:
                return "WHITE_WON"
        else:
            return "UNFINISHED"

    def make_move(self, square_from, square_to):
        """
        Takes the starting square (square_from) and the end square (square_to) as
        parameters. It determines, through use of the player, potential_moves
        (or potential_attacks for Pawn), path_to_moves (if the piece in question has
        this), and more to determine if a particular move is allowed. If a move is
        allowed, the method returns True and otherwise, returns False
        """
        x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
        y_axis = ["8", "7", "6", "5", "4", "3", "2", "1"]
        board = self.get_board_state()
        column_from = x_axis.index(square_from[0])
        row_from = y_axis.index(square_from[1])
        column_to = x_axis.index(square_to[0])
        row_to = y_axis.index(square_to[1])
        from_space = board[row_from][column_from]
        to_space = board[row_to][column_to]
        from_piece = from_space.get_piece_object()
        from_type = from_piece.get_type()

        if from_space.get_player() == "None":
            return False
        else:
            move_set = from_piece.potential_moves()

        if self.get_game_state() != "UNFINISHED":
            return False

        # White moves only on even turns, Black moves only on odd.
        if self._turn_number % 2 == 0 and from_space.get_player() == "Black":
            return False
        elif self._turn_number % 2 != 0 and from_space.get_player() == "White":
            return False
        else:

            if from_type == "Pawn":
                attack_set = from_piece.potential_attacks()
                if square_to in attack_set:
                    if to_space.get_player() == from_space.get_player() or to_space.get_player() == "None":
                        return False
                    else:  # Check this
                        self.update_board(from_space.get_player(), from_type, square_to, square_from)
                        self._turn_number += 1
                        return True
                elif to_space.get_player() != "None":
                    return False

            if square_to in move_set:
                if to_space.get_player() == from_space.get_player():
                    return False
                else:
                    # The King and Knight don't have the path_to_move method. The king only moves one square at a time
                    # and the Knight jumps.
                    if from_type == "King" or from_type == "Knight":
                        self.update_board(from_space.get_player(), from_type, square_to, square_from)
                        self._turn_number += 1
                        return True
                    else:
                        path = from_piece.path_to_move(square_to)
                        # If the path value is an empty list, just update as is. There are no extra spaces to check.
                        if len(path) == 0:
                            self.update_board(from_space.get_player(), from_type, square_to, square_from)
                            self._turn_number += 1
                            return True
                        for move in path:
                            column_path = x_axis.index(move[0])
                            row_path = y_axis.index(move[1])
                            path_space = board[row_path][column_path]
                            if path_space.get_player() != "None":
                                return False
                        self.update_board(from_space.get_player(), from_type, square_to, square_from)
                        self._turn_number += 1
                        return True
            else:
                return False

new_game = ChessVar()
new_game.print_board()