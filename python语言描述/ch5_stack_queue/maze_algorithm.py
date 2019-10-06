"""
求解迷宫的算法
"""

from python语言描述.ch5_stack_queue.stack import SStack
from python语言描述.ch5_stack_queue.queue import SQueue

dirs = [(0, 1), (1, 0), (0, -1), (-1,0)]


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
    """递归求解"""
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=" ")
                return True
    return False


def print_path(end, pos, st):
    print("path:")
    print(end, pos, end=' ')

    while not st.is_empty():
        print(st.pop()[0], end=' ')


def maze_solver(maze, start, end):
    """栈和回溯法"""
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])

            if nextp == end:
                print_path(end, pos, st)
                return
            if passable(maze, nextp):
                st.push((pos, i+1))
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print("No path found.")


def maze_solver_queue(maze, start, end):
    """队列"""
    if start == end:
        print("Path finds")
        return
    sq = SQueue()
    mark(maze, start)
    sq.enqueue(start)
    while not sq.is_empty():
        pos = sq.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])

            if passable(maze, nextp):
                if nextp == end:
                    print("Path find.")
                    return
                mark(maze, nextp)
                sq.enqueue(nextp)
    print("No path.")


if __name__ == "__main__":
    maze = [[1]*6, [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1]*6]
    print(maze)

    # 递归法
    # find_path(maze, pos=(1, 1), end=(5, 4))

    # 栈
    # maze_solver(maze, start=(1, 1), end=(5, 4))

    # 队列
    maze_solver_queue(maze, start=(1, 1), end=(5, 4))

