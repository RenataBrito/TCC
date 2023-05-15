
int countPositive (int x[], int length)
{
    int count = 0;
 int i;
    for (i = 0; i < length; i++) {
       if (x[i] >= 0) {
          count++;
       }
    }
     return (TRAP_ON_NEGATIVE(count)) ; 
}
int inArr[100];
int main(int argc, char* argv[])
{
    int i;
 for (i = 1; i < argc; i++) {
  inArr[i - 1] = atoi(argv[i]);
 }
 printf("Number of positive numbers is: %d\n", countPositive(inArr, argc - 1));
 return 0;
}
