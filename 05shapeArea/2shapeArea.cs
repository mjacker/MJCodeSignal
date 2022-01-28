int solution(int n) {
    int sum = 0;
    for (int i = 0 ; i < n - 1 ; i++){
        sum += 2 + 4 * i;
    }
    sum += 1 + 2 * (n - 1);
    return sum;
}
