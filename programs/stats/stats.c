/* Introduction to Software Testing, www.introsoftwaretesting.com
* Authors: Paul Ammann & Jeff Offutt
* Chapter 2, section 2.3, slide 15 */
#include <stdio.h>
#include <math.h>

/*Vinicius: the same issues that the Java version has were kept in this new version*/
/*that is, test 2 also produces NaNs as in the Java version*/

/* Example for data flow. Has some issues.
 * The calculation of mean fails with an empty numbers list.
 * The calculation of var fails with a numbers list of length one. */
void computeStats(int numbers[], int size)
{
	double med, var, sd, mean, sum, varsum;
	int i;
	sum = 0.0;
	for (i = 0; i < size; i++) {
		sum += numbers[i];
	}	
	/*the following line implies that the array must be sorted in ascending order*/
	med = numbers[size/2]; 
	mean = sum / size;
	
	varsum = 0.0;
	for (i = 0; i < size; i++) {
	   varsum = varsum  + ((numbers[i] - mean) * (numbers [i] - mean)); 
	}
	var = size <= 1 ? 0 : varsum / (size - 1);
	sd  = sqrt(var);
	printf("median:             %2.3f\n", med);
	printf("mean:               %2.3f\n", mean);
   	printf("variance:           %2.3f\n", var);
	printf("standard deviation: %2.3f\n", sd);
}

int numbers[100];
/*Driver function for stats*/
int main (int argc, char* argv[])
{
int i;

	for (i = 1; i < argc; i++)
		numbers[i-1] = atoi(argv[i]);
	computeStats(numbers, argc-1);
	printf("\n");	
	return 0;
}
