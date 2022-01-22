int solution(int year) {
    int centuryMod, centuryRound;
    centuryMod = year % 10;
    centuryRound = year  100;
    
    if (year  100) return 1;
    if ((centuryMod) == 0 ) return centuryRound;
    else 
        return (centuryRound) + 1;
}
