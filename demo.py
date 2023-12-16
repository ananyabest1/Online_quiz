def find_provinces(is_connected):
    n = len(is_connected)
    visited = [False] * n
    provinces = 0

    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if is_connected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            provinces += 1

    return provinces

def main():
    n = int(input())
    is_connected = [list(map(int, input().split())) for _ in range(n)]

    provinces = find_provinces(is_connected)
    print(provinces)

if __name__ == "__main__":
    main()
