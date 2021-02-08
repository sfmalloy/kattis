#include <iostream>

int main() {
	int a, b, c;
	std::cin >> a >> b >> c;

	unsigned moveCount = 0;
	while (c - a > 2) {
		++moveCount;
		if (b - a < c - b) {
			a = b;
			b = a + 1;
		} else {
			c = b;
			b = c - 1;
		}
	}

	std::cout << moveCount << '\n';
	
	return 0;
}
