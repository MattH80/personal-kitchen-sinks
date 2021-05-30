#include <iostream>
#include <string>

void find_repeated_values(int* a, int size_A, int* b, int size_B)
{
    int tempArray[1000] = {0};
    for(int i = 0; i < size_A; i++)
    {
        int currentValue = a[i];
        tempArray[currentValue] = 1;
    }

    int counter = 0;
    for(int i = 0; i < size_B; i++)
    {
        int currentValue = b[i];
        if(tempArray[currentValue])
        {
            std::cout << currentValue << "\n";
            counter++;
        }
    }

    std::cout << "Total Count: " << counter << "\n";
}


int main()
{
    int array1[5] = {42, 1, 57, 5, 317};
    int array2[6] = {5, 57, 11, 111, 256, 317};

    find_repeated_values(array1, 5, array2, 6);
    
}
