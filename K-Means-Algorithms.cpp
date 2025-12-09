/**
 * @file K-Means-Algorithms.cpp
 * @brief Simple 1D K-Means clustering implementation in C++.
 *
 * This program demonstrates a basic K-Means clustering algorithm on a set of 10 integers.
 * It asks the user to input 10 numbers and 2 initial means. It then iteratively
 * groups the numbers into two clusters based on the nearest mean and recalculates
 * the means until convergence.
 *
 * @note This code uses legacy headers (<iostream.h>, <conio.h>) and syntax,
 *       targeting older compilers like Turbo C++. It may not compile on modern
 *       standard-compliant C++ compilers without modification.
 */

#include <iostream.h>
#include <conio.h>

/**
 * @brief Main execution function.
 *
 * Performs the following steps:
 * 1. Takes 10 integer inputs from the user.
 * 2. Takes 2 initial mean values from the user.
 * 3. Iteratively:
 *    - Assigns each number to the cluster defined by the closest mean.
 *    - Recalculates the mean of each cluster.
 *    - Prints the current clusters and their means.
 *    - Repeats until the means stop changing.
 *
 * @return void (Standard C++ expects int, but void is used here as per legacy style)
 */
void main()
{
    int i1, i2, i3, t1, t2;

    int k0[10];
    int k1[10];
    int k2[10];

    cout << "\nEnter 10 numbers:\n";
    for (i1 = 0; i1 < 10; i1++)
    {
        cin >> k0[i1];
    }

    //initial means
    int m1;
    int m2;

    cout << "\n Enter initial mean 1:";
    cin >> m1;
    cout << "\n Enter initial mean 2:";
    cin >> m2;

    int om1, om2; //old means

    do
    {

        //saving old means
        om1 = m1;
        om2 = m2;

        //creating clusters
        i1 = i2 = i3 = 0;
        for (i1 = 0; i1 < 10; i1++)
        {
            //calculating distance to means
            t1 = k0[i1] - m1;
            if (t1 < 0)
            {
                t1 = -t1;
            }

            t2 = k0[i1] - m2;
            if (t2 < 0)
            {
                t2 = -t2;
            }

            if (t1 < t2)
            {
                //near to first mean
                k1[i2] = k0[i1];
                i2++;
            }
            else
            {
                //near to second mean
                k2[i3] = k0[i1];
                i3++;
            }
        }

        t2 = 0;
        //calculating new mean
        for (t1 = 0; t1 < i2; t1++)
        {
            t2 = t2 + k1[t1];
        }
        if (i2 > 0) m1 = t2 / i2; // Avoid division by zero if cluster is empty

        t2 = 0;
        for (t1 = 0; t1 < i3; t1++)
        {
            t2 = t2 + k2[t1];
        }
        if (i3 > 0) m2 = t2 / i3; // Avoid division by zero if cluster is empty

        //printing clusters
        cout << "\nCluster 1:";
        for (t1 = 0; t1 < i2; t1++)
        {
            cout << k1[t1] << " ";
        }
        cout << "\nm1=" << m1;

        cout << "\nCluster 2:";
        for (t1 = 0; t1 < i3; t1++)
        {
            cout << k2[t1] << " ";
        }
        cout << "\nm2=" << m2;

        cout << "\n ----";
    } while (m1 != om1 && m2 != om2);

    cout << "\n Clusters created";

    //ending
    getch();
}
