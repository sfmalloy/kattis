#include <iostream>

int main() {
	int x, y;
	std::cin >> x >> y;

	if (x < 0) {
		if (y < 0)
			std::cout << 3 << '\n';
		else
			std::cout << 2 << '\n';
	} else {
		if (y < 0)
			std::cout << 4 << '\n';
		else
			std::cout << 1 << '\n';
 	}

	return 0;
}
