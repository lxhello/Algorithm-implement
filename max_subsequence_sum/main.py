def main():
    items = list(map(int, input("enter liet:").split(",")))
    overall = partial = items[0]
    for i in range(1, len(items)):
        # 0 -2 3 5 -1 2
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == "__main__":
    main()
