
long
jday(mon, day, year)
int mon, day, year;
{
 long m = mon, d = day, y = year;
 long c, ya, j;
 if(m > 2) m -= 3;
 else {
  m += 9;
  --y;
 }
 c = y/100L;
 ya = y - (100L * c);
 j = (146097L * c) /4L + (1461L * ya) / 4L + (153L * m + 2L)/5L + d + 1721119L;
 return(j);
}
int *
jdate(j)
long j;
{
 static int ret[4];
 long d, m, y;
   (ret[3] = ((TRAP_ON_ZERO(j) + 1L) % 7L)) ; 
 j -= 1721119L;
 y = (4L * j - 1L)/146097L;
 j = 4L * j - 1L - 146097L * y;
 d = j/4L;
 j = (4L * d + 3L)/1461L;
 d = 4L * d + 3L - 1461L * j;
 d = (d + 4L)/4L;
 m = (5L * d - 3L)/153L;
 d = 5L * d - 3 - 153L * m;
 d = (d + 5L) / 5L;
 y = 100L * y + j;
 if(m < 10)
  m += 3;
 else {
  m -= 9;
  ++y;
 }
 ret[0] = m;
 ret[1] = d;
 ret[2] = y;
 return(ret);
}
int main(int argc, char *argv[])
{
long l;
int *d;
 if (argc > 2)
 {
  l = jday(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]));
  printf("Julian day: %ld\n", l);
 }
 else
 {
  l = atol(argv[1]);
  d = jdate(l);
  printf("Month: %d Day: %d Year: %d Week day: %d\n", d[0], d[1],d[2], d[3]);
 }
}
