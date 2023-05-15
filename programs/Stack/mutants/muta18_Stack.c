
struct stack_node
{
    struct stack_node *above;
    int data;
    struct stack_node *below;
};
typedef struct stack_node stack_list;
typedef stack_list *link;
void join(link above, link below);
int push(int value);
int pop();
int isEmpty();
int removeBottom();
void print_stack();
link top;
link bottom;
int size = 0;
link stack1=((void *)0);
link stack2=((void *)0);
void join(link above, link below) {
 if (below != ((void *)0)) below->above = above;
 if  ( (above >= ((void (*)) 0) ) )  above->below = below;
}
int push(int value)
{
 link new_node;
 size++;
 new_node=(link) malloc(sizeof(stack_list));
 if(!new_node)
 {
  printf("Error\n");
  return 0;
 }
 if (size == 1) bottom = new_node;
 new_node->data=value;
 join(new_node, top);
 top = new_node;
 return 1;
}
int pop()
{
int k;
    if ( ! isEmpty() )
    {
 k = top->data;
 top = top->below;
 if ( top != ((void *)0) )
 {
  free(top->above);
  top->above = ((void *)0);
 }
 else
  bottom = top;
 size--;
 return k;
    }
    printf("Stack is empty\n");
    return 0;
}
int isEmpty()
{
 if(size==0)
  return 1;
 else
  return 0;
}
int removeBottom()
{
  link b = bottom;
  bottom = bottom->above;
  if(bottom!=((void *)0))
   bottom->below=((void *)0);
  size--;
  return b->data;
}
void print_stack()
{
link b = bottom;
 printf("Bottom - up: ");
 while ( b != ((void *)0) )
 {
  printf("%d ", b->data);
  b = b->above;
 }
 printf("\n");
}
void main(int argc, char *argv[])
{
    driver(atoi(argv[1]));
}
