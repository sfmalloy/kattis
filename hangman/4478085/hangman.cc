#include <iostream>
#include <string>
#include <set>

int main() {
    std::string word, letters;
    std::cin >> word >> letters; 
    
    int health = 10;
    
    std::set<char> unique;
    for (const char& l : word) {
        unique.insert(l);
    }

    size_t guesses = 0;
    for (size_t i = 0; i < letters.size() && health > 0 && guesses < unique.size(); ++i) {
        if (unique.insert(letters[i]).second) {
            --health;
            unique.erase(letters[i]);
        } else {
            ++guesses;
        }
    }
    
    std::cout << (health > 0 ? "WIN" : "LOSE") << '\n';

    return 0;
}
