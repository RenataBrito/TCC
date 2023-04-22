
char twoPred(int x, int y)
{
 int z = 0;
 if (x < y)
    (z = 0) ; 
 else
  z = 0;
 if (z && x + y == 10)
  return 'A';
 else
  return 'B';
}
int main (int argc, char* argv[])
{
 printf("The result is: %c\n", twoPred(atoi(argv[1]), atoi(argv[2])));
 return 0;
}
