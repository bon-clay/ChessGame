chess_places = {
    "rook": (
        (0, 0),
        (0, 7)
    ),
    "knight": (
        (0, 1),
        (0, 6),
    ),
    "bishop": (
        (0, 2),
        (0, 5),
    ),
    "queen": (
        (0, 3),
    ),
    "king": (
        (0, 4),
    ),
    "pawn": (
        *[(1, x) for x in range(8)],
    )
}
