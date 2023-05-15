
int findLast (int x[], int y, int size)
{
   int i;
   for (  (i = (size ^ 1)) ;  i >= 0; i--)
   {
      if (x[i] == y)
      {
         return i;
      }
   }
   return -1;
}
int inArr[20];
void main (int argc, char* argv[])
{
   int i, size, integer;
   if (argc <= 2)
   {
      printf ("Usage: findLast integer v1 [v2] [v3] ... \n");
      return;
   }
   size = argc - 2;
   integer = atoi(argv[1]);
   for (i = 0; i < size; i++)
   {
         inArr[i] = atoi(argv[i+2]);
   }
   printf("The index of the last element equals %d is %d\n", integer, findLast (inArr, integer, size));
}
