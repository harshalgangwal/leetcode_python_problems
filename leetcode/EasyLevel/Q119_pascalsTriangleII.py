def getRow(rowIndex: int) -> List[int]:
        row = [1]  # Initialize the first row

        for i in range(rowIndex):  
            row.append(1)  # Add a 1 at the end
            for j in range(len(row) - 2, 0, -1):  # Update elements from right to left
                row[j] = row[j] + row[j - 1]

        return row 