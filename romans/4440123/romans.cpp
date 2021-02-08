#include <iostream>

int main() {
	double x;
	std::cin >> x;

	printf("%.0f\n", x * (1000 * (5280.0/4854.0)));

	return 0;
}
