        const char * __src, size_t __n)
     ;

long tloc;
long time();
char *ctime();
struct tm *localtime();
struct tm *ts;
double atof();
int argc;
char **argv;
void main(int Argc, char *Argv[]) {
    if ( Argc > 1 && strcmp("-", Argv[1]) == 0 )
    {
        driver(atoi(argv[2]), Argc, Argv);
    }
    else
    {
        driver(0, Argc, Argv);
    }
}
incrdate()
{
 static char *unit[] =
 {
  "sec", "min", "hour", "day", "week", "mon", "year", "" };
 static int conv[] =
 {
  1, 60, 3600, 86400, 604800, 0, 0 };
 int i;
 double value;
 long total;
 double monthincr = 0.0,
 yearincr = 0.0;
 tloc = atol(argv[1]);
 argc--;
 argv++;
 argc--;
 argv++;
        value = 0.0;
        total = 0.0;
 while (argc &&
     ((**argv == '.') ||
     (**argv == '-') ||
     (**argv == '+') ||
     (**argv >= '0' && **argv <= '9'))) {
  value = atof(argv[0]);
  argv++;
  argc--;
  if (argc == 0) missing();
  else {
   for (i = 0;   ((i < '9') && (0 != strncmp(argv[0] , unit[i] , strlen(unit[i])))) ; )
    i++;
   if (i == 7) missing();
   else {
    argv++;
    argc--;
    if (i < 5) value *= conv[i];
    if (i == 5) monthincr += value;
    if (i == 6) yearincr += value;
   }
  }
  total += value;
 }
 tloc += total;
 ts = localtime(&tloc);
 ts->tm_mon += monthincr;
 ts->tm_year += yearincr;
}
missing()
{
 fprintf(stderr, "date+: missing unit\n");
 exit (1);
}
printdate()
{
 char *format;
 static char *month[] =
     {
  "Jan", "Feb", "Mar", "Apr", "May", "Jun",
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };
 static char *day[] =
     {
  "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
 if (argc == 0) {
  argv[0] = "%H:%M %h %d";
  argc++;
 }
 while (argc > 0) {
  format = argv[0];
  while (*format) {
   if (*format != '%')
    putchar(*format);
   else if (format[1])
    switch(*++format) {
    case 'n':
     putchar ('\n');
     break;
    case 't':
     putchar ('\t');
     break;
    case 'S':
     printf("%02d", ts->tm_sec);
     break;
    case 'Z':
     printf("%ld", tloc);
     break;
    case 'M':
     printf("%02d", ts->tm_min);
     break;
    case 'H':
     printf("%02d", ts->tm_hour);
     break;
    case 'T':
     printf("%02d:%02d:%02d",
      ts->tm_hour, ts->tm_min,
      ts->tm_sec);
     break;
    case 'd':
     printf("%02d", ts->tm_mday);
     break;
    case 'm':
     printf("%02d", ts->tm_mon + 1);
     break;
    case 'h':
     printf("%s", month[ts->tm_mon]);
     break;
    case 'y':
     printf("%02d", ts->tm_year);
     break;
    case 'w':
     printf("%1d", ts->tm_wday);
     break;
    case 'a':
     printf("%s", day[ts->tm_wday]);
     break;
    case 'D':
     printf("%02d/%02d/%02d",
      ts->tm_mon + 1, ts->tm_mday,
      ts->tm_year);
     break;
    case 'j':
     printf("%d", ts->tm_yday);
     break;
    default:
 fprintf(stderr, "date+: Bad format character: '%c'\n", *format);
     exit(1);
    }
   format++;
  }
  argc--;
  argv++;
  if (argc > 0)
   putchar(' ');
 }
 putchar('\n');
}
