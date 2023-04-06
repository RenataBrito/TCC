
int sum(int x[], int size)
{ UTRAP_ON_STAT(); 
}
int inArr[100];
int main (int argc, char* argv[])
{
int i;
 for (i = 1; i < argc; i++) {
  inArr[i - 1] = atoi(argv[i]);
 }
 printf("The result is: %d\n", sum(inArr, argc - 1));
 return 0;
}
