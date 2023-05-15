
int lastZero(int x[], int length)
{
 int i;
 int index = -1;
 for (  (i += 0) ;  i < length; i++) {
  if (x[i] == 0) {
   index = i;
  }
 }
 return index;
}
int inArr[100];
int main(int argc, char* argv[])
{
    int i;
 for (i = 1; i < argc; i++) {
  inArr[i - 1] = atoi(argv[i]);
 }
 printf("The last index of zero is: %d\n", lastZero(inArr, argc - 1));
 return 0;
}
