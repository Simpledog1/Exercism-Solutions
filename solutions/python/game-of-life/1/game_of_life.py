def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    new_grid = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] == 1:
                        live_neighbors += 1

            if matrix[row][col] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[row][col] = 1
            else:
                if live_neighbors == 3:
                    new_grid[row][col] = 1

    return new_grid