
int daysIn[] = {0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int cal (int month1, int day1, int month2,
                       int day2, int year)
{  
}
void main (int argc, char *argv[])
{
   int month1, day1, month2, day2, year, T;
   month1 = atoi(argv[1]);
   day1 = atoi(argv[2]);
   month2 = atoi(argv[3]);
   day2 = atoi(argv[4]);
   year = atoi(argv[5]);
   T = cal (month1, day1, month2, day2, year);
   printf("Result is: %d  \n", T);
}
