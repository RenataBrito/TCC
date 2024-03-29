     ;

char dayw[] = {
 " S  M Tu  W Th  F  S"
};
char *smon[]= {
 "January", "February", "March", "April",
 "May", "June", "July", "August",
 "September", "October", "November", "December",
};
char string[432];
main(argc, argv)
int argc;
char *argv[];
{
    if ( argc > 1 && strcmp("-", argv[1]) == 0 )
    {
        driver(atoi(argv[2]), argc, argv);
    }
    else
    {
        driver(0, argc, argv);
    }
    return 0;
}
dispatch(argc, argv)
char *argv[];
{
 register y, i, j;
 int m;
 if(argc == 2)
  goto xlong;
 if(argc < 2) {
  time_t t;
  struct tm *tm;
  t = time(0);
  tm = (struct tm *) localtime(&t);
  m = tm->tm_mon + 1;
  y = tm->tm_year + 1900;
 } else {
  m = atoi(argv[1]);
  if(m<1 || m>12) {
   fprintf(stderr, "cal: %s: Bad month.\n", argv[1]);
   exit(1);
  }
  y = atoi(argv[2]);
  if(y<1 || y>9999) {
   fprintf(stderr, "cal: %s: Bad year.\n", argv[2]);
   exit(2);
  }
 }
   (printf("   %s %u\n" , smon[(m - 1)] , TRAP_ON_NEGATIVE(y))) ; 
 printf("%s\n", dayw);
 cal(m, y, string, 24);
 for(i=0; i<6*24; i+=24)
  pstr(string+i, 24);
 exit(0);
xlong:
 y = atoi(argv[1]);
 if(y<1 || y>9999) {
  fprintf(stderr, "cal: %s: Bad year.\n", argv[1]);
  exit(2);
 }
 printf("\n\n\n");
 printf("				%u\n", y);
 printf("\n");
 for(i=0; i<12; i+=3) {
  for(j=0; j<6*72; j++)
   string[j] = '\0';
  printf("	 %.3s", smon[i]);
  printf("			%.3s", smon[i+1]);
  printf("		       %.3s\n", smon[i+2]);
  printf("%s   %s   %s\n", dayw, dayw, dayw);
  cal(i+1, y, string, 72);
  cal(i+2, y, string+23, 72);
  cal(i+3, y, string+46, 72);
  for(j=0; j<6*72; j+=72)
   pstr(string+j, 72);
 }
 printf("\n\n\n");
 exit(0);
}
pstr(str, n)
char *str;
{
 register i;
 register char *s;
 s = str;
 i = n;
 while(i--)
  if(*s++ == '\0')
   s[-1] = ' ';
 i = n+1;
 while(i--)
  if(*--s != ' ')
   break;
 s[1] = '\0';
 printf("%s\n", str);
}
char mon[] = {
 0,
 31, 29, 31, 30,
 31, 30, 31, 31,
 30, 31, 30, 31,
};
cal(m, y, p, w)
char *p;
{
 register d, i;
 register char *s;
 s = p;
 d = jan1(y);
 mon[2] = 29;
 mon[9] = 30;
 switch((jan1(y+1)+7-d)%7) {
 case 1:
  mon[2] = 28;
  break;
 default:
  mon[9] = 19;
  break;
 case 2:
  ;
 }
 for(i=1; i<m; i++)
  d += mon[i];
 d %= 7;
 s += 3*d;
 for(i=1; i<=mon[m]; i++) {
  if(i==3 && mon[m]==19) {
   i += 11;
   mon[m] += 11;
  }
  if(i > 9)
   *s = i/10+'0';
  s++;
  *s++ = i%10+'0';
  s++;
  if(++d == 7) {
   d = 0;
   s = p+w;
   p = s;
  }
 }
}
jan1(yr)
{
 register y, d;
 y = yr;
 d = 4+y+(y+3)/4;
 if(y > 1800) {
  d -= (y-1701)/100;
  d += (y-1601)/400;
 }
 if(y > 1752)
  d += 3;
 return(d%7);
}
