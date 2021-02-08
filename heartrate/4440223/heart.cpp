#include <iostream>
#include <vector>

int main() {
	int cases;
	std::cin >> cases;
	std::vector<double> min, mid, max;
	
	for (int i = 0; i < cases; ++i) {
		int b;
		double p;
		std::cin >> b >> p;

		double abpm = 60 / p;
		double bpm = abpm * b;

		min.push_back(bpm - abpm);
		mid.push_back(bpm);
		max.push_back(bpm + abpm);
	}

	for (int i = 0; i < cases; ++i) {
		printf("%.4f %.4f %.4f\n", min[i], mid[i], max[i]);
	}

	return 0;
}
