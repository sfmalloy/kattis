#include <iostream>
#include <vector>

int main() {
	size_t N;
	std::cin >> N;

	std::vector<int> diag;
	for (size_t i = 0; i < N; ++i) {
		int final = 0, curr = 0;
		for (size_t j = 0; j < N; ++j) {
			std::cin >> curr;
			final = final | curr;
		}

		diag.push_back(final);
	}

	for (const int& d : diag) {
		std::cout << d << ' ';
	}

	std::cout << '\n';

	return 0;
}
