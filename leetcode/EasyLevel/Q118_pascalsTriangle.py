def generate(numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize row with all 1s
            for j in range(1, i):  # Compute middle values
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)  # Add row to result

        return triangle