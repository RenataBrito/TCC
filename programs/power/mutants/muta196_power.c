
int power (int left, int right)
{
   int rslt, i;
   rslt = left;
   if  ( (TRAP_ON_NEGATIVE(right) == 0) )  {
      rslt = 1;
   }
   else {
 for (i = 2; i <= right; i++)
  rslt = rslt * left;
   }
   return rslt;
}
int main (int argc, char* argv[])
{
int k,l;
   k = atoi(argv[1]);
   l = atoi(argv[2]);
   printf("The result is: %d\n", power(k,l));
   return 0;
}
