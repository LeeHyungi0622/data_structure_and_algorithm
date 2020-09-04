def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

# 최대 몇 개가 필요한지 : N
# 현재의 행 : current_row
def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)

            current_candidate.pop()

def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

def main():
    print(solve_n_queens(4))

if __name__ == "__main__":
    main()