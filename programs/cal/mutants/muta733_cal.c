
int daysIn[] = {0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int cal (int month1, int day1, int month2,
                       int day2, int year)
{
   int numDays, i;
   if (month2 == month1)
      numDays = day2 - day1;
   else
   {
      int m4 = year % 4;
      int m100 = year % 100;
      int m400 = year % 400;
      if ((m4 != 0) || ((m100 == 0) && (m400 != 0)))
         daysIn[2] = 28;
      else
         daysIn[2] = 29;
        (numDays = (day2 + (m4 - day1))) ;  
      for ( i = month1 + 1; i <= month2-1; i++)
         numDays = daysIn[i] + numDays;
   }
   return (numDays);
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
