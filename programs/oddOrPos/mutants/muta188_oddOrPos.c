
int oddOrPos (int x[], int length)
{
    int count = 0;
 int i;
    for (i = 0; i < length; i++) {
  if  ( (((x[i] % 2) == (- 1)) || (x[i] > 0)) )  {
   count++;
  }
 }
    return count;
}
int inArr[100];
int main(int argc, char* argv[])
{
    int i;
 for (i = 1; i < argc; i++) {
  inArr[i - 1] = atoi(argv[i]);
 }
 printf("Number of elements that are either odd or positive is: %d\n", oddOrPos (inArr, argc - 1));
 return 0;
}
