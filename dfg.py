def manage_queue():
    queue = []
    results = []

    while True:
        operation = input("Введите операцию, а для завершения введите 'exit': ")
        if operation == "exit":
            break
        parts = operation.split()
        if parts[0] == "COME":
            k = int(parts[1])
            if k > 0:
                queue.extend([0] * k)
            else:
                queue = queue[:k]
        elif parts[0] == "WORRY":
            i = int(parts[1])
            queue[i] = 1
        elif parts[0] == "QUIET":
            i = int(parts[1])
            queue[i] = 0
        elif parts[0] == "WORRY_COUNT":
            count = queue.count(1)
            results.append(count)
    for result in results:
        print(result)

manage_queue()