#include <iostream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

int
main(int argc, char* argv[])
{
    int cases;
    cin >> cases;
    
    vector<double> aboveAverage;

    for (int i = 0; i < cases; ++i)
    {
        float students;
        cin >> students;

        vector<float> grades;
        float average = 0;
        for (int j = 0; j < students; ++j)
        {
            double grade;
            cin >> grade;
            grades.push_back(grade);
            average += grade;
        }

        average /= grades.size();
        int count = 0;
        for (float grade : grades)
        {
            if (grade > average)
            {
                ++count;
            }
        }

        aboveAverage.push_back((double) count / students);
    }

    for (double percent : aboveAverage)
    {
        printf("%.3f%%\n", percent * 100);
    }

    return 0;
}