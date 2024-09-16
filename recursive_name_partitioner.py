import pandas as pd

def calculate_partitions(df, goal, boundaries, depth, max_depth):
    if max_depth == 0:
        # Handle the case for a single partition
        partition_size = len(df)
        score = (goal - partition_size) ** 2
        if score >= 0:
            print(f'A-Z:{partition_size} - score={score}')
        return

    if depth == max_depth:
        partitions = []
        start = 'A'
        for boundary in boundaries:
            end = chr(64 + boundary)
            query_string = f'LastNameFirstLetter >= "{start}" and LastNameFirstLetter <= "{end}"'
            bucket = df.query(query_string)
            partitions.append(len(bucket))
            start = chr(65 + boundary)
        query_string = f'LastNameFirstLetter >= "{start}" and LastNameFirstLetter <= "Z"'
        bucket = df.query(query_string)
        partitions.append(len(bucket))

        score = sum((goal - size) ** 2 for size in partitions)
        if score >= 0:
            partition_ranges = [f'{chr(64 + boundaries[i-1] + 1)}-{chr(64 + boundaries[i])}:{partitions[i]}' for i in range(1, len(boundaries))]
            partition_ranges.insert(0, f'A-{chr(64 + boundaries[0])}:{partitions[0]}')
            partition_ranges.append(f'{chr(65 + boundaries[-1])}-Z:{partitions[-1]}')
            print(f'{", ".join(partition_ranges)} - score={score}')
        return

    start = boundaries[-1] + 1 if boundaries else 1
    for boundary in range(start, 26 - (max_depth - depth)):
        calculate_partitions(df, goal, boundaries + [boundary], depth + 1, max_depth)

if __name__ == '__main__':
    data = {
        'first_name': ['John', 'Jane', 'Jim', 'Jenny', 'Jack'],
        'last_name': ['Doe', 'Smith', 'Brown', 'Smith', 'Black']
    }
    df = pd.DataFrame(data)

    # Add a column to the dataframe with the first letter of the 'Last Name' field
    df['LastNameFirstLetter'] = df['last_name'].str[0]

    goal = 2
    max_depth = 0  # Change this value to support different levels of depth

    calculate_partitions(df, goal, [], 0, max_depth)