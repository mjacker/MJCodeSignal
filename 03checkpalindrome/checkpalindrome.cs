bool solution(string inputString) {
    // convent input string to char array
    char [] reverseInput = inputString.ToCharArray();
    
    // reverse Array 
    Array.Reverse(reverseInput);
    
    // convert char array to string    
    string message = new string(reverseInput);
    
    // Return true if reversed is equal, false if not.
    if( message == inputString) return true;
    else return false;
}
