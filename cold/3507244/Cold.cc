#include <iostream>

int
main(int argc, char* argv[])
{
    int N;
    std::cin >> N;
    
    int count = 0;

    for (int i = 0; i < N; ++i)
    {
        int temp;
        std::cin >> temp;
        if (temp < 0)
            ++count;
    }

    std::cout << count << std::endl;

    return 0;
}