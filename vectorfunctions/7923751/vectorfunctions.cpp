#include <algorithm>
#include <numeric>

#include "vectorfunctions.h"

void backwards(std::vector<int>& vec) {
    for (size_t b = 0, f = vec.size() - 1; b < f; ++b, --f) {
        std::swap(vec[b], vec[f]);
    }
}

std::vector<int> everyOther(const std::vector<int>& vec) {
    std::vector<int> other;
    for (size_t i = 0; i < vec.size(); i += 2) {
        other.push_back(vec[i]);
    }

    return other;
}

int smallest(const std::vector<int>& vec) {
    return *std::min_element(std::begin(vec), std::end(vec));
}

int sum(const std::vector<int>& vec) {
    return std::accumulate(std::begin(vec), std::end(vec), 0);
}

int veryOdd(const std::vector<int>& suchVector) {
    int num = 0;
    for (size_t i = 1; i < suchVector.size(); i += 2) {
        if (suchVector[i] % 2 == 1)
            ++num;
    }

    return num;
}
