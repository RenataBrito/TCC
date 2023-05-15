     ;

void sort(double *list, int low, int high) {
int min, indexOfMin, i;
 if (low < high) {
     min = list[low];
       (indexOfMin += low) ; 
     for (i = low + 1; i <= high; i++)
     {
      if (list[i] < min)
      {
       min = list[i];
       indexOfMin = i;
      }
     }
     list[indexOfMin] = list[low];
     list[low] = min;
     sort(list, low + 1, high);
 }
  }
double list[100];
void main(int argc, char *argv[]) {
int i;
    for (i = 1; i < argc; i++)
 list[i-1] = atof(argv[i]);
    sort(list, 0, i - 2);
    printf("******** Sorted numbers: \n");
    for (i = 0; i < argc-1; i++)
   printf("%.lf ",list[i]);
    printf("\n");
  }
