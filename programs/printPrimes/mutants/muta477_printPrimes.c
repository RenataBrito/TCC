
int isDivisible (int i, int j)
{
   if (j%i == 0)
      return 1;
   else
      return 0;
}
void printPrimes (int n)
{  
}
void main (int argc, char *argv[])
{
   int integer = 0;
   integer = atoi(argv[1]);
   printPrimes(integer);
}
